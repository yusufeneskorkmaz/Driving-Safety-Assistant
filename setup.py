from setuptools import setup, find_packages

setup(
    name="DrivingSafetyAssistant",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "ultralytics",
        "opencv-python",
        "numpy",
        "cvzone",
        "dlib",
        "scipy",
        "streamlit",
        "mediapipe",
    ],
)