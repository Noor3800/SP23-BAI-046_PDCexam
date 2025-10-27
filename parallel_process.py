#Task 2
import os
import time
from PIL import Image, ImageDraw, ImageFont
from concurrent.futures import ProcessPoolExecutor

input_folder = "images_dataset"
output_folder = "output_parallel"
os.makedirs(output_folder, exist_ok=True)

def process_image(args):
    img_path, output_path = args
    img = Image.open(img_path).convert("RGB")
    img = img.resize((128, 128))
    draw = ImageDraw.Draw(img)
    text = "PDC Lab"
    font = ImageFont.load_default()
    draw.text((10, 10), text, fill=(255, 0, 0), font=font)
    img.save(output_path)

def run_parallel(workers):
    start = time.perf_counter()

    tasks = []
    for cls in os.listdir(input_folder):
        cls_input = os.path.join(input_folder, cls)
        cls_output = os.path.join(output_folder, cls)
        os.makedirs(cls_output, exist_ok=True)

        for img_file in os.listdir(cls_input):
            in_path = os.path.join(cls_input, img_file)
            out_path = os.path.join(cls_output, img_file)
            tasks.append((in_path, out_path))

    with ProcessPoolExecutor(max_workers=workers) as executor:
        executor.map(process_image, tasks)

    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    results = []
    for w in [1, 2, 4, 8]:
        t = run_parallel(w)
        results.append((w, t))
        print("Workers =", w, "Time =", round(t, 2), "seconds")


    print("\nWorkers | Time (s) | Speedup")
    print("-------- | -------- | -------")
    base = results[0][1]
    for w, t in results:
        print("Workers:", w, "Time:", round(t, 2), "seconds", "Speedup:", round(base/t, 2), "x")


