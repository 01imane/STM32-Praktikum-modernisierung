from dotenv import load_dotenv
import os

load_dotenv()
# OpenAI API Key
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Modell
MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"
# Temperatur
TEMPERATURE = 0.2

# maximale Antwort
MAX_TOKENS = 1200