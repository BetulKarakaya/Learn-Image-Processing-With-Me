import cv2
import os
import tkinter as tk


class FaceDetector:
    def __init__(self, image_path: str, folder_name: str = "face_detection_results"):
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")

        # Convert to grayscale
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Enhance contrast (useful for group photos and low lighting)
        self.gray = cv2.equalizeHist(self.gray)

        # Haarcascade file paths
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    def detect_face(self):
        # Adjusted parameters for better detection
        faces = self.face_cascade.detectMultiScale(
            self.gray,
            scaleFactor=1.1,   # More sensitive search
            minNeighbors=8,    # Stronger filter to reduce false positives
            minSize=(40, 40)   # Ignore very small face-like patterns
        )
        print(f"🔍 {len(faces)} faces detected.")

        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 255, 0), 2)
            roi_gray = self.gray[y:y+h, x:x+w]
            roi_color = self.image[y:y+h, x:x+w]

            eyes = self.eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(10, 10)
            )

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)

        self.output = self.image.copy()
        cv2.imwrite(os.path.join(self.folder_name, "result.jpg"), self.output)

    def show_result(self, win_name="Detected Faces"):
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(win_name, self.output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def explain_detection(self):
        print("✔️ Faces detected with tuned Haar cascade parameters:")
        print("   - scaleFactor=1.1 → more precise search")
        print("   - minNeighbors=8 → reduces false positives")
        print("   - minSize=(40,40) → ignores very small objects")
        print("✔️ Histogram equalization applied to enhance contrast")


def main():
    #Photo by Elkayslense : https://www.pexels.com/photo/traditional-african-wedding-ceremony-outdoors-34011255/
    image_path = "faces2.jpg"
    folder_name = "face_detection_results"

    detector = FaceDetector(image_path, folder_name)
    detector.detect_face()
    detector.show_result()
    detector.explain_detection()


if __name__ == "__main__":
    main()
