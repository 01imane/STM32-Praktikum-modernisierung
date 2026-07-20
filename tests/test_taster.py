import serial
import time
import sys
import os

# AI-Agent einbinden
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.ai_agent import analyze

# -----------------------------
# Einstellungen
# -----------------------------
PORT = "COM7"
BAUDRATE = 115200

EXPECTED_TIME = 1.0      # Sollwert: 1 Sekunde
TOLERANCE = 0.05         # ±50 ms

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
    print("Ungültige Auswahl!")
    sys.exit()

expected_message, blink_test = tests[choice]

# -----------------------------
# UART öffnen
# -----------------------------
try:
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
except serial.SerialException:
    print("❌ COM-Port konnte nicht geöffnet werden.")
    analyze("UART_CONNECTION_ERROR")
    sys.exit()

print("\nStarte Test...\n")

timestamps = []
message_received = False

start = time.time()

while time.time() - start < 10:

    line = ser.readline().decode(errors="ignore").strip()

    if line:

        print(line)

        if line == expected_message:

            message_received = True

            if blink_test:
                timestamps.append(time.time())

ser.close()

# -----------------------------
# Test 4 (kein Blinken)
# -----------------------------
if not blink_test:

    if message_received:
        print("\n✅ PASS")
        print("Alle LEDs wurden eingeschaltet.")
    else:
        print("\n❌ FAIL")
        analyze("ALL_ON_NOT_DETECTED")

    sys.exit()

# -----------------------------
# Blinktest
# -----------------------------
if len(timestamps) < 2:

    print("\n❌ FAIL")
    print("Zu wenige Blinkereignisse erkannt.")
    analyze("NO_BLINK_DETECTED")
    sys.exit()

passed = True

print("\nGemessene Blinkzeiten:")

for i in range(len(timestamps)-1):

    dt = timestamps[i+1] - timestamps[i]

    print(f"{i+1}. {dt:.3f} s")

    if abs(dt - EXPECTED_TIME) <= TOLERANCE:

        print("   ✅ OK")

    elif dt < EXPECTED_TIME:

        print("   ❌ Zu schnell")
        analyze("TIMER_TOO_FAST")
        passed = False

    else:

        print("   ❌ Zu langsam")
        analyze("TIMER_TOO_SLOW")
        passed = False

print()

if passed:

    print("===================================")
    print("✅ TEST BESTANDEN")
    print("Blinkzeit korrekt (1 Sekunde).")
    print("===================================")

else:

    print("===================================")
    print("❌ TEST NICHT BESTANDEN")
    print("===================================")