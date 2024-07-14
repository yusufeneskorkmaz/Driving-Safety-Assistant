import cv2
from src.DrivingSafetyAssistant.components.eye_detector import EyeDetector
from src.DrivingSafetyAssistant.components.phone_detector import PhoneDetector

class SafetyAnalysisPipeline:
    def __init__(self):
        self.eye_detector = EyeDetector()
        self.phone_detector = PhoneDetector()

    def analyze_frame(self, frame):
        tiredness_detected, tiredness_frame = self.eye_detector.detect_tiredness(frame)
        phone_detected, phone_frame = self.phone_detector.detect_phone_usage(tiredness_frame)

        if tiredness_detected:
            cv2.putText(phone_frame, "TIREDNESS DETECTED!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        return tiredness_detected, phone_detected, phone_frame