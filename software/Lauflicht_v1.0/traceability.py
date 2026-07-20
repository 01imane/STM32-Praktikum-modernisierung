import os
import re
import sys

# =====================================================
# SysML Patterns
# =====================================================

SYSML_ID_PATTERN = re.compile(
    r'attribute\s+id\s*=\s*"([^"]+)"'
)

SYSML_REQ_STATUS_PATTERN = re.compile(
    r'attribute\s+requirement_status\s*=\s*"([^"]+)"'
)

SYSML_IMPL_STATUS_PATTERN = re.compile(
    r'attribute\s+implementation_status\s*=\s*"([^"]+)"'
)

SYSML_DERIVED_PATTERN = re.compile(
    r'derived\s+([A-Za-z0-9_]+)'
)

SYSML_DOC_PATTERN = re.compile(
    r'doc\s*/\*(.*?)\*/',
    re.DOTALL
)

C_SATISFIES_PATTERN = re.compile(
    r'@satisfies\s+([A-Za-z0-9_-]+)'
)

# =====================================================
# SysML einlesen
# =====================================================

def parse_sysml_files(directory):

    requirements = {}

    for root, _, files in os.walk(directory):

        for file in files:

            if not file.endswith(".sysml"):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:

                content = f.read()

            for m in re.finditer(r"\brequirement\b", content):

                brace_start = content.find("{", m.end())

                if brace_start == -1:
                    continue

                depth = 0
                i = brace_start
                block = None

                while i < len(content):

                    if content[i] == "{":
                        depth += 1

                    elif content[i] == "}":
                        depth -= 1

                        if depth == 0:
                            block = content[brace_start + 1:i]
                            break

                    i += 1

                if block is None:
                    continue

                id_match = SYSML_ID_PATTERN.search(block)

                if not id_match:
                    continue

                req_status_match = SYSML_REQ_STATUS_PATTERN.search(block)
                impl_status_match = SYSML_IMPL_STATUS_PATTERN.search(block)
                derived_match = SYSML_DERIVED_PATTERN.search(block)
                doc_match = SYSML_DOC_PATTERN.search(block)

                req_id = id_match.group(1)

                requirements[req_id] = {

                    "requirement_status":
                        req_status_match.group(1)
                        if req_status_match else "Unknown",

                    "implementation_status":
                        impl_status_match.group(1)
                        if impl_status_match else "Unknown",

                    "derived":
                        derived_match.group(1)
                        if derived_match else "-",

                    "description":
                        " ".join(doc_match.group(1).split())
                        if doc_match else "",

                    "file":
                        os.path.relpath(path),

                    "implemented":
                        False,

                    "implemented_in":
                        []
                }

    return requirements

# =====================================================
# C-Code prüfen
# =====================================================

def check_c_implementations(directory, requirements):

    for root, _, files in os.walk(directory):

        for file in files:

            if not file.endswith((".c", ".h")):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:

                for line_num, line in enumerate(f, 1):

                    matches = C_SATISFIES_PATTERN.findall(line)

                    for req_id in matches:

                        if req_id in requirements:

                            requirements[req_id]["implemented"] = True

                            requirements[req_id]["implemented_in"].append(
                                f"{os.path.relpath(path)} : Line {line_num}"
                            )

                        else:

                            print(
                                f"⚠ Warnung: Requirement '{req_id}' "
                                f"nicht in SysML gefunden "
                                f"({file}: Zeile {line_num})"
                            )

# =====================================================
# Konsolenausgabe
# =====================================================

def generate_report(requirements):

    print("\n")
    print("=" * 120)
    print(
        f"{'Requirement':<28}"
        f"{'Req.Status':<15}"
        f"{'Impl.Status':<18}"
        f"{'Code':<10}"
        f"{'Lernziel'}"
    )
    print("=" * 120)

    missing = 0

    for req_id, data in sorted(requirements.items()):

        code = "Ja" if data["implemented"] else "Nein"

        print(
            f"{req_id:<28}"
            f"{data['requirement_status']:<15}"
            f"{data['implementation_status']:<18}"
            f"{code:<10}"
            f"{data['derived']}"
        )

        if (
            data["requirement_status"] == "Approved"
            and not data["implemented"]
        ):
            missing += 1

    print("=" * 120)

    return missing

# =====================================================
# Markdown Report
# =====================================================

def generate_markdown_report(
        requirements,
        output_file="requirements_report.md"
):

    total = len(requirements)

    implemented = sum(
        1
        for r in requirements.values()
        if r["implemented"]
    )

    coverage = (
        implemented / total * 100
        if total > 0 else 0
    )

    with open(output_file, "w", encoding="utf-8") as md:

        md.write("# Traceability Report\n\n")

        md.write(f"**Gesamt Anforderungen:** {total}\n\n")
        md.write(f"**Implementiert:** {implemented}\n\n")
        md.write(f"**Abdeckung:** {coverage:.1f}%\n\n")

        md.write(
            "| Requirement | Req.Status | Impl.Status | Lernziel | "
            "Code | Datei |\n"
        )

        md.write(
            "|--------------|------------|-------------|----------|------|-------|\n"
        )

        for req_id, data in sorted(requirements.items()):

            code = "Ja" if data["implemented"] else "Nein"

            md.write(
                f"| {req_id} | "
                f"{data['requirement_status']} | "
                f"{data['implementation_status']} | "
                f"{data['derived']} | "
                f"{code} | "
                f"{data['file']} |\n"
            )

    print(f"\n📄 Report erstellt: {output_file}")

# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    

    sysml_dir = "./model"
    c_dir = "./core"
    print("SysML:", os.path.abspath(sysml_dir))
    print("Code :", os.path.abspath(c_dir))

    print("🔍 Starte Traceability Check...\n")

    requirements = parse_sysml_files(sysml_dir)
    print("Gefundene Requirements:", len(requirements))

    check_c_implementations(c_dir, requirements)

    missing = generate_report(requirements)

    generate_markdown_report(requirements)

    if missing > 0:

        print(f"\n❌ {missing} Anforderungen sind noch nicht implementiert.")
        sys.exit(1)

    else:

        print("\n✅ Alle Anforderungen wurden erfolgreich implementiert.")
        sys.exit(0)