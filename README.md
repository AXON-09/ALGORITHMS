# Algorithms

A collection of **fundamental Data Structures and Algorithms implemented in Python 3**.

This repository focuses on building a strong foundation in **Data Structures and Algorithms**, understanding how algorithms work, their implementation, and their time and space complexity.

> **Note:** This repository contains base-building algorithm implementations only. LeetCode and coding-problem solutions are maintained separately.

---

## 📚 Algorithms

### 1. Complexity

* Big-O Notation
* Time Complexity
* Space Complexity
* Best Case
* Average Case
* Worst Case
* Amortized Analysis Basics

---

### 2. Arrays

* Array Traversal
* Array Insertion
* Array Deletion
* Finding Maximum / Minimum
* Array Reversal
* Prefix Sum
* Difference Array
* Kadane's Algorithm
* Two Pointers
* Sliding Window
* Frequency Counting

---

### 3. Strings

* String Traversal
* String Reversal
* Palindrome
* Character Frequency
* Anagram
* Two Pointers
* Sliding Window

---

### 4. Searching

* Linear Search
* Binary Search
* Binary Search on Answer

---

### 5. Sorting

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Counting Sort
* Heap Sort

---

### 6. Hashing

* Hash Table Basics
* Hash Function
* Hashing
* HashSet
* HashMap / Dictionary
* Frequency Map
* Hash Collisions
* Collision Handling
* Chaining
* Linear Probing
* Quadratic Probing

---

### 7. Linked Lists

* Singly Linked List
* Traversal
* Insertion
* Deletion
* Reverse Linked List
* Finding Middle Node
* Fast & Slow Pointers
* Cycle Detection
* Merge Two Sorted Lists

---

### 8. Stack

* Stack Implementation
* Push
* Pop
* Peek
* Stack using Array
* Stack using Linked List
* Min Stack
* Monotonic Stack
* Next Greater Element
* Infix / Prefix / Postfix Basics

---

### 9. Queue

* Queue Implementation
* Enqueue
* Dequeue
* Queue using Array
* Queue using Linked List
* Circular Queue
* Deque
* Priority Queue
* BFS Basics

---

### 10. Recursion

* Base Case
* Recursive Case
* Factorial
* Fibonacci
* Sum of Numbers
* Power Calculation
* Recursive Array Traversal
* Recursive String Traversal
* Tree Recursion
* Backtracking Basics

---

### 11. Trees

* Binary Tree
* Binary Search Tree
* Tree Traversal

  * Preorder
  * Inorder
  * Postorder
  * Level Order
* Tree Height
* Tree Depth
* BST Search
* BST Insertion

---

### 12. Heaps / Priority Queue

* Min Heap
* Max Heap
* Heapify
* Build Heap
* Heap Sort
* Priority Queue
* Python `heapq`

---

### 13. Graphs

#### Graph Representation

* Adjacency Matrix
* Adjacency List

#### Graph Traversal

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

#### Basic Graph Algorithms

* Connected Components
* Cycle Detection

#### Shortest Path

* BFS Shortest Path
* Dijkstra's Algorithm

---

### 14. Greedy

* Greedy Strategy
* Activity Selection
* Fractional Knapsack
* Interval Scheduling
* Jump Game

---

### 15. Backtracking

* Subsets
* Permutations
* Combinations
* Combination Sum
* Maze Problems

---

### 16. Dynamic Programming — Basics

* Memoization
* Tabulation
* 1D Dynamic Programming
* 2D Dynamic Programming
* Fibonacci
* Climbing Stairs
* House Robber
* Knapsack Basics

---

### 17. Bit Manipulation

* Bitwise AND
* Bitwise OR
* Bitwise XOR
* Bitwise NOT
* Left Shift
* Right Shift
* Check Odd / Even
* Set Bit
* Clear Bit
* Toggle Bit
* XOR Basics

---

## 🧠 Important Problem-Solving Patterns

These are fundamental patterns that repeatedly appear across different algorithms and data structures.

* Two Pointers
* Sliding Window
* Fast & Slow Pointers
* Prefix Sum
* Difference Array
* Frequency Counting
* Monotonic Stack
* Binary Search
* BFS / DFS
* Backtracking
* Greedy
* Dynamic Programming

---

## 🗂️ Repository Structure

