import os
import json
from PIL import Image

image_dir = "images"
output_file = "images.json"

images_data = []

for file in os.listdir(image_dir):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
        filepath = os.path.join(image_dir, file)
        with Image.open(filepath) as img:
            width, height = img.size
            if width > height:
                orientation = "landscape"
            elif width < height:
                orientation = "portrait"
            else:
                orientation = "square"
            images_data.append({
                "file": file,
                "width": width,
                "height": height,
                "orientation": orientation
            })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(images_data, f, ensure_ascii=False, indent=2)

print(f"✅ Saved {len(images_data)} images to {output_file}")
