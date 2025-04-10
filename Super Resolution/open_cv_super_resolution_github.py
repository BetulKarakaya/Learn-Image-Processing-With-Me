import cv2
import os
import matplotlib.pyplot as plt

class SuperResolution:
    def __init__(self, image_path: str, model_name: str = "EDSR", scale: int = 2):
        self.image_path = image_path
        self.model_name = model_name.upper()
        self.scale = scale
        self.sr = cv2.dnn_superres.DnnSuperResImpl_create()

        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"⚠️ Image not found at path: {self.image_path}")
        
        # Load model
        self.load_model()

    def load_model(self):
        print(f"🚀 Loading model: {self.model_name} with scale x{self.scale}")
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        models_dir = os.path.join(base_dir, "models")

        model_paths = {
            "EDSR": f"EDSR_x{self.scale}.pb",
            "FSRCNN": f"FSRCNN_x{self.scale}.pb",
            "ESPCN": f"ESPCN_x{self.scale}.pb",
            "LAPSRN": f"LapSRN_x{self.scale}.pb"
        }

        model_file = model_paths.get(self.model_name)
        if model_file is None:
            raise ValueError(f"❌ Unsupported model name: '{self.model_name}'. Supported: {list(model_paths.keys())}")
        
        model_path = os.path.join(models_dir, model_file)
        
        print("📁 Looking for model in:", model_path)
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Model file not found: {model_path}")

        self.sr.readModel(model_path)
        self.sr.setModel(self.model_name.lower(), self.scale)

    def upscale(self):
        print("✨ Upscaling image...")
        return self.sr.upsample(self.image)

    def show_result(self, result):
        print("👀 Showing original and enhanced image...")

        resized_original = cv2.resize(self.image, (result.shape[1], result.shape[0]))
        combined = cv2.hconcat([resized_original, result])

        #BGR -> RGB (because matplotlib doesn't like BGR)
        combined_rgb = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(12, 6))
        plt.imshow(combined_rgb)
        plt.title("Original vs Enhanced")
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def save(self, result):
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        result_dir = os.path.join(base_dir, "results")

        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
            print(f"📂 'results' directory created at: {result_dir}")
        else:
            print(f"📂 'results' directory already exists.")

        original_name = os.path.splitext(os.path.basename(self.image_path))[0]
        extension = os.path.splitext(self.image_path)[-1]
        
        filename = f"{original_name}_{self.model_name}_x{self.scale}{extension}"
        full_path = os.path.join(result_dir, filename)

        cv2.imwrite(full_path, result)
        print(f"✅ Enhanced image saved at: {full_path}")


    def run(self):
        upscaled_img = self.upscale()
        self.show_result(upscaled_img)
        self.save(upscaled_img)

def main():
    image_path = "Actitis_hypoleucos_1_tb_(Marek_Szczepanek).jpg" 
    model = "EDSR"  # Options: EDSR, FSRCNN, ESPCN, LAPSRN
    scale = 2       # Options: 2, 3, 4

    sr_app = SuperResolution(image_path=image_path, model_name=model, scale=scale)
    sr_app.run()

if __name__ == "__main__":
    main()
