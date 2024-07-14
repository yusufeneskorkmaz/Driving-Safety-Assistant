import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "DrivingSafetyAssistant"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/eye_detector.py",
    f"src/{project_name}/components/phone_detector.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/safety_analysis_pipeline.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/dashboard/__init__.py",
    f"src/{project_name}/dashboard/app.py",
    "main.py",
    "setup.py",
    ".gitignore",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

# Create requirements.txt
requirements_content = """
ultralytics
opencv-python
numpy
cvzone
dlib
scipy
streamlit
mediapipe
-e .
"""

with open("requirements.txt", "w") as f:
    f.write(requirements_content.strip())
logging.info("Created requirements.txt")

# Create directories
for dir in ["logs", "data", "models"]:
    os.makedirs(dir, exist_ok=True)
    logging.info(f"Created '{dir}' directory")

print("Project structure created successfully!")