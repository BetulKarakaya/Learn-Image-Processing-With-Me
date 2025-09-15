import cv2
import numpy as np
import os
import tkinter as tk


class CircleDetector:
    def __init__(self, image_path: str, folder_name: str = "circle_detection_results"):
        """
        Initialize with an image path, prepare output folder, and load the image.
        """
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")

        # Keep copy for drawing
        self.output = self.image.copy()

        # Get screen size for fullscreen display
        root = tk.Tk()
        root.withdraw()
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

    def detect_circles(self, dp=1, min_dist=40, param1=80, param2=40, min_radius=10, max_radius=1000):
        """
        Detect circles using Hough Transform and draw only the first detected circle.
        """
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)

        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=dp,
            minDist=min_dist,
            param1=param1,
            param2=param2,
            minRadius=min_radius,
            maxRadius=max_radius
        )

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :1]:
                x, y, r = i
                cv2.circle(self.output, (x, y), r, (0, 200, 0), 10)  # outline
                cv2.circle(self.output, (x, y), 2, (0, 0, 255), 3)  # center
                print(f"✅ Circle detected at (x={x}, y={y}) with radius={r}")
        else:
            print("⚠️ No circles detected")

        
        cv2.imwrite(f"{self.folder_name}/detected_circle.png", self.output)

    def show_result(self, win_name="Detected Circle"):
        """
        Show the result in full screen.
        """
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(win_name, self.output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def explain_detection(self):
        """
        Explain the circle detection process.
        """
        print("📘 Circle Detection with OpenCV:")
        print("- Convert image to grayscale.")
        print("- Apply median blur to reduce noise.")
        print("- Use Hough Circle Transform to detect circles.")
        print("- Draw the first detected circle and its center.")
        print("- Save and display the result.")


def main():
    #Photo: https://www.pexels.com/photo/person-holding-camera-with-red-lights-on-lens-1413906/
    image_path = "circle.jpg"
    folder_name = "circle_detection_results"

    detector = CircleDetector(image_path, folder_name)
    detector.detect_circles()
    detector.show_result()
    detector.explain_detection()


if __name__ == "__main__":
    main()
