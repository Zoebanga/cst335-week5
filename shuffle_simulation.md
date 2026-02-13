# Shuffle Simulation

After running the map step, each partition produced key-value pairs in the format:

(item_category, 1)

Example outputs:
laptop,1
camera,1
projector,1

Each partition was processed independently. This simulates distributed workers processing separate data blocks.

---

## What the Shuffle Step Does

The shuffle phase groups all values with the same key across partitions.

Conceptually, after combining all map outputs, the data is reorganized like this:

laptop:    [1,1,1,1,1,1,...]
camera:    [1,1,1,1,...]
projector: [1,1,...]

In a real distributed system (such as Hadoop or Spark), this step requires data to move across machines over the network. All values for the same key must be sent to the same reducer.

Because of this network movement, the shuffle stage is often the most expensive part of distributed processing.

In this simulation, the grouping was conceptual and handled locally, but it mirrors how distributed systems prepare data for aggregation in the reduce phase.
