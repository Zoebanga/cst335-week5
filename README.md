# CST 335 – Week 5  
## Simulating Distributed Processing with MapReduce Concepts

### Project Overview

This project simulates a MapReduce-style distributed processing workflow on a single machine. The goal is to demonstrate how large-scale systems break computation into map, shuffle, and reduce stages.

The dataset represents equipment loan logs from multiple campuses. Although the dataset is small, the structure mirrors how distributed systems operate at scale.

---

## Folder Structure


---

## How It Works

### 1. Partitioning
The full dataset was split into four smaller CSV files. Each partition simulates a distributed storage block (similar to HDFS).

### 2. Map Phase
Each partition is processed independently. The map step outputs key-value pairs in the format:

(item_category, 1)

Example:

### 3. Shuffle Phase
All identical keys are grouped together before aggregation. In real distributed systems, this step requires data to move across the network so that all values for the same key reach the same reducer.

Example grouping:

### 4. Reduce Phase
All grouped values are summed to produce final totals.

Final results:
- laptop: 18  
- camera: 13  
- projector: 9  

---

## How to Run

From the project root folder:

```bash
python map_step.py
python reduce_step.py
results/final_counts.csv

AI was used to help structure explanations and guide implementation logic. All code was reviewed, executed, and validated manually.


