from dotenv import load_dotenv
import os

load_dotenv()
# OpenAI API Key
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Modell
MODEL = "openrouter/free"


#  0.2 ist ein niedriger Wert und eignet sich für
# sachliche technische Rückmeldungen.
TEMPERATURE = 0.2

# maximale Antwort
MAX_TOKENS = 3500