# Object Tracking & Counting with YOLOv8

## Watch the Video 📺

[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube&logoColor=white&style=for-the-badge)](https://youtu.be/YyidGtx-QmQ)

## Overview
This project demonstrates real-time **Object detection, tracking, and counting** using **YOLOv8**, **Supervision**, and **OpenCV**. The goal is to track Object movement across a defined line in a video and count how many people enter and exit. This approach is useful for applications like **crowd analysis, surveillance, and retail analytics**.

---

<img width="1845" height="811" alt="Image" src="https://github.com/user-attachments/assets/81afde11-d5bf-4a10-92fa-5d40f6313295" />

## Table of Contents
1. [Introduction](#introduction)
2. [Video Source](#video-source)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Features](#features)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction
Tracking and counting Object in video streams is a crucial task in computer vision. This project leverages **YOLOv8 for object detection** and the **Supervision library** for line-based counting to build a robust, real-time tracking and counting pipeline.

### Objectives
- Detect and track Object in videos using YOLOv8.
- Count the number of Object crossing a predefined line.
- Annotate bounding boxes and counts in real-time.
- Provide a reusable framework for similar surveillance or analytics tasks.

---

## Video Source
### Input
- The project works with any Object activity video.  
- Example videos included in repo: `mall_counting.mp4`, `highway_car.mp4`, `highway_car2.mp4`

You can replace it with your own video by updating the `VIDEO_PATH` variable in the code.

---

## Technologies Used
- **Python**: Core programming language.
- **YOLOv8 (Ultralytics)**: Object detection.
- **Supervision**: Line zone tracking & annotation.
- **OpenCV**: Video processing & visualization.
- **NumPy**: Numerical operations.

---

## Installation
### Prerequisites
Ensure Python (>= 3.8) is installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/DataScientist00/Credit-Card-Fraud-Detection-Project.git
   cd Credit-Card-Fraud-Detection-Project
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Place your input video (e.g., `mall_counting.mp4`) in the project directory if not already available.

---

## Usage
Run the following command:
```bash
python app.py
```
or try other scripts (`app2.py`, `app3.py`) depending on your experiment.

The script will:
- Load YOLOv8 model (e.g., `yolov8s.pt` or `yolov8m.pt`).
- Detect Object in each frame.
- Track and count people crossing a virtual line.
- Display real-time annotated output.

Press **ESC** to exit the video window.

---

📷 Preview of Running project

<img width="1434" height="829" alt="Image" src="https://github.com/user-attachments/assets/66edfb76-afbe-4fdd-8c08-3a7c62a55757" />---

## Features
- **Real-Time Detection**: Using YOLOv8 for accurate person detection.
- **Line-Based Counting**: Entry/Exit count tracking with Supervision.
- **Bounding Box Annotation**: Visualize detections with bounding boxes.
- **Customizable**: Works with any video source.
- **Lightweight & Fast**: Runs efficiently on CPU/GPU.

---

## Results
- **Accurate Tracking**: Object crossing the line are counted in both directions.
- **In/Out Metrics**: Displayed directly on the video feed.
- **Applications**:
  - Crowd Management  
  - Retail Store Analytics  
  - Surveillance Systems  

---

## Contributing
We welcome contributions to improve this project! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a pull request.

---

## Acknowledgements
- Thanks to **Ultralytics** for YOLOv8.  
- **Supervision library** for line-based tracking.  
- Open-source community projects that inspired this implementation.

---

## Contact
For questions or support, please reach out:  
- **Email**: nikzmishra@gmail.com  
- **YouTube**: [NeuralArc00](https://www.youtube.com/@NeuralArc00/videos)  
