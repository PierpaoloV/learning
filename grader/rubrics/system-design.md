# System Design Grading Rubric

Grade the design on these 6 dimensions (1–5 each):

## 1. Requirements Clarification (1–5)
- 5: Clearly identified functional + non-functional requirements, asked good questions
- 3: Covered basics but missed important constraints
- 1: Jumped straight to solution without clarifying

## 2. High-Level Design (1–5)
- 5: Clear architecture diagram/description, right components chosen
- 3: Reasonable design but missing key components
- 1: Vague or incorrect architecture

## 3. Scalability (1–5)
- 5: Addressed horizontal scaling, load balancing, sharding, caching
- 3: Some scalability considerations
- 1: No scalability discussion

## 4. Data Model (1–5)
- 5: Appropriate DB choice (SQL vs NoSQL justified), schema design, indexing
- 3: Basic schema, weak justification
- 1: Wrong DB choice or no data model

## 5. Bottlenecks & Trade-offs (1–5)
- 5: Identified bottlenecks, discussed trade-offs (consistency vs availability, etc.)
- 3: Mentioned some trade-offs
- 1: No trade-off analysis

## 6. Depth on One Component (1–5)
- 5: Went deep on one subsystem (e.g. ranking, feed generation, rate limiting)
- 3: Surface-level on everything
- 1: No depth anywhere

## Output format
Return a markdown report with score per dimension, total /30, and specific gaps to address.
