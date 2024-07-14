import streamlit as st
import cv2
from src.DrivingSafetyAssistant.pipeline.safety_analysis_pipeline import SafetyAnalysisPipeline
from src.DrivingSafetyAssistant.config.configuration import config

def main():
    dashboard_config = config.get_dashboard_config()
    video_config = config.get_video_config()

    st.title(dashboard_config["title"])

    pipeline = SafetyAnalysisPipeline()

    cap = cv2.VideoCapture(video_config["source"])
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, video_config["width"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, video_config["height"])
    cap.set(cv2.CAP_PROP_FPS, video_config["fps"])

    stframe = st.empty()
    st_tiredness = st.empty()
    st_phone = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        tiredness_detected, phone_detected, analyzed_frame = pipeline.analyze_frame(frame)

        stframe.image(analyzed_frame, channels="BGR")
        st_tiredness.text(f"Tiredness Detected: {tiredness_detected}")
        st_phone.text(f"Phone Usage Detected: {phone_detected}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

if __name__ == "__main__":
    main()