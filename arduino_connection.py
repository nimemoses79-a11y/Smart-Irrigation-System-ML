
import time
import joblib
import serial
import pandas as pd

PORT = "COM7"
BAUD_RATE = 9600
MODEL_FILE = "smart_irrigation_model.pkl"

# Load your already-trained ML model
model = joblib.load(MODEL_FILE)

# Detect the feature name used when training the model
if hasattr(model, "feature_names_in_"):
    feature_name = model.feature_names_in_[0]
else:
    feature_name = "Soil_Moisture"

print("ML model loaded successfully.")
print("Input feature:", feature_name)
print("Model classes:", model.classes_)

arduino = None

try:
    # Connect to Arduino
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=3)
    time.sleep(2)  # Allow Arduino to restart

    # Ensure pump is OFF at startup
    arduino.write(b"0")
    arduino.flush()

    print("\nConnected to Arduino on", PORT)
    print("Automatic irrigation started.")
    print("Press Ctrl+C to stop.\n")

    while True:
        line = arduino.readline().decode(
            "utf-8", errors="ignore"
        ).strip()

        if not line.startswith("MOISTURE,"):
            continue

        try:
            moisture = int(line.split(",", 1)[1])
        except ValueError:
            continue

        # Predict soil condition using the trained model
        sample = pd.DataFrame(
            [[moisture]], columns=[feature_name]
        )
        prediction = str(model.predict(sample)[0]).strip()
        condition = prediction.lower()

        # Dry soil needs irrigation.
        # All other trained classes turn the pump OFF.
        if condition == "dry":
            command = b"1"
            pump_status = "ON"
        elif condition in (
            "slightly wet",
            "moderately wet",
            "wet"
        ):
            command = b"0"
            pump_status = "OFF"
        else:
            # Unknown prediction: fail safe
            command = b"0"
            pump_status = "OFF"
            print("WARNING: Unknown class:", prediction)

        arduino.write(command)
        arduino.flush()

        print(
            f"Moisture: {moisture} | "
            f"ML prediction: {prediction} | "
            f"Pump command: {pump_status}"
        )

except KeyboardInterrupt:
    print("\nStopping irrigation program...")

except Exception as error:
    print("ERROR:", error)

finally:
    if arduino is not None and arduino.is_open:
        try:
            # Tell Arduino to turn the pump OFF
            arduino.write(b"0")
            arduino.flush()
            time.sleep(0.2)
        except Exception:
            pass
        arduino.close()

    print("Serial connection closed.")