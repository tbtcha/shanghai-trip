import os
import json
from PIL import Image

# папки
full_dir = "images/full"
thumb_dir = "images/thumbs"
output_file = "images.json"

# создаём папку для превью
os.makedirs(thumb_dir, exist_ok=True)

images_data = []

for file in os.listdir(full_dir):
    if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
        full_path = os.path.join(full_dir, file)
        thumb_path = os.path.join(thumb_dir, file)

        # генерируем превью (если нет)
        if not os.path.exists(thumb_path):
            with Image.open(full_path) as img:
                img.thumbnail((400, 400))  # макс. 400px
                img.save(thumb_path, "JPEG", quality=70)

        # определяем ориентацию
        with Image.open(full_path) as img:
            width, height = img.size
            if width > height:
                orientation = "landscape"
            elif width < height:
                orientation = "portrait"
            else:
                orientation = "square"

        images_data.append({
            "file": file,
            "thumb": os.path.join("images/thumbs", file),
            "full": os.path.join("images/full", file),
            "width": width,
            "height": height,
            "orientation": orientation
        })

# сохраняем JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(images_data, f, ensure_ascii=False, indent=2)

print(f"✅ Saved {len(images_data)} images to {output_file}")
