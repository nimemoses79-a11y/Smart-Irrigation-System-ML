
import serial
import time
import pickle
import os

# Arduino connection
PORT = "COM7"
BAUD_RATE = 9600

# Load the trained ML model
folder = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(folder, "smart_irrigation_model.pkl")

with open(model_path, "rb") as file:
    model = pickle.load(file)

print("Smart Irrigation ML System")
print("Loading model...")

try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=2)
    time.sleep(2)
    print("Arduino connected on", PORT)

    while True:
        line = arduino.readline().decode(
            "utf-8", errors="ignore"
        ).strip()

        if line:
            print("Arduino:", line)

            # Find a numeric soil moisture reading
            try:
                reading = int(line)

                prediction = model.predict([[reading]])[0]
                print("ML prediction:", prediction)

            except ValueError:
                pass

except serial.SerialException as error:
    print("Arduino connection error:", error)

except KeyboardInterrupt:
    print("\nStopping Smart Irrigation.")

finally:
    if "arduino" in locals() and arduino.is_open:
        arduino.close()