
import cv2
import supervision as sv
from ultralytics import YOLO

model = YOLO("yolov8s.pt")
VIDEO_PATH = "highway_car.mp4"

CAR, TRUCK = 2, 7

cap = cv2.VideoCapture(VIDEO_PATH)
ret, frame = cap.read()

if not ret:
    cap.release()
    raise RuntimeError(f"Cannot read video: {VIDEO_PATH}")

H, W = frame.shape[:2]
cap.release()

LINE_Y = H // 2

line_zone = sv.LineZone(
    start=sv.Point(0, LINE_Y),
    end=sv.Point(W, LINE_Y)
)
line_annotator = sv.LineZoneAnnotator()

box_annotator = sv.BoxAnnotator(thickness=2)
label_annotator = sv.LabelAnnotator(
    text_scale=0.6,
    text_thickness=2
)

# Six counters
car_in = car_out = 0
truck_in = truck_out = 0
total_in = total_out = 0

# Track each ID's previous vertical position and crossing directions
previous_y = {}
counted = {}

for result in model.track(
    source=VIDEO_PATH,
    stream=True,
    classes=[CAR, TRUCK],
    imgsz=640,
    tracker="bytetrack.yaml",
    persist=True,
    verbose=False
):
    frame = result.orig_img
    detections = sv.Detections.from_ultralytics(result)

    # Update Supervision's line-zone visualization/state
    line_zone.trigger(detections)

    if detections.tracker_id is not None:
        for xyxy, track_id, class_id in zip(
            detections.xyxy,
            detections.tracker_id,
            detections.class_id
        ):
            if track_id is None:
                continue

            track_id = int(track_id)
            class_id = int(class_id)

            # Bottom-center point of the bounding box
            center_y = int((xyxy[1] + xyxy[3]) / 2)

            if track_id not in counted:
                counted[track_id] = set()

            if track_id in previous_y:
                old_y = previous_y[track_id]

                # Moving from above to below the line
                if old_y < LINE_Y <= center_y:
                    if "down" not in counted[track_id]:
                        counted[track_id].add("down")
                        total_in += 1

                        if class_id == CAR:
                            car_in += 1
                        elif class_id == TRUCK:
                            truck_in += 1

                # Moving from below to above the line
                elif old_y > LINE_Y >= center_y:
                    if "up" not in counted[track_id]:
                        counted[track_id].add("up")
                        total_out += 1

                        if class_id == CAR:
                            car_out += 1
                        elif class_id == TRUCK:
                            truck_out += 1

            previous_y[track_id] = center_y

    # Bounding-box labels
    labels = []
    for class_id, track_id in zip(
        detections.class_id,
        detections.tracker_id
    ):
        name = model.names[int(class_id)]
        labels.append(
            f"{name} ID:{int(track_id)}"
            if track_id is not None else name
        )

    frame = box_annotator.annotate(
        scene=frame,
        detections=detections
    )
    frame = label_annotator.annotate(
        scene=frame,
        detections=detections,
        labels=labels
    )

    line_annotator.annotate(frame, line_zone)

    counters = [
        f"Cars In: {car_in}",
        f"Cars Out: {car_out}",
        f"Trucks In: {truck_in}",
        f"Trucks Out: {truck_out}",
        f"Total In: {total_in}",
        f"Total Out: {total_out}"
    ]

    for i, text in enumerate(counters):
        cv2.putText(
            frame, text, (25, 30 + i * 32),
            cv2.FONT_HERSHEY_SIMPLEX, 0.75,
            (0, 255, 0), 2
        )

    cv2.imshow("Vehicle Tracking & Counting", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

