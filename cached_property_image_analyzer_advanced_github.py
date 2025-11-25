from functools import cached_property
from pathlib import Path
from collections import Counter
from typing import Tuple

from PIL import Image


def _human_readable_size(num_bytes: int) -> str:
    """Convert bytes to a human-friendly string (KB, MB, ...)."""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if num_bytes < 1024.0:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.2f} PB"


def _rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """Convert an (R, G, B) tuple to a hex color string."""
    return "#{:02x}{:02x}{:02x}".format(*rgb)


class ImageAnalyzer:
    """Create a simple report about an image file."""

    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.image = Image.open(self.image_path)

    # --------------------------------------------
    # Basic file & image attributes (cheap)
    # --------------------------------------------
    @property
    def file_size_bytes(self) -> int:
        return self.image_path.stat().st_size

    @property
    def file_size(self) -> str:
        return _human_readable_size(self.file_size_bytes)

    @property
    def file_type(self) -> str:
        """Image file format as reported by Pillow (e.g., JPEG, PNG)."""
        return self.image.format or "UNKNOWN"

    @property
    def color_mode(self) -> str:
        """Image color mode (e.g., RGB, CMYK, L, RGBA)."""
        return self.image.mode

    # Expensive / derived computations (cached)
    @cached_property
    def total_pixels(self) -> int:
        """Expensive computation executed ONLY once."""
        width, height = self.image.size
        return width * height

    @cached_property
    def aspect_ratio(self) -> str:
        """Return aspect ratio as a rounded float (width / height)."""
        w, h = self.image.size
        return str(round(w / h, 2))

    @cached_property
    def dominant_color(self) -> Tuple[str, Tuple[int, int, int], float]:
        """
        Robust dominant color detection.
        Returns:
          (hex_color, (r,g,b), percentage)
        Strategy:
          - handle alpha by compositing on white,
          - resize to speed up,
          - reduce to an adaptive palette (e.g. 8 colors),
          - count pixels and compute percentage.
        """
        # work on a copy so we never modify self.image
        img = self.image.copy()

        # Ensure we have RGBA to detect alpha and composite if necessary
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # Composite on white background to handle transparency cleanly
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = Image.alpha_composite(bg, img)

        # Convert to RGB (no alpha now)
        img = img.convert("RGB")

        # Resize to speed up processing (keeps aspect)
        small = img.resize((80, 80), Image.Resampling.LANCZOS)

        # Reduce to an adaptive palette to cluster similar colors
        pal = small.convert("P", palette=Image.ADAPTIVE, colors=8).convert("RGB")

        # Count colors
        pixels = list(pal.getdata())
        if not pixels:
            return ("#000000", (0, 0, 0), 0.0)

        counts = Counter(pixels)
        most_common_rgb, most_common_count = counts.most_common(1)[0][0], counts.most_common(1)[0][1]

        # percentage of image the dominant color covers (approx)
        total = sum(counts.values())
        percentage = round((most_common_count / total) * 100, 2)

        hex_color = _rgb_to_hex(most_common_rgb)
        return (hex_color, most_common_rgb, percentage)

    def show_info(self) -> None:
        print(f"- File: {self.image_path.name}")
        print(f"- File type: {self.file_type}")
        print(f"- File size: {self.file_size} ({self.file_size_bytes} bytes)")
        print(f"- Color mode: {self.color_mode}")
        print(f"- Resolution: {self.image.size[0]} x {self.image.size[1]} (width x height)")
        print(f"- Total pixels: {self.total_pixels}")
        print(f"- Aspect ratio (w/h): {self.aspect_ratio}")
        hex_color, rgb, pct = self.dominant_color
        print(f"- Dominant color: {hex_color} (RGB{rgb})")


def main():
    # Adjust the filename as needed. Example uses 'sample.jpg' same as your original code.
    analyzer = ImageAnalyzer("sample.jpg")

    print("--- IMAGE REPORT ---")
    analyzer.show_info()

    # Demonstrate caching: these accesses won't re-run the expensive computations
    print("\n--- CACHED PROPERTIES (access again) ---")
    print("Total pixels (cached):", analyzer.total_pixels)
    print("Aspect ratio (cached):", analyzer.aspect_ratio)
    print("Dominant color (cached):", analyzer.dominant_color)


if __name__ == "__main__":
    main()
