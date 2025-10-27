# PDC Lab Exam - Parallel and Distributed Image Processing

This project implements and compares **three methods** for batch image preprocessing using Python as part of the **Parallel and Distributed Computing Lab Exam**.

Each script processes a dataset of 57 images across 4 folders — *cats*, *dogs*, *cars*, and *flowers* — by resizing them to **128x128 pixels** and adding a **watermark (“PDC Lab”)**.

---

## 📂 Folder Structure

images_dataset/           # Input dataset (4 subfolders)
output_seq/               # Output from sequential processing
output_parallel/          # Output from parallel processing
output_distributed/       # Output from distributed simulation
sequential_process.py     # Task 1: Sequential processing
parallel_process.py       # Task 2: Parallel multiprocessing
distributed_sim.py        # Task 3: Distributed processing simulation
report.txt                # Task 4: Execution time comparison and analysis
README.md                 # Project overview


---

## Scripts Overview

### sequential_process.py
Processes all images **sequentially** using a single CPU thread.  
Saves resized, watermarked images to `output_seq/`.

### parallel_process.py
Uses **multiprocessing.Pool** to process images concurrently.  
Tested with **1, 2, 4, and 8 workers**, and prints a speedup table comparing times.

### distributed_sim.py
Simulates a **distributed setup** with 2 worker nodes.  
Each node processes half of the dataset and reports **individual and total processing times**.

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone [Your-Repo-URL]
   cd [Your-Repo-Name]

    ```
   
2. **Install dependencies**
   ```bash
   pip install pillow
   
   ```

3. **Run the scripts**
   ```bash
   # Sequential Processing
   python sequential_process.py

   # Parallel Processing
   python parallel_process.py

   # Distributed Simulation
   python distributed_sim.py

    ```

## Results Summary

- The total dataset (57 images) processed **very quickly**, resulting in minimal computational load.  
- Due to this, **parallel and distributed versions had higher overhead** compared to sequential.

---

### Parallel Speedup Table

| Workers | Time (s) | Speedup |
| :------: | :------: | :------: |
| 1 | 0.93 | 1.00x |
| 2 | 0.81 | 1.14x |
| 4 | 1.22 | 0.76x |
| 8 | 1.94 | 0.48x |

---

### Distributed Simulation Summary

| Node | Images Processed | Time (s) |
| :--- | :---------------- | :------- |
| Node 1 | 28 | 0.32 |
| Node 2 | 29 | 0.31 |
| **Total Distributed Time** | - | **1.08s** |
| **Efficiency** | - | **0.31x (vs Sequential)** |

---

## Analysis

- **Best Configuration:** 2 workers achieved the best performance (0.81s).  
- **Overall Fastest:** Sequential execution (0.34s total).  
- **Main Point:** The workload was too small; parallel overhead outweighed processing gains.  
- **Observation:** For lightweight image tasks, sequential processing remains most efficient.  
- **Improvement Idea:** Larger datasets or heavier transformations would benefit more from multiprocessing or GPU acceleration.

   
