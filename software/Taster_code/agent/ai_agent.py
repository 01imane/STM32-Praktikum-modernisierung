from agent.knowledge_base import ERROR_DB


def analyze(error_code):

    print("\n==========================================")
    print("🤖 STUDENTENAGENT")
    print("==========================================")

    if error_code not in ERROR_DB:

        print("⚠ Unbekannter Fehler.")
        return

    e = ERROR_DB[error_code]

    print("❌ Test nicht bestanden\n")

    print(f"Requirement : {e['requirement']}")
    print(f"Lernziel    : {e['learning_goal']}")
    print(f"Vorlesung   : {e['lecture']}")

    print("\n------------------------------------------")

    print("Ursache")
    print(f"  {e['cause']}")

    print("\nBetroffener Code")
    print(f"  {e['code']}")

    print("\nEmpfehlung")
    print(f"  {e['hint']}")

    print("\n==========================================")