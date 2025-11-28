"""
YOLOv8 NMS Trick - Full Script (with screen-fit preview)
- Shows WRONG (duplicates/no filtering) vs CORRECT (confidence filter + per-class NMS)
- Ensures the combined preview always fits your screen
Requirements:
    pip install ultralytics opencv-python numpy
"""
from pathlib import Path
import cv2
import numpy as np
from ultralytics import YOLO  # pip install ultralytics

def get_screen_size(default=(1600, 900)):
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        root.destroy()
        return (w, h)
    except Exception:
        pass
    try:
        import ctypes
        user32 = ctypes.windll.user32
        w = user32.GetSystemMetrics(0)
        h = user32.GetSystemMetrics(1)
        return (w, h)
    except Exception:
        pass

    return default


def resize_to_screen(image: np.ndarray, max_ratio: float = 0.95) -> np.ndarray:
    screen_w, screen_h = get_screen_size()
    max_w = int(screen_w * max_ratio)
    max_h = int(screen_h * max_ratio)

    img_h, img_w = image.shape[:2]

    scale_w = max_w / img_w
    scale_h = max_h / img_h
    scale = min(1.0, scale_w, scale_h)

    if scale >= 1.0:
        return image.copy()

    new_w = max(1, int(img_w * scale))
    new_h = max(1, int(img_h * scale))
    return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)


def nms_numpy(boxes: np.ndarray, scores: np.ndarray, iou_threshold: float = 0.45):
    """
    boxes: (N,4) array [x1,y1,x2,y2]
    scores: (N,) confidence scores
    returns: indices of boxes to keep
    """
    if boxes.size == 0:
        return []

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    areas = (x2 - x1) * (y2 - y1)
    order = scores.argsort()[::-1]  # desc by score

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        # IoU with remaining
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1)
        h = np.maximum(0.0, yy2 - yy1)
        inter = w * h
        iou = np.zeros_like(inter)
        denom = areas[i] + areas[order[1:]] - inter
        valid = denom > 0
        if np.any(valid):
            iou[valid] = inter[valid] / denom[valid]

        inds = np.where(iou <= iou_threshold)[0]
        order = order[inds + 1]  # shift because order[0] was current
    return keep


def draw_boxes(img: np.ndarray, boxes, scores, classes, names=None, color=(0, 255, 0)):
    """
    Draw boxes on a BGR image. `boxes` expected in pixel coords [x1,y1,x2,y2].
    """
    out = img.copy()
    for (x1, y1, x2, y2), s, c in zip(boxes.astype(int).tolist(), scores.tolist(), classes.tolist()):
        cv2.rectangle(out, (x1, y1), (x2, y2), color, 2)
        label = f"{names[int(c)] if names else int(c)} {s:.2f}"
        cv2.putText(out, label, (x1, max(15, y1 - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
    return out

def main():
    img_path = "faces2.jpg"  # change if you want
    if not Path(img_path).exists():
        raise SystemExit("Put a sample.jpg next to this script or change img_path.")

    # read original with OpenCV (BGR)
    orig = cv2.imread(img_path)
    if orig is None:
        raise SystemExit("Cannot read image. Is the file corrupted?")

    # load model (downloads yolov8n.pt if needed)
    model = YOLO("yolov8n.pt")

    # Run inference
    results = model(orig)[0]  # single image Results

    # Extract boxes, scores, classes robustly (works whether on CPU tensor or numpy)
    def to_numpy(x):
        try:
            return x.cpu().numpy()
        except Exception:
            try:
                return x.numpy()
            except Exception:
                return np.array(x)

    boxes_all = to_numpy(results.boxes.xyxy) if hasattr(results.boxes, "xyxy") else to_numpy(results.boxes.xyxy)
    scores_all = to_numpy(results.boxes.conf)
    classes_all = to_numpy(results.boxes.cls)
    names = results.names if hasattr(results, "names") else None

    
    # WRONG: draw everything the model returned (no manual filtering, no NMS)
    # For teaching, artificially duplicate boxes to emulate duplicates
    if boxes_all.size > 0:
        boxes_dup = np.vstack([boxes_all, boxes_all + np.array([5, 5, 5, 5])])  # slightly shifted copy
        scores_dup = np.concatenate([scores_all, scores_all * 0.8])
        classes_dup = np.concatenate([classes_all, classes_all])
    else:
        boxes_dup = boxes_all
        scores_dup = scores_all
        classes_dup = classes_all

    wrong_drawn = draw_boxes(orig, boxes_dup, scores_dup, classes_dup, names=names, color=(0, 0, 255))

  
    # CORRECT: confidence threshold + per-class NMS
    conf_thresh = 0.25
    iou_thresh = 0.45

    mask = scores_all >= conf_thresh
    boxes_filtered = boxes_all[mask]
    scores_filtered = scores_all[mask]
    classes_filtered = classes_all[mask]

    if boxes_filtered.size == 0:
        print("No detections above confidence threshold.")
        correct_drawn = orig.copy()
    else:
        keep_indices = []
        for cls_id in np.unique(classes_filtered):
            inds = np.where(classes_filtered == cls_id)[0]
            cls_boxes = boxes_filtered[inds]
            cls_scores = scores_filtered[inds]
            keep = nms_numpy(cls_boxes, cls_scores, iou_threshold=iou_thresh)
            if len(keep) > 0:
                keep_indices.extend(inds[keep])

        if len(keep_indices) == 0:
            correct_drawn = orig.copy()
        else:
            boxes_final = boxes_filtered[keep_indices]
            scores_final = scores_filtered[keep_indices]
            classes_final = classes_filtered[keep_indices]
            correct_drawn = draw_boxes(orig, boxes_final, scores_final, classes_final, names=names, color= (255,184,140 ))

   
    # Prepare side-by-side comparison and ensure it fits screen
    # Resize each panel for display if the original is huge, but keep same sizes so hstack works.
    max_single_w = 1400  # safety per-panel max width (if too big we'll scale down combined)
    h, w = orig.shape[:2]
    scale_panel = min(1.0, max_single_w / w)
    disp_wrong = cv2.resize(wrong_drawn, (int(w * scale_panel), int(h * scale_panel)), interpolation=cv2.INTER_AREA)
    disp_correct = cv2.resize(correct_drawn, (int(w * scale_panel), int(h * scale_panel)), interpolation=cv2.INTER_AREA)

    combined = np.hstack([disp_wrong, disp_correct])
    try:
        cv2.putText(combined, "WRONG: duplicates, no filtering (red)", (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(combined, "CORRECT: conf filter + NMS (green)", (int(w * scale_panel) + 10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 184,140), 2)
    except Exception:
        pass  # safe guard for very small images

    preview = resize_to_screen(combined)

    winname = "YOLOv8 - NMS Trick: WRONG vs CORRECT"
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.imshow(winname, preview)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
