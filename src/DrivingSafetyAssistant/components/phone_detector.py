from ultralytics import YOLO
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from src.DrivingSafetyAssistant.config.configuration import config


class PhoneDetector:
    def __init__(self):
        phone_config = config.get_phone_detector_config()
        self.model = YOLO(phone_config["model_path"])
        self.detector = HandDetector(maxHands=5)
        self.confidence_threshold = phone_config["confidence"]

    def detect_phone_usage(self, frame):
        imgs = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.model(imgs, verbose=False)
        labels = results[0].names

        person_list = []
        phone_list = []

        for i in range(len(results[0].boxes)):
            x1, y1, x2, y2 = results[0].boxes.xyxy[i]
            score = results[0].boxes.conf[i]
            label = results[0].boxes.cls[i]
            x1, y1, x2, y2, score, label = int(x1), int(y1), int(x2), int(y2), float(score), int(label)
            name = labels[label]

            if score < self.confidence_threshold:
                continue
            if name == 'person':
                person_list.append((x1, y1, x2, y2))
            if name == 'cell phone':
                phone_list.append((x1, y1, x2, y2))

        copy = frame.copy()
        hands, copy = self.detector.findHands(copy, flipType=False)

        hand_list = []

        for phone in phone_list:
            (x21, y21, x22, y22) = phone
            region1 = np.array([(x21, y21), (x22, y21), (x22, y22), (x21, y22)])
            region1 = region1.reshape((-1, 1, 2))

            for hand in hands:
                for j in range(21):
                    x, y, z = hand['lmList'][j]
                    inside_region1 = cv2.pointPolygonTest(region1, (x, y), False)
                    if inside_region1 > 0:
                        cx = int(x21 / 2 + x22 / 2)
                        cy = int(y21 / 2 + y22 / 2)
                        hand_list.append((cx, cy))

        phone_detected = False
        for person in person_list:
            control = False
            (x21, y21, x22, y22) = person
            region1 = np.array([(x21, y21), (x22, y21), (x22, y22), (x21, y22)])
            region1 = region1.reshape((-1, 1, 2))

            for hand in hand_list:
                (x, y) = hand
                inside_region1 = cv2.pointPolygonTest(region1, (x, y), False)
                if inside_region1 > 0:
                    control = True

            if control:
                cv2.rectangle(frame, (x21, y21), (x22, y22), (102, 0, 153), 5)
                cv2.putText(frame, 'Phone Detected', (x21, y21 - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
                phone_detected = True

        return phone_detected, frame