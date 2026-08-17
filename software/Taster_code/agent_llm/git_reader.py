import subprocess


def run_git_command(command):
    """
    Führt einen Git-Befehl aus und gibt dessen Ausgabe zurück.
    """

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False
        )

        return result.stdout.strip()

    except Exception as e:
        return f"Git-Fehler: {e}"


# --------------------------------------------------
# Aktueller Branch
# --------------------------------------------------

def get_branch():

    return run_git_command(
        ["git", "branch", "--show-current"]
    )


# --------------------------------------------------
# Letzte Commits
# --------------------------------------------------

def get_commit_history(number=10):

    return run_git_command([
        "git",
        "log",
        f"-{number}",
        "--pretty=format:%h | %an | %ad | %s",
        "--date=short"
    ])


# --------------------------------------------------
# Letzter Commit
# --------------------------------------------------

def get_last_commit():

    return run_git_command([
        "git",
        "show",
        "--stat",
        "--oneline",
        "-1"
    ])


# --------------------------------------------------
# Aktuelle Änderungen
# --------------------------------------------------

def get_diff():

    return run_git_command([
        "git",
        "diff"
    ])


# --------------------------------------------------
# Repository Status
# --------------------------------------------------

def get_status():

    return run_git_command([
        "git",
        "status",
        "--short"
    ])


# --------------------------------------------------
# Anzahl Commits
# --------------------------------------------------

def get_commit_count():

    return run_git_command([
        "git",
        "rev-list",
        "--count",
        "HEAD"
    ])


# --------------------------------------------------
# Git-Informationen für den KI-Agenten
# --------------------------------------------------

def load_git_information():

    return f"""
==================================================
Aktueller Branch
==================================================

{get_branch()}

==================================================
Repository Status
==================================================

{get_status()}

==================================================
Anzahl der Commits
==================================================

{get_commit_count()}

==================================================
Commit-Historie
==================================================

{get_commit_history()}

==================================================
Letzter Commit
==================================================

{get_last_commit()}

==================================================
Aktuelle Änderungen (Diff)
==================================================

{get_diff()}
"""