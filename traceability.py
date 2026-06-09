import os
import re
import sys

# Patterns
SYSML_ID_PATTERN = re.compile(r'attribute\s+id\s*=\s*"([^"]+)"')
SYSML_STATUS_PATTERN = re.compile(r'attribute\s+(?:status|requirement_status)\s*=\s*"([^"]+)"')
C_SATISFIES_PATTERN = re.compile(r'@satisfies\s+([A-Za-z0-9_-]+)')


def parse_sysml_files(directory):
    requirements = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.sysml'):
                path = os.path.join(root, file)

                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    for m in re.finditer(r"\brequirement\b", content):
                        brace_start = content.find('{', m.end())
                        if brace_start == -1:
                            continue

                        depth = 0
                        i = brace_start
                        block = None

                        while i < len(content):
                            if content[i] == '{':
                                depth += 1
                            elif content[i] == '}':
                                depth -= 1
                                if depth == 0:
                                    block = content[brace_start+1:i]
                                    break
                            i += 1

                        if block is None:
                            continue

                        id_match = SYSML_ID_PATTERN.search(block)
                        status_match = SYSML_STATUS_PATTERN.search(block)

                        if id_match:
                            req_id = id_match.group(1)
                            status = status_match.group(1) if status_match else "Unknown"

                            requirements[req_id] = {
                                "status": status,
                                "file": os.path.relpath(path),
                                "implemented": False,
                                "implemented_in": []
                            }

    return requirements


def check_c_implementations(directory, requirements):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.c', '.h')):
                path = os.path.join(root, file)

                with open(path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        matches = C_SATISFIES_PATTERN.findall(line)

                        for req_id in matches:
                            if req_id in requirements:
                                requirements[req_id]["implemented"] = True
                                requirements[req_id]["implemented_in"].append(
                                    f"{os.path.relpath(path)}:Line {line_num}"
                                )
                            else:
                                print(f" Warnung: Unbekannte ID {req_id} in {file}:L{line_num}")


def generate_report(requirements):
    print("\n" + "="*80)
    print(f"{'ANFORDERUNG':<25} | {'STATUS':<12} | {'IMPLEMENTIERT?'}")
    print("="*80)

    missing = 0

    for req_id, data in sorted(requirements.items()):
        status = data["status"]

        if status in ["Approved", "Released", "Active"] and not data["implemented"]:
            print(f"{req_id:<25} | {status:<12} |  FEHLT")
            missing += 1

        elif data["implemented"]:
            print(f"{req_id:<25} | {status:<12} |  Ja")

        else:
            print(f"{req_id:<25} | {status:<12} | ➖ Optional")

    print("="*80)
    return missing


def generate_markdown_report(requirements, output_file="requirements_report.md"):
    total = len(requirements)
    implemented = sum(1 for r in requirements.values() if r["implemented"])

    coverage = (implemented / total * 100) if total > 0 else 0

    with open(output_file, 'w', encoding='utf-8') as md:
        md.write("# Traceability Report\n\n")
        md.write(f"**Gesamt Anforderungen:** {total}\n\n")
        md.write(f"**Implementiert:** {implemented} ({coverage:.1f}%)\n\n")

        md.write("| ID | Status | Implementiert | Datei |\n")
        md.write("|----|--------|--------------|-------|\n")

        for req_id, data in sorted(requirements.items()):
            status = data["status"]
            impl = "ok" if data["implemented"] else "NO"
            file = data["file"]

            md.write(f"| {req_id} | {status} | {impl} | {file} |\n")

    print(f" Report erstellt: {output_file}")


if __name__ == "__main__":

    # MEINE PFADE
    sysml_dir = "./software/model"
    c_dir = "./software"

    print("🔍 Starte Traceability Check...\n")

    requirements = parse_sysml_files(sysml_dir)

    check_c_implementations(c_dir, requirements)

    missing = generate_report(requirements)

    generate_markdown_report(requirements)

    if missing > 0:
        print(f"\n {missing} Anforderungen fehlen!")
        sys.exit(1)
    else:
        print("\n Alle Anforderungen erfüllt!")
        sys.exit(0)