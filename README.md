# Smart Irrigation System Using Machine Learning

An automated irrigation prototype using Python, a Decision Tree machine-learning model and Arduino Uno to monitor soil moisture and control a water pump.

## Project Overview

This project automatically controls a water pump based on soil moisture conditions.

When the soil is dry, the machine-learning model predicts the condition and switches the pump ON. When the soil is wet, the pump switches OFF.

The system was successfully tested with automatic pump control.

## Technologies Used

- Python
- Scikit-learn
- Decision Tree Classifier
- Pandas
- Joblib
- Arduino Uno
- C++
- Serial Communication

## Hardware Components

- Arduino Uno
- Soil moisture sensor
- Relay module
- Mini water pump
- Power supply
- Connecting wires

## How It Works

1. The soil moisture sensor measures the soil moisture.
2. Arduino sends the sensor reading to Python through serial communication.
3. Python loads the saved Decision Tree model.
4. The model predicts one of four soil conditions:
   - Dry
   - Slightly Wet
   - Moderately Wet
   - Wet
5. If the prediction is Dry, Python sends a command to switch the pump ON.
6. For the other three conditions, Python sends a command to switch the pump OFF.

## Machine Learning Model

The project uses a Scikit-learn Decision Tree Classifier.

- Input feature: `Soil_Moisture`
- Number of output classes: 4
- Splitting criterion: Gini
- Model file: `smart_irrigation_model.pkl`

## Project Structure

```text
Smart-Irrigation-System-ML/
│
├── arduino/
│   └── Smart_Irrigation_Arduino.ino
│
├── python/
│   ├── smart_irrigation.py
│   ├── arduino_connection.py
│   └── smart_irrigation_model.pkl
│
├── dataset/
│   ├── smart_irrigation_moisture_dataset_updated.csv
│   └── smart_irrigation_moisture_dataset.csv
│
├── images/
│   └── Prototype photographs
│
└── README.md
```

## Testing and Results

The complete prototype was tested successfully.

- Dry soil: Water pump automatically switched ON.
- Wet soil: Water pump automatically switched OFF.

## My Contribution

- Assembled the Arduino-based hardware prototype.
- Connected the soil moisture sensor, relay and water pump.
- Implemented Python and Arduino serial communication.
- Integrated the saved machine-learning model into the irrigation control system.
- Tested automatic pump operation under dry and wet soil conditions.

## Future Improvements

- Monitor soil moisture remotely.
- Add a mobile application.
- Integrate IoT-based monitoring.
- Improve irrigation decisions using additional environmental data.

## Note

The updated CSV dataset is the main dataset used in the project. The original model-training script and model accuracy measurements are not currently included in this repository.

