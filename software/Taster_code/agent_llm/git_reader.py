import subprocess


def git_log():

    try:

        result = subprocess.run(

            ["git", "log", "--oneline", "-5"],

            capture_output=True,

            text=True

        )

        return result.stdout

    except Exception as e:

        return str(e)


def git_status():

    try:

        result = subprocess.run(

            ["git", "status"],

            capture_output=True,

            text=True

        )

        return result.stdout

    except Exception as e:

        return str(e)


def git_diff():

    try:

        result = subprocess.run(

            ["git", "diff"],

            capture_output=True,

            text=True

        )

        return result.stdout

    except Exception as e:

        return str(e)