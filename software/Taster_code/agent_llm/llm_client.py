# Importiert den offiziellen OpenAI-Python-Client.
from openai import OpenAI
from .config import API_KEY, MODEL, TEMPERATURE, MAX_TOKENS


# Erstellt ein Client-Objekt für API-Anfragen.
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def ask_llm(prompt):

    response = client.chat.completions.create(
        model=MODEL,

 # Steuert die Zufälligkeit der Antwort.       
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        messages=[
            {
                # Verhalten
                "role": "system",
                "content": "Du bist ein Tutor für Embedded Systems."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print("\n==============================")
    print("MODELL:", MODEL)

    # Gibt den Grund aus, weshalb die Antwort beendet wurde.
    print("Finish:", response.choices[0].finish_reason)
    print("==============================")

    if not response.choices:
        print("Keine Antwort erhalten!")
        return None

    answer = response.choices[0].message.content

    print("\nAntwort:")


    return answer
    