import streamlit as st
import tempfile
import os
import cv2
import atexit
from ultralytics import YOLO

# Load YOLO model (you can replace this with a custom trained model if needed)
model = YOLO("yolov8n.pt")  # You can change this to "yolov8s.pt" or custom model path

# Define the labels we're interested in
energy_objects = {"lamp", "light", "bulb", "tv", "monitor"}  # Extend as needed
human_label = "person"

st.title("⚡ Energy Waste Detection System (YOLO + Streamlit)")

uploaded_file = st.file_uploader("📹 Upload a video file", type=["mp4", "avi", "mov"])

def process_video(video_file):
    # Save to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(video_file.read())
        temp_path = temp_file.name

    atexit.register(lambda: os.path.exists(temp_path) and os.remove(temp_path))  # Clean up later

    cap = cv2.VideoCapture(temp_path)
    frame_count = 0
    energy_detected = False
    human_detected = False
    all_detected_objects = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame_count > 100:  # Limit for performance
            break

        results = model.predict(source=frame, conf=0.4, verbose=False)
        if results:
            result = results[0]
            boxes = result.boxes
            for box in boxes:
                cls_id = int(box.cls)
                label = model.names[cls_id].lower()
                all_detected_objects.add(label)

                if label in energy_objects:
                    energy_detected = True
                if human_label in label:
                    human_detected = True

        frame_count += 1

    cap.release()
    return energy_detected, human_detected, all_detected_objects

# Main logic
if uploaded_file is not None:
    st.info("⏳ Processing video...")
    energy, human, detected_objects = process_video(uploaded_file)

    st.success("✅ Processing complete!")

    st.write("🔍 **Detected objects in video:**")
    st.write(", ".join(sorted(detected_objects)) if detected_objects else "None")

    if energy and not human:
        st.error("⚠️ Energy Wastage Detected: Light/Appliance on but no human present!")
    elif energy and human:
        st.info("✅ Energy usage is appropriate: Human present with devices on.")
    elif not energy:
        st.success("💡 No energy-consuming objects detected.")
