# Performance Comparison: Sequential vs Partitioned Workflow

## Sequential Workflow

In a sequential approach, the entire loans_full.csv file would be processed in one pass on a single machine. The system reads every row and counts item categories in a single loop.

This approach is simple but has limitations:
- No parallel processing
- If the process fails, the entire job must restart
- Does not scale well for large datasets

## Partitioned Workflow (Simulated Distributed Processing)

In the partitioned workflow, the data is split into multiple smaller CSV files. Each partition is processed independently during the map phase.

Advantages:
- Each partition could be processed in parallel on different machines
- If one partition fails, only that partition needs reprocessing
- Scales better as data size increases

Although our laptop runs the partitions sequentially, the structure mirrors how distributed systems like Hadoop and Spark operate across clusters.
