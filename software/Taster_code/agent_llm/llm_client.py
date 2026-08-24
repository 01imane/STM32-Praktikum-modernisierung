from openai import OpenAI
from .config import API_KEY, MODEL, TEMPERATURE, MAX_TOKENS



client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def ask_llm(prompt):

    response = client.chat.completions.create(
        model=MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        messages=[
            {
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
    print("Finish:", response.choices[0].finish_reason)
    print("==============================")

    if not response.choices:
        print("Keine Antwort erhalten!")
        return None

    answer = response.choices[0].message.content

    print("\nAntwort:")


    return answer
    