import os
import cv2
import numpy as np

class CornerDetector:
    def __init__(self, image_path, save_folder):
        self.image_path = image_path
        self.save_folder = save_folder
        os.makedirs(save_folder, exist_ok=True)

        self.original = cv2.imread(image_path)
        if self.original is None:
            raise FileNotFoundError(f"Image not found: {image_path}")

        self.image = self.original.copy()
        self.gray = cv2.cvtColor(self.original, cv2.COLOR_BGR2GRAY)
        self.gray = np.float32(self.gray)
        self.window_name = "🟡 Corner Detection"
        self.display_size = (1280, 720)
        self.corners = []

    def detect_corners(self):
        corners = cv2.goodFeaturesToTrack(self.gray, maxCorners=300,
                                        qualityLevel=0.01, minDistance=10)
        self.corners = []

        if corners is not None:
            for corner in corners:
                # corner.shape = (1, 2), flatten ile [x, y] yapıyoruz
                point = corner.flatten()
                if len(point) == 2:
                    x, y = int(point[0]), int(point[1])
                    self.corners.append((x, y))
                    cv2.circle(self.image, (x, y), 3, (0, 255, 0), -1)

    def get_resized_with_padding(self):
        h, w = self.original.shape[:2]
        target_w, target_h = self.display_size
        scale = min(target_w / w, target_h / h)
        new_w, new_h = int(w * scale), int(h * scale)

        resized = cv2.resize(self.image, (new_w, new_h), interpolation=cv2.INTER_AREA)

        pad_x = (target_w - new_w) // 2
        pad_y = (target_h - new_h) // 2
        padded = cv2.copyMakeBorder(resized, pad_y, target_h - new_h - pad_y,
                                    pad_x, target_w - new_w - pad_x,
                                    cv2.BORDER_CONSTANT, value=(0, 0, 0))

        return padded, scale, pad_x, pad_y

    def draw_on_display(self):
        disp_img, _, _, _ = self.get_resized_with_padding()
        return disp_img

    def draw_on_original_and_save(self, filename="corners.jpg"):
        output = self.original.copy()
        for x, y in self.corners:
            cv2.circle(output, (x, y), 3, (0, 0, 255), -1)
        path = os.path.join(self.save_folder, filename)
        cv2.imwrite(path, output)
        print(f"✅ Saved with corners: {path}")


    def show(self):
        self.detect_corners()
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

        while True:
            if cv2.getWindowProperty(self.window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

            display = self.draw_on_display()
            cv2.imshow(self.window_name, display)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break
            elif key == ord('s'):
                self.draw_on_original_and_save()

        cv2.destroyAllWindows()

def main():
    print("=" * 50)
    print("🎯 Corner Detection Tool")
    print(" [s] Save image with corners")
    print(" [ESC] Exit or close window")
    print("=" * 50)

    image_path = "bird.jpg"
    save_folder = "detected_corners"

    app = CornerDetector(image_path, save_folder)
    app.show()

if __name__ == "__main__":
    main()
