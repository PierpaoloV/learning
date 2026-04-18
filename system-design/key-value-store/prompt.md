# System Design — Key-Value Store (Week 3)

Design a distributed key-value store like Redis or DynamoDB.

## Requirements to address
- `put(key, value)` and `get(key)` operations
- Keys and values are strings (up to 10KB)
- 1M writes/day, 10M reads/day
- Data must be durable (survive restarts)
- High availability (no single point of failure)

## Questions to ask yourself before designing
- Do we need strong consistency or is eventual consistency OK?
- How do we distribute keys across nodes?
- What happens when a node goes down?
- How do we handle hot keys?

## Write your design in `design.md`
Cover: partitioning strategy (consistent hashing), replication, conflict resolution, write/read path, failure handling.
