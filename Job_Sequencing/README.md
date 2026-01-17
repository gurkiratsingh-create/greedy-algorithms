# Job Sequencing with Deadlines (Optimized using DSU)

This repository contains a Python implementation of the **Job Sequencing with Deadlines** problem using a **Greedy approach optimized with Disjoint Set Union (DSU)**.

## Problem
Given two arrays `profit[]` and `deadline[]`, each job takes 1 unit time and only one job can be done at a time. The goal is to **maximize total profit** while completing jobs before their deadlines.

## Approach
- Pair jobs as `(profit, deadline)`
- Sort jobs in descending order of profit (greedy choice)
- Use **DSU (Union-Find)** to find the latest available time slot efficiently
- Assign jobs and update DSU to avoid reusing slots

## Complexity
- **Time:** `O(n log n)`
- **Space:** `O(n)`

## Example
profit = [100, 27, 15, 10]
deadline = [3, 1, 2, 1]
Output: [3, 142]

## File
job_sequencing.py

## Author
**Gurkirat Singh** 
