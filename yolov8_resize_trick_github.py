import cv2
from ultralytics import YOLO

def resize_to_screen(image, max_screen_w=1600, max_screen_h=900):
    """Resize the image to fit within given screen bounds."""
    h, w = image.shape[:2]

    scale = min(max_screen_w / w, max_screen_h / h)

    new_w, new_h = int(w * scale), int(h * scale)
    return cv2.resize(image, (new_w, new_h)), scale

def draw_detected_boxes(image, results, scale):
    """Draw YOLO predictions mapped back to the resized image."""
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0]

            # scale coords for the resized image
            x1 = int(x1 * scale)
            y1 = int(y1 * scale)
            x2 = int(x2 * scale)
            y2 = int(y2 * scale)

            cls = int(box.cls[0])
            label = r.names[cls]
            conf = float(box.conf[0])

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 200, 0), 2)
            cv2.putText(image, f"{label} {conf:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255, 255, 255), 2)
    return image

def main():
    model = YOLO("yolov8n.pt")
    img = cv2.imread("sample.jpg")

    # Resize to typical screen-safe values
    resized, scale = resize_to_screen(img)

    # YOLO inference on original size (maximum accuracy)
    results = model(img)[0]

    # Draw boxes correctly on resized image
    output = draw_detected_boxes(resized, [results], scale)

    cv2.imshow("YOLOv8 - Auto Resized", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
