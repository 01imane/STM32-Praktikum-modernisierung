from agent.knowledge_base import ERROR_DB

def analyze(error_code):

    print("\n==============================")
    print("🤖 AI AGENT ANALYSE")
    print("==============================")

    if error_code in ERROR_DB:
        e = ERROR_DB[error_code]

        print("❌ Fehler erkannt")
        print(f"📘 Ursache: {e['cause']}")
        print(f"📚 Vorlesung: {e['lecture']}")
        print(f"➡️ Thema: {e['topic']}")
        print(f"🛠 Tipp: {e['hint']}")
    else:
        print("⚠️ Unbekannter Fehler")