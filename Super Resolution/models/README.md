# 📦 Pre-trained Super Resolution Models

This folder contains pre-trained super-resolution models used by the OpenCV `cv2.dnn_superres` module.  
These models allow upscaling of images using deep learning-based methods such as EDSR, FSRCNN, ESPCN, and LapSRN.

---

## 🧠 Models Included
- ✅ `FSRCNN_x2.pb`
- ✅ `FSRCNN_x3.pb`
- ✅ `FSRCNN_x4.pb`
- ✅ `LapSRN_x2.pb`
- ✅ `LapSRN_x4.pb`
- ✅ `LapSRN_x8.pb`
- ✅ `ESPCN_x2.pb`
- ✅ `ESPCN_x3.pb`
- ✅ `ESPCN_x4.pb`

❌ Due to GitHub's 25MB file size limit, **EDSR models** (especially higher scales) are not included here.  
You can manually download them from the official OpenCV GitHub repository:

🔗 [https://github.com/opencv/opencv_contrib/tree/master/modules/dnn_superres](https://github.com/opencv/opencv_contrib/tree/master/modules/dnn_superres)

---

## 📜 License

These model files are shared under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).  
They are originally provided by the [OpenCV project](https://opencv.org/) via the `opencv_contrib` repository.

Please give proper credit if you use or redistribute these models.

---

## 📥 How to Use

Simply place the `.pb` model files in this `models/` directory and ensure the main application points to them correctly.

```python
model_path = os.path.join("models", "LapSRN_x4.pb")
sr.readModel(model_path)
sr.setModel("lapsrn", 4)
