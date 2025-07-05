
# ⚡ Energy Waste Detection System

A Streamlit-based web application that uses **YOLOv8 object detection** to analyze uploaded video footage and detect **energy wastage**—specifically when **lights are on but no humans are present**. This project aims to support energy conservation by monitoring occupancy and appliance usage patterns.

---

## 🚀 Features

* 🔍 Detects **lamp/light**, **human**, and other common objects in videos using YOLOv8.
* ⚠️ Flags **"Energy Wastage Detected"** when devices (e.g., lights, lamps) are on with **no human presence**.
* 📋 Displays all detected objects in the video.
* ✅ Lightweight and easy to run via **Streamlit web app**.
* 🎥 Upload any `.mp4`, `.avi`, or `.mov` video for analysis.

---

## 🧠 How It Works

1. YOLOv8 is used to detect objects frame-by-frame.
2. Checks if **energy-related devices** (e.g., lamp/light/tv/monitor) are detected.
3. Verifies whether **person** is present.
4. Triggers alert if **energy devices are ON but no human is detected**.

---

## 📁 Directory Structure

```
.
├── clone.py               # Main Streamlit application
├── README.md              # Project documentation
└── requirements.txt       # Dependencies
```

---

## 🛠️ Installation & Running

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/energy-waste-detection.git
cd energy-waste-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run clone.py
```

---

## 📦 Requirements

Include these in `requirements.txt`:

```txt
streamlit
ultralytics
opencv-python
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📽️ Sample Video Sources

You can test the app using any video, or download from:

* [https://www.pexels.com/videos/](https://www.pexels.com/videos/)
* [https://pixabay.com/videos/](https://pixabay.com/videos/)

---

## 🧪 Example Output

* ✅ Detected Objects: person, lamp, tv
* ⚠️ Energy Wastage Detected: Light is on but no person is present.

---

## 🧠 Future Improvements

* Train a **custom YOLO model** to better detect specific appliances (e.g., fan, tube light).
* Add **real-time webcam** support.
* Export results as **PDF/CSV reports**.
* Integrate with **Raspberry Pi or edge device** for home automation.

---

## 💡 Use Cases

* Smart Homes
* Office Energy Monitoring
* School/College Campus Automation
* Public Space Surveillance

---

## 📜 License

MIT License. Feel free to fork, improve, and use it in your own energy-saving initiatives.

