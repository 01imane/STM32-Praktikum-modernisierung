import serial
import re
from agent.ai_agent import analyze

# ----------------------------------
# UART
# ----------------------------------

ser = serial.Serial("COM7", 115200, timeout=2)

print("Starte Lauflicht-Test...\n")

# Erwartete Reihenfolge
expected = [
    "LED1",
    "LED2",
    "LED3",
    "LED4",
    "LED5",
    "LED6",
    "LED7",
    "LED8"
]

received = []
timestamps = []

print("Empfange UART-Daten...\n")

while len(received) < 8:

    line = ser.readline().decode(errors="ignore").strip()

    if not line:
        continue

    print(line)

    match = re.search(r"(LED\d+) ON (\d+)", line)

    if match:

        received.append(match.group(1))
        timestamps.append(int(match.group(2)))

# ----------------------------------
# Reihenfolge prüfen
# ----------------------------------

print("\n==============================")
print("Prüfe LED-Reihenfolge")
print("==============================")

sequence_ok = True

for i in range(len(expected)):

    if received[i] != expected[i]:

        sequence_ok = False

        print(f"❌ Erwartet : {expected[i]}")
        print(f"   Erhalten : {received[i]}")

        analyze("LED_SEQUENCE_ERROR")
        break

if sequence_ok:
    print("✅ Reihenfolge korrekt")

# ----------------------------------
# Timing prüfen
# ----------------------------------

print("\n==============================")
print("Prüfe Timing")
print("==============================")

timing_ok = True

print()

for i in range(len(timestamps)-1):

    dt = timestamps[i+1] - timestamps[i]

    print(f"{i+1}. {dt} ms")

    if 950 <= dt <= 1050:

        print("   ✅ OK")

    else:

        print("   ❌ Fehler")

        timing_ok = False

if not timing_ok:
    analyze("LED_TIMING_ERROR")

# ----------------------------------
# Ergebnis
# ----------------------------------

print("\n===================================")

if sequence_ok and timing_ok:

    analyze("TEST_OK")

else:

    print("\n==============================")
    print("❌ TEST NICHT BESTANDEN")
    print("==============================")