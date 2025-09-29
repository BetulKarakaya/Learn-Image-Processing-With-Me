import os
import cv2
import random
from ultralytics import YOLO


class YOLOv8ObjectDetector:
    def __init__(self, image_path: str, folder_name: str = "yolov8_results"):
        """
        Initialize YOLOv8 detector with an image and output folder.
        """
        self.image = cv2.imread(image_path)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")

        # Preprocessing: enhance contrast and reduce noise
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        self.image = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

        # Load YOLOv8 small model (pre-trained on COCO dataset)
        self.model = YOLO("yolov8s.pt")

    def _get_color(self, class_id: int):
        """
        Generate a unique color for each class ID.
        """
        random.seed(class_id)
        return tuple(random.randint(0, 255) for _ in range(3))

    def detect_objects(self, conf_threshold=0.3, iou_threshold=0.4, imgsz=960):
        """
        Detect objects in the image and draw bounding boxes with labels.
        """
        results = self.model.predict(
            self.image,
            conf=conf_threshold,
            iou=iou_threshold,
            imgsz=imgsz
        )
        annotated = self.image.copy()

        count = 0
        for result in results:
            class_names = result.names
            for box in result.boxes:
                conf = float(box.conf[0])
                if conf >= conf_threshold:
                    count += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cls_id = int(box.cls[0])
                    class_name = class_names[cls_id]

                    color = self._get_color(cls_id)
                    cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(
                        annotated,
                        f"{class_name} {conf:.2f}",
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2,
                    )

        print(f"🔍 {count} objects detected with confidence > {conf_threshold}")

        self.output = annotated
        cv2.imwrite(os.path.join(self.folder_name, "yolov8_result.jpg"), self.output)

    def show_result(self, win_name="YOLOv8 Object Detection"):
        """
        Display the detection result in a resizable window.
        """
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.imshow(win_name, self.output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    # Image: Fotoğraf: Burak The Weekender: https://www.pexels.com/tr-tr/fotograf/gunduz-siyah-beyaz-otobus-63505/
    image_path = "cars.jpg"  # Example image
    folder_name = "yolov8_results"

    detector = YOLOv8ObjectDetector(image_path, folder_name)
    detector.detect_objects(conf_threshold=0.3, iou_threshold=0.4, imgsz=960)
    detector.show_result()


if __name__ == "__main__":
    main()
