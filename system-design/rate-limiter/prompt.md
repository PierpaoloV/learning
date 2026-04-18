# System Design — Rate Limiter (Week 4)

Design a rate limiter that can be used as middleware in a distributed API gateway.

## Requirements to address
- Limit each user to N requests per time window (e.g. 100 req/min)
- Should work across multiple API servers (distributed)
- Low latency — must not add more than 1ms to each request
- Return HTTP 429 when limit is exceeded

## Questions to ask yourself before designing
- Fixed window vs sliding window vs token bucket — which algorithm?
- Where do you store the counters? (local memory vs Redis)
- What happens if the rate limiter itself goes down?
- How do you handle race conditions in distributed counters?

## Write your design in `design.md`
Cover: algorithm choice and tradeoffs, storage backend, distributed synchronization, failure modes.
