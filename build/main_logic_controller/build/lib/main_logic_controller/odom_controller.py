# kangaroo_test.py
# Step 1 — Test script to query Kangaroo encoder positions

import serial
import time

# Step 1 — Open serial port to Kangaroo
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
time.sleep(2)  # Wait for serial port to initialize
print("Connected to Kangaroo on /dev/ttyAMA0")

# Function to send command and read response
def send_command(ser, command):
    # Send command (with carriage return)
    ser.write(command.encode('utf-8') + b'\r')
    time.sleep(0.1)  # Give Kangaroo time to respond

    # Read any available response
    response = ser.read(ser.in_waiting).decode('utf-8').strip()
    return response

# Step 2 — Main loop: query position repeatedly
while True:
    try:
        # Query DRIVE axis position
        response_drive = send_command(ser, "D,getp")
        print(f"[Kangaroo] Drive Pos: {response_drive}")

        # Query TURN axis position
        response_turn = send_command(ser, "T,getp")
        print(f"[Kangaroo] Turn Pos: {response_turn}")

        # Wait a bit before next query
        time.sleep(0.1)  # 10 Hz

    except KeyboardInterrupt:
        # Exit gracefully if user presses Ctrl+C
        print("Exiting...")
        break

# Close serial port when done
ser.close()
print("Serial port closed.")
