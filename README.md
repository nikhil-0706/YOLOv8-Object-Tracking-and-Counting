# YOLOv8 Object Tracking and Counting

A computer vision project for detecting, tracking, and counting people and vehicles in video footage using YOLOv8, Supervision, and OpenCV.

## Overview

This project implements object detection, tracking, and line-crossing counting using YOLOv8. It supports people counting as well as vehicle detection and counting for cars and trucks. Bounding boxes, class labels, tracking IDs, and directional counts are displayed on the video.

## Features

- **Object Detection:** Detect people and vehicles using YOLOv8.
- **Object Tracking:** Track detected objects across video frames using ByteTrack.
- **Bounding Boxes and Labels:** Display object classes and tracking IDs.
- **People Counting:** Count people crossing a virtual line.
- **Vehicle Counting:** Track cars and trucks and count crossings separately.
- **Combined Counters:** Display total vehicle entries and exits.
- **Video Processing:** Process local video files using OpenCV.

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- Supervision
- OpenCV
- ByteTrack

## Project Structure

```text
YOLOv8-Object-Tracking-and-Counting/
├── app.py
├── app2.py
├── app3.py
├── requirements.txt
├── README.md
├── highway_car.mp4
├── mall_counting.mp4
└── yolov8s.pt
```

The exact files in your repository may differ. Video files and model weights may be excluded from Git if they are too large.

## Requirements

- Python 3.11 recommended
- pip
- Git
- A compatible operating system for OpenCV

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/nikhil-0706/YOLOv8-Object-Tracking-and-Counting.git
cd YOLOv8-Object-Tracking-and-Counting
```

### 2. Create a virtual environment

**Windows (Command Prompt):**

```bat
py -3.11 -m venv .venv
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you do not have a complete `requirements.txt`, install the main libraries with:

```bash
pip install ultralytics supervision opencv-python
```

### 4. Add the input videos and model weights

Place the required video files and model weights in the project directory if they are not included in the repository.

## Usage

Activate the virtual environment before running any script.

### Vehicle tracking and counting

```bash
python app.py
```

This script is intended for tracking vehicles, displaying bounding boxes and labels, and counting line crossings.

### Additional tracking experiment

```bash
python app2.py
```

The functionality depends on the implementation in `app2.py`.

### People tracking and counting

```bash
python app3.py
```

This script detects people, displays bounding boxes and tracking IDs, and counts crossings of a virtual line.

Press **ESC** to close the video window.

## Configuration

You can customize the video source by changing the `VIDEO_PATH` variable in the relevant Python script.

For the standard YOLOv8 COCO model:

- `0`: Person
- `2`: Car
- `7`: Truck

For example, `classes=[2, 7]` filters detections to cars and trucks, while `classes=[0]` selects people.

## Applications

- Traffic monitoring
- Vehicle flow analysis
- People counting
- Crowd monitoring
- Retail footfall analysis
- Video-based computer vision experiments

## Limitations

- Detection accuracy depends on video quality, lighting, occlusion, and model performance.
- Tracking IDs can change when objects disappear or become occluded.
- Line-crossing counts depend on the line placement and direction of movement.
- CPU inference may be slower than inference on a compatible GPU.
- Counts should be validated on the intended video before operational use.

## Acknowledgements

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [Supervision](https://github.com/roboflow/supervision)
- [OpenCV](https://opencv.org/)

## License

Add a license if you intend to distribute this project publicly. Until a license is included, reuse is subject to applicable copyright law.
