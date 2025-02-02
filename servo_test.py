import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)  # Allow Arduino to reset
    ser.reset_input_buffer()

    # Send data once
    ser.write(b"box1\n")
    time.sleep(1)  # Allow Arduino to process

    ser.close()  # Close serial port
