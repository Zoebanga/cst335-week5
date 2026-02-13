# Reflection on Distributed Processing Concepts

This simulation illustrates the three core stages of MapReduce: map, shuffle, and reduce. During the map phase, each partition independently produced key-value pairs such as (laptop, 1). This mirrors how distributed workers process data blocks in parallel across a cluster.

The shuffle phase grouped all identical keys together before aggregation. In real distributed systems, this step requires moving data across the network so that all values for the same key reach the same reducer. This network movement can become a bottleneck at large scale, especially if one key appears far more frequently than others (data skew).

The reduce phase summed all grouped values to produce final totals. While our simulation ran on a single machine, it reflects how large-scale systems operate. Spark improves on traditional MapReduce by using directed acyclic graphs (DAGs), in-memory processing, and optimized shuffle strategies, reducing unnecessary disk writes and improving performance for iterative workloads.
