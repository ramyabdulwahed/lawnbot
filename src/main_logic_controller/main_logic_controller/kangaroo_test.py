import serial
import time

# Open serial connection
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)

# Clear buffers
ser.reset_input_buffer()
ser.reset_output_buffer()

# Send command to Kangaroo
ser.write(b"1,getp\r")
time.sleep(0.2)

# Read reply
response = ser.read(32)
print("Raw response bytes:", response)
print("As text:", response.decode(errors="replace").strip())