```text
algorithms/
│
├── 01_complexity/
│   ├── big_o.py
│   ├── time_complexity.py
│   ├── space_complexity.py
│   └── amortized_analysis.py
│
├── 02_arrays/
│   ├── traversal.py
│   ├── insertion.py
│   ├── deletion.py
│   ├── find_max_min.py
│   ├── reverse_array.py
│   ├── prefix_sum.py
│   ├── difference_array.py
│   ├── kadanes_algorithm.py
│   ├── two_pointers.py
│   ├── sliding_window.py
│   └── frequency_counting.py
│
├── 03_strings/
│   ├── traversal.py
│   ├── reverse_string.py
│   ├── palindrome.py
│   ├── character_frequency.py
│   ├── anagram.py
│   ├── two_pointers.py
│   └── sliding_window.py
│
├── 04_searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   └── binary_search_on_answer.py
│
├── 05_sorting/
│   ├── bubble_sort.py
│   ├── selection_sort.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   ├── counting_sort.py
│   └── heap_sort.py
│
├── 06_hashing/
│   ├── hash_table.py
│   ├── hash_function.py
│   ├── hash_collision.py
│   ├── chaining.py
│   ├── linear_probing.py
│   ├── quadratic_probing.py
│   └── frequency_map.py
│
├── 07_linked_lists/
│   ├── singly_linked_list.py
│   ├── traversal.py
│   ├── insertion.py
│   ├── deletion.py
│   ├── reverse_linked_list.py
│   ├── find_middle.py
│   ├── fast_slow_pointer.py
│   ├── detect_cycle.py
│   └── merge_sorted_lists.py
│
├── 08_stacks/
│   ├── stack.py
│   ├── stack_using_array.py
│   ├── stack_using_linked_list.py
│   ├── push_pop_peek.py
│   ├── min_stack.py
│   ├── monotonic_stack.py
│   └── next_greater_element.py
│
├── 09_queues/
│   ├── queue.py
│   ├── queue_using_array.py
│   ├── queue_using_linked_list.py
│   ├── circular_queue.py
│   ├── deque.py
│   └── priority_queue.py
│
├── 10_recursion/
│   ├── basic_recursion.py
│   ├── factorial.py
│   ├── fibonacci.py
│   ├── sum_of_numbers.py
│   ├── power.py
│   ├── recursive_array.py
│   └── recursive_string.py
│
├── 11_trees/
│   ├── binary_tree.py
│   ├── binary_search_tree.py
│   ├── preorder.py
│   ├── inorder.py
│   ├── postorder.py
│   ├── level_order.py
│   ├── tree_height.py
│   ├── tree_depth.py
│   ├── bst_search.py
│   └── bst_insertion.py
│
├── 12_heaps/
│   ├── min_heap.py
│   ├── max_heap.py
│   ├── heapify.py
│   ├── build_heap.py
│   ├── heap_sort.py
│   └── priority_queue.py
│
├── 13_graphs/
│   ├── graph_representation.py
│   ├── adjacency_matrix.py
│   ├── adjacency_list.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── connected_components.py
│   ├── cycle_detection.py
│   │
│   └── shortest_path/
│       ├── bfs_shortest_path.py
│       └── dijkstra.py
│
├── 14_greedy/
│   ├── activity_selection.py
│   ├── fractional_knapsack.py
│   ├── interval_scheduling.py
│   └── jump_game.py
│
├── 15_backtracking/
│   ├── subsets.py
│   ├── permutations.py
│   ├── combinations.py
│   ├── combination_sum.py
│   └── maze.py
│
├── 16_dynamic_programming/
│   ├── memoization.py
│   ├── tabulation.py
│   ├── fibonacci.py
│   ├── climbing_stairs.py
│   ├── house_robber.py
│   └── knapsack.py
│
├── 17_bit_manipulation/
│   ├── bitwise_operations.py
│   ├── check_odd_even.py
│   ├── set_bit.py
│   ├── clear_bit.py
│   ├── toggle_bit.py
│   └── xor_basics.py
│
└── 18_patterns/
    ├── two_pointers.py
    ├── sliding_window.py
    ├── fast_slow_pointer.py
    ├── prefix_sum.py
    ├── difference_array.py
    ├── monotonic_stack.py
    ├── binary_search.py
    ├── bfs_dfs.py
    ├── backtracking.py
    ├── greedy.py
    └── dynamic_programming.py
```

---

## 📈 Complexity Reference

| Algorithm      |    Time Complexity | Space Complexity |
| -------------- | -----------------: | ---------------: |
| Linear Search  |               O(n) |             O(1) |
| Binary Search  |           O(log n) |             O(1) |
| Bubble Sort    |              O(n²) |             O(1) |
| Selection Sort |              O(n²) |             O(1) |
| Insertion Sort |              O(n²) |             O(1) |
| Merge Sort     |         O(n log n) |             O(n) |
| Quick Sort     | O(n log n) Average | O(log n) Average |
| Heap Sort      |         O(n log n) |             O(1) |
| Counting Sort  |           O(n + k) |         O(n + k) |
| BFS            |           O(V + E) |             O(V) |
| DFS            |           O(V + E) |             O(V) |
| Dijkstra       |   O((V + E) log V) |             O(V) |

---

## 📖 Recommended Learning Order

Build the foundation progressively:

```text
Complexity
    ↓
Arrays
    ↓
Strings
    ↓
Searching
    ↓
Sorting
    ↓
Hashing
    ↓
Linked Lists
    ↓
Stack
    ↓
Queue
    ↓
Recursion
    ↓
Trees
    ↓
Heap
    ↓
Graphs
    ↓
Dijkstra
    ↓
Greedy
    ↓
Backtracking
    ↓
Dynamic Programming
    ↓
Bit Manipulation
    ↓
Problem-Solving Patterns
```

---

## 🐍 Language

**Python 3**

---

## 🎯 Purpose

The purpose of this repository is to build a strong foundation in **Data Structures and Algorithms** through implementation and understanding.

Each implementation focuses on:

* Understanding the algorithm
* Implementing it from scratch
* Understanding the underlying logic
* Analyzing time complexity
* Analyzing space complexity
* Learning reusable algorithmic patterns

### Separate Repository

**LeetCode problems, coding questions, and interview problem solutions are maintained separately.**

This repository is dedicated to **learning the algorithms themselves**.
