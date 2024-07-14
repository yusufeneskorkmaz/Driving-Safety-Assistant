import os
from pathlib import Path

class Config:
    def __init__(self):
        self.ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.parent
        self.SRC_DIR = self.ROOT_DIR / "src"
        self.MODELS_DIR = self.ROOT_DIR / "models"
        self.DATA_DIR = self.ROOT_DIR / "data"
        self.LOGS_DIR = self.ROOT_DIR / "logs"

        # Eye detector configuration
        self.EYE_DETECTOR_MODEL = self.MODELS_DIR / "shape_predictor_68_face_landmarks.dat"
        self.EYE_AR_THRESH = 0.3
        self.EYE_AR_CONSEC_FRAMES = 48

        # Phone detector configuration
        self.PHONE_DETECTOR_MODEL = self.MODELS_DIR / "yolov8l.pt"
        self.PHONE_DETECTION_CONFIDENCE = 0.5

        # Video configuration
        self.VIDEO_SOURCE = 0  # 0 for webcam, or provide a file path for video file
        self.FRAME_WIDTH = 640
        self.FRAME_HEIGHT = 480
        self.FPS = 30

        # Dashboard configuration
        self.DASHBOARD_TITLE = "Driving Safety Assistant"
        self.DASHBOARD_REFRESH_RATE = 100  # milliseconds

    def get_eye_detector_config(self):
        return {
            "predictor_path": str(self.EYE_DETECTOR_MODEL),
            "eye_ar_thresh": self.EYE_AR_THRESH,
            "eye_ar_consec_frames": self.EYE_AR_CONSEC_FRAMES
        }

    def get_phone_detector_config(self):
        return {
            "model_path": str(self.PHONE_DETECTOR_MODEL),
            "confidence": self.PHONE_DETECTION_CONFIDENCE
        }

    def get_video_config(self):
        return {
            "source": self.VIDEO_SOURCE,
            "width": self.FRAME_WIDTH,
            "height": self.FRAME_HEIGHT,
            "fps": self.FPS
        }

    def get_dashboard_config(self):
        return {
            "title": self.DASHBOARD_TITLE,
            "refresh_rate": self.DASHBOARD_REFRESH_RATE
        }

config = Config()