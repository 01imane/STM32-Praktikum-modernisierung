from openai import OpenAI
from config import *

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(prompt):

    response = client.chat.completions.create(

        model=MODEL,

        temperature=TEMPERATURE,

        max_tokens=MAX_TOKENS,

        messages=[

            {
                "role":"system",
                "content":
                "Du bist ein Tutor für Embedded Systems."
            },

            {
                "role":"user",
                "content":prompt
            }

        ]

    )

    return response.choices[0].message.content