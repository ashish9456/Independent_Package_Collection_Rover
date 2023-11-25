import RPi.GPIO as GPIO
import time

# Define GPIO pin numbers
IR_SENSOR_PIN = 27  # Replace with the actual GPIO pin number you are using

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

def detect_red_light():
    try:
        while True:
            if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
                print("Red light detected!")
            else:
                print("No red light detected.")
            
            time.sleep(1)  # Check the sensor every 1 second
    
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO on program exit

if __name__ == "__main__":
    print("Red light sensing program started.")
    detect_red_light()
