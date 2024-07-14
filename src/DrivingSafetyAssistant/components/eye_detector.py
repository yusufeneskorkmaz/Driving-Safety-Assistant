import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from src.DrivingSafetyAssistant.config.configuration import config


class EyeDetector:
    def __init__(self):
        eye_config = config.get_eye_detector_config()
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(eye_config["predictor_path"])
        self.EYE_AR_THRESH = eye_config["eye_ar_thresh"]
        self.EYE_AR_CONSEC_FRAMES = eye_config["eye_ar_consec_frames"]
        self.COUNTER = 0

    def calculate_ear(self, eye):
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        C = dist.euclidean(eye[0], eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def detect_tiredness(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)

        for face in faces:
            landmarks = self.predictor(gray, face)

            left_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)])
            right_eye = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)])

            leftEAR = self.calculate_ear(left_eye)
            rightEAR = self.calculate_ear(right_eye)

            ear = (leftEAR + rightEAR) / 2.0

            if ear < self.EYE_AR_THRESH:
                self.COUNTER += 1
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    cv2.putText(frame, "TIREDNESS DETECTED!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    return True, frame
            else:
                self.COUNTER = 0

        return False, frame