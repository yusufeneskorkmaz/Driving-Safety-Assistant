# Driving Safety Assistant

This project is a driving safety assistant that detects driver tiredness and phone usage while driving.

## Features

- Eye tiredness detection
- Phone usage detection
- Real-time video analysis
- Streamlit dashboard for easy visualization

## Screenshot from Streamlit App

[![Screenshot-2024-07-15-000037.png](https://i.postimg.cc/KvMVmSFc/Screenshot-2024-07-15-000037.png)](https://postimg.cc/sv3KJLvb)

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Download the required model files:
   - YOLOv8 model: Download `yolov8l.pt` and place it in the `models` directory
   - Dlib shape predictor: Download `shape_predictor_68_face_landmarks.dat` and place it in the `models` directory

## Usage
Set PYTHONPATH environment variable

```
$env:PYTHONPATH = "$env:PYTHONPATH;
```
Run the Streamlit app:

```
streamlit run main.py
```

This will start the dashboard, which will use your computer's webcam to analyze driving safety in real-time.

## Project Structure

- `src/DrivingSafetyAssistant/`: Main package directory
  - `components/`: Contains the eye detector and phone detector modules
  - `pipeline/`: Contains the safety analysis pipeline
  - `dashboard/`: Contains the Streamlit app
- `main.py`: Entry point for the Streamlit app
- `setup.py`: Setup file for the package
- `requirements.txt`: List of required packages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).