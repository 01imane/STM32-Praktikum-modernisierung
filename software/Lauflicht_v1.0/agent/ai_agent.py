from agent.knowledge_base import ERROR_DB


def analyze(error_code):

    print("\n==============================")
    print("🤖 AI AGENT ANALYSE")
    print("==============================")

    if error_code == "TEST_OK":

        print("✅ TEST BESTANDEN")
        print("Alle Anforderungen wurden erfolgreich erfüllt.")
        return

    if error_code in ERROR_DB:

        e = ERROR_DB[error_code]

        print("❌ Fehler erkannt")
        print(f"📘 Ursache   : {e['cause']}")
        print(f"📚 Vorlesung : {e['lecture']}")
        print(f"➡️ Thema     : {e['topic']}")
        print(f"🛠 Hinweis   : {e['hint']}")

    else:

        print("⚠️ Unbekannter Fehler")