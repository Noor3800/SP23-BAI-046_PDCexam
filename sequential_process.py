#Task 1
import os
import time
from PIL import Image, ImageDraw, ImageFont

input_folder = "images_dataset"
output_folder = "output_seq"
os.makedirs(output_folder, exist_ok=True)

def process_image(img_path, output_path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((128, 128)) 

    # Add watermark
    draw = ImageDraw.Draw(img)
    text = "PDC Lab"
    font = ImageFont.load_default()
    draw.text((10, 10), text, fill=(255, 0, 0), font=font)

    img.save(output_path)

start = time.perf_counter()

for cls in os.listdir(input_folder):
    cls_input = os.path.join(input_folder, cls)
    cls_output = os.path.join(output_folder, cls)
    os.makedirs(cls_output, exist_ok=True)

    for img_file in os.listdir(cls_input):
        in_path = os.path.join(cls_input, img_file)
        out_path = os.path.join(cls_output, img_file)
        process_image(in_path, out_path)

end = time.perf_counter()
print(f"Sequential Processing Time: {end - start:.2f} seconds")
