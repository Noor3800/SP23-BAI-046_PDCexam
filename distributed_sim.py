#Task 3
import os
import time
from PIL import Image, ImageDraw, ImageFont
from multiprocessing import Process, Manager

input_folder = "images_dataset"
output_folder = "output_distributed"
os.makedirs(output_folder, exist_ok=True)

def process_images(subset, node_name, result_dict):
    start = time.perf_counter()
    for img_path, out_path in subset:
        img = Image.open(img_path).convert("RGB")
        img = img.resize((128, 128))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), "PDC Lab", fill=(255, 0, 0))
        img.save(out_path)
    end = time.perf_counter()
    result_dict[node_name] = end - start

if __name__ == "__main__":
    all_images = []
    for cls in os.listdir(input_folder):
        cls_input = os.path.join(input_folder, cls)
        cls_output = os.path.join(output_folder, cls)
        os.makedirs(cls_output, exist_ok=True)
        for img_file in os.listdir(cls_input):
            in_path = os.path.join(cls_input, img_file)
            out_path = os.path.join(cls_output, img_file)
            all_images.append((in_path, out_path))

    n = len(all_images)
    half = n // 2
    subset_1, subset_2 = all_images[:half], all_images[half:]

    manager = Manager()
    result_dict = manager.dict()

    p1 = Process(target=process_images, args=(subset_1, "Node 1", result_dict))
    p2 = Process(target=process_images, args=(subset_2, "Node 2", result_dict))

    start_total = time.perf_counter()
    p1.start(); p2.start()
    p1.join(); p2.join()
    end_total = time.perf_counter()

    print("Node 1 processed", len(subset_1), "images in", round(result_dict['Node 1'],2), "s")
    print("Node 2 processed", len(subset_2), "images in", round(result_dict['Node 2'], 2), "s")
    print("Total distributed time: ", round(end_total - start_total, 2), "s")

    seq_time = 18.24  
    efficiency = seq_time / (end_total - start_total)
    print("Efficiency: ", round(efficiency, 2),  "x over sequential")