# Fractional Knapsack (Greedy Algorithm)

This repository contains a Python implementation of the **Fractional Knapsack** problem using a **Greedy approach**.

The Fractional Knapsack problem is a classic example where the greedy strategy produces an optimal solution.

---

## 📌 Problem Statement

Given:
- A set of items, each with a **value (profit)** and **weight**
- A knapsack with a fixed **capacity**

You are allowed to **take fractions of items**.

🎯 **Goal:**  
Maximize the total value in the knapsack without exceeding its capacity.

---

## 💡 Greedy Approach

The optimal strategy for the Fractional Knapsack problem is:

1. Compute the **value-to-weight ratio** for each item  
2. Sort items in **descending order of value/weight**
3. Pick items greedily:
   - Take the whole item if possible
   - Otherwise, take the fractional part that fits

This approach works because fractional selection is allowed.

---

## ⚙️ Algorithm Steps

1. Calculate `va
