from .git_reader import (
    get_branch,
    get_commit_count,
    get_commit_history,
    get_last_commit,
    get_diff,
    get_status
)


def build_git_summary():

    summary = {

        "branch": get_branch(),

        "commit_count": get_commit_count(),

        "status": get_status(),

        "history": get_commit_history(),

        "last_commit": get_last_commit(),

        "diff": get_diff()

    }

    return summary


def format_git_summary():

    data = build_git_summary()

    return f"""
==================================================
Git Repository
==================================================

Branch:
{data["branch"]}

--------------------------------------------------

Anzahl Commits:

{data["commit_count"]}

--------------------------------------------------

Repository Status:

{data["status"]}

--------------------------------------------------

Commit Historie:

{data["history"]}

--------------------------------------------------

Letzter Commit:

{data["last_commit"]}

--------------------------------------------------

Aktuelle Änderungen:

{data["diff"]}

"""