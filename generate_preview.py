from PIL import Image
import os

src_folder = "images/full"
thumb_folder = "images/thumbs"

os.makedirs(thumb_folder, exist_ok=True)

for filename in os.listdir(src_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
        img_path = os.path.join(src_folder, filename)
        thumb_path = os.path.join(thumb_folder, filename)

        img = Image.open(img_path)
        img.thumbnail((400, 400))  # превью максимум 400px
        img.save(thumb_path, "JPEG", quality=70)

print("✅ Превью сгенерированы в", thumb_folder)
