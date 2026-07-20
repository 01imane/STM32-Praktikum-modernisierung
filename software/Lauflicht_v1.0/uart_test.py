import serial

ser = serial.Serial("COM7", 115200, timeout=1)

print("Warte auf UART-Daten...\n")

while True:
    line = ser.readline().decode(errors="ignore").strip()

    if line:
        print(line)