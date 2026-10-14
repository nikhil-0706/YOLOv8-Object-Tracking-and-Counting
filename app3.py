
import cv2
import supervision as sv
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8s.pt")

VIDEO_PATH = "mall_counting.mp4"

# Get video dimensions
cap = cv2.VideoCapture(VIDEO_PATH)
ret, frame = cap.read()

if not ret:
    cap.release()
    raise RuntimeError(f"Could not read video: {VIDEO_PATH}")

H, W = frame.shape[:2]
cap.release()

# Counting line in the middle
line_zone = sv.LineZone(
    start=sv.Point(0, H // 2),
    end=sv.Point(W, H // 2)
)
line_annotator = sv.LineZoneAnnotator()

# Bounding box annotator
box_annotator = sv.BoxAnnotator(thickness=2)

# Label annotator
label_annotator = sv.LabelAnnotator(
    text_scale=0.7,
    text_thickness=2
)

# Tracking and counting loop
for result in model.track(
    source=VIDEO_PATH,
    stream=True,
    classes=[0],  # Person only
    imgsz=640,
    tracker="bytetrack.yaml",
    persist=True,
    verbose=False
):
    frame = result.orig_img
    detections = sv.Detections.from_ultralytics(result)

    # Create person labels with tracking IDs
    labels = []

    for class_id, tracker_id in zip(
        detections.class_id,
        detections.tracker_id
    ):
        if tracker_id is not None:
            labels.append(f"person ID: {int(tracker_id)}")
        else:
            labels.append("person")

    # Draw bounding boxes
    frame = box_annotator.annotate(
        scene=frame,
        detections=detections
    )

    # Draw labels above bounding boxes
    frame = label_annotator.annotate(
        scene=frame,
        detections=detections,
        labels=labels
    )

    # Update people counter
    line_zone.trigger(detections)
    line_annotator.annotate(frame, line_zone)

    # Display counts
    cv2.putText(
        frame, f"People (In): {line_zone.in_count}",
        (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 2
    )

    cv2.putText(
        frame, f"People (Out): {line_zone.out_count}",
        (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 2
    )

    cv2.imshow("People Tracking & Counting", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()


