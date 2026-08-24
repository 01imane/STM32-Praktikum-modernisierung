import serial
import sys
import os
import time
import inspect


print(">>> Neue professor_agent.py geladen <<<")
# AI-Agent importieren
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#war für den ersten Einsatz mit .py agent
# from agent.ai_agent import analyze
from agent_llm.student_agent import student_agent

from agent_llm.professor_agent import professor_agent
# -----------------------------
# Einstellungen
# -----------------------------
PORT = "COM7"
BAUDRATE = 115200

EXPECTED_TIME = 1000      # 1000 ms
TOLERANCE = 20            # ±20 ms

# -----------------------------
# Test auswählen
# -----------------------------
print("Welchen Test möchten Sie durchführen?")
print("1 - LED1 blinkt")
print("2 - LED2 blinkt")
print("3 - Alle LEDs blinken")
print("4 - Alle LEDs dauerhaft an")

choice = input("Auswahl: ")

tests = {
    "1": ("LED1 TOGGLE", True),
    "2": ("LED2 TOGGLE", True),
    "3": ("ALL TOGGLE", True),
    "4": ("ALL ON", False)
}

if choice not in tests:
    print("Ungültige Auswahl.")
    sys.exit()

expected_message, blink_test = tests[choice]
requirements = {
    "LED1 TOGGLE": "TASTER_1_FUNCTION",
    "LED2 TOGGLE": "TASTER_2_FUNCTION",
    "ALL TOGGLE": "TASTER_3_FUNCTION",
    "ALL ON": "TASTER_4_FUNCTION"
}

requirement = requirements[expected_message]

# -----------------------------
# UART öffnen
# -----------------------------
try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
except Exception as e:

    print("❌ COM-Port konnte nicht geöffnet werden.")

    student_agent(
        test_name="UART",
        expected=0,
        average=0,
        tolerance=0,
        requirement="UART_CONNECTION",
        uart_output=f"""
        UART konnte nicht geöffnet werden.

        Fehlermeldung:

        {e}
        """
    )

    sys.exit()

print("\nStarte Test...\n")

timestamps = []


start = time.time()
TIMEOUT = 20      # Sekunden

# -----------------------------
# UART lesen
# -----------------------------
while True:

    # Timeout
    if time.time() - start > TIMEOUT:
        print("\n❌ Timeout.")

        student_agent(
          test_name=expected_message,
          expected=EXPECTED_TIME,
          average=0,
          tolerance=TOLERANCE,
          requirement=requirement,
          uart_output= f"""
            Timeout nach {TIMEOUT} Sekunden.

            Es wurden keine UART-Daten empfangen.
        """
)
        ser.close()
        sys.exit()

    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    print(line)

    # -----------------------------
    # Falscher Test?
    # -----------------------------
  
    # -----------------------------
    # Richtige Nachricht
    # -----------------------------
    if line.startswith(expected_message):

      

        if blink_test:

            parts = line.split()

            try:
                timestamp = int(parts[-1])
                timestamps.append(timestamp)
            except:
                pass

        else:

            print("\n==============================")
            print("✅ TEST BESTANDEN")
            print("==============================")
            student_agent(
                test_name=expected_message,
                expected=0,
                average=0,
                tolerance=0,
                requirement=requirement,
                uart_output="ALL ON ."
    )

            ser.close()
            sys.exit()

        if len(timestamps) >= 10:
            break

ser.close()

# -----------------------------
# Blinktest
# -----------------------------
if len(timestamps) < 2:

    print("\n❌ Zu wenige Blinkereignisse erkannt.")
    student_agent(
            test_name=expected_message,
            expected=EXPECTED_TIME,
            average=0,
            tolerance=TOLERANCE,
            requirement=requirement,
            uart_output="Keine Blinkereignisse erkannt."
)
    sys.exit()

print("\nGemessene Blinkzeiten:\n")

passed = True
diffs = []

for i in range(len(timestamps)-1):

    dt = timestamps[i+1] - timestamps[i]
    diffs.append(dt)

    print(f"{i+1}. {dt} ms")

    

average = sum(diffs) / len(diffs)

print("\n--------------------------------")
print(f"Durchschnitt: {average:.1f} ms")
print("--------------------------------")


# Ergebnis
# -----------------------------


student_agent(

    test_name=expected_message,

    expected=EXPECTED_TIME,

    average=average,
    
    tolerance=TOLERANCE,

    requirement=requirement,

    uart_output= f"""
    Messwerte:

    {diffs}

    Durchschnitt:

    {average:.1f} ms

    Sollwert:

    {EXPECTED_TIME} ms

    Toleranz:

    ±{TOLERANCE} ms
    """

   )

professor_agent(
    student="Imane",
    
    test_name=expected_message,

    expected=EXPECTED_TIME,

    measured=average,

    tolerance=TOLERANCE,

    requirement=requirement,

    result=passed,

    uart_output=f"""
Messwerte:

{diffs}

Durchschnitt:

{average:.1f} ms

Sollwert:

{EXPECTED_TIME} ms

Toleranz:

±{TOLERANCE} ms
"""
)
print(inspect.signature(professor_agent))