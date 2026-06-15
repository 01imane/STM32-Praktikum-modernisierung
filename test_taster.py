import serial
import time

ser = serial.Serial('COM7', 115200)  # STM32 an COM7!

print("Starte Test...")

timestamps = []

start = time.time()

while time.time() - start < 10:
    line = ser.readline().decode(errors='ignore').strip()
    print(line)

    if "T1 LED1 ON" in line:
        timestamps.append(time.time())

# Frequenz prüfen (nur T1 Beispiel)
if len(timestamps) > 1:
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]

    print("\nT1 Frequenz:")
    for d in diffs:
        print(f"{d:.2f} s")

    for d in diffs:
        if 0.40 < d < 0.55:
            print("✅ OK")
        else:
            print("❌ Fehler")