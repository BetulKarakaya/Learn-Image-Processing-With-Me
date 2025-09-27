import cv2
import os


class DNNFaceDetector:
    def __init__(self, image_path: str, folder_name: str = "face_detection_results"):
        self.image = cv2.imread(image_path)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")

        # Load DNN model
        proto_path = os.path.join("DNN", "deploy.prototxt")
        model_path = os.path.join("DNN", "res10_300x300_ssd_iter_140000.caffemodel")

        if not os.path.exists(proto_path) or not os.path.exists(model_path):
            raise FileNotFoundError("❌ Model files not found in 'DNN/' folder")

        self.net = cv2.dnn.readNetFromCaffe(proto_path, model_path)

    def detect_faces(self, conf_threshold=0.5):
        (h, w) = self.image.shape[:2]

        # Prepare input blob for DNN
        blob = cv2.dnn.blobFromImage(
            cv2.resize(self.image, (300, 300)),
            1.0,
            (300, 300),
            (104.0, 177.0, 123.0)
        )
        self.net.setInput(blob)
        detections = self.net.forward()

        count = 0
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > conf_threshold:
                count += 1
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")

                cv2.rectangle(self.image, (startX, startY), (endX, endY), (0, 255, 255), 2)
                text = f"{confidence*100:.1f}%"
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.putText(self.image, text, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        print(f"🔍 {count} faces detected with confidence > {conf_threshold}")

        self.output = self.image.copy()
        cv2.imwrite(os.path.join(self.folder_name, "dnn_result.jpg"), self.output)

    def show_result(self, win_name="DNN Face Detection"):
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.imshow(win_name, self.output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
     #Photo by Elkayslense : https://www.pexels.com/photo/traditional-african-wedding-ceremony-outdoors-34011255/
    image_path = "faces2.jpg"
    folder_name = "face_detection_results"

    detector = DNNFaceDetector(image_path, folder_name)
    detector.detect_faces(conf_threshold=0.3)  
    detector.show_result()


if __name__ == "__main__":
    main()
