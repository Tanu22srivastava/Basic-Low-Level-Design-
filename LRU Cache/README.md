# 🧠 LRU Cache – Low Level Design (LLD)

This project is a Python implementation of an **LRU (Least Recently Used) Cache** using a doubly linked list and a hash map for optimal performance.

---

## 🚀 Features

- Fast **O(1)** time complexity for `get()` and `put()` operations
- Custom cache capacity
- Automatic eviction of the least recently used item when capacity is exceeded
- Clean modular design using:
  - Doubly Linked List (via `Node`)
  - Hash map for quick key lookups
  - Separation of demo execution logic in `LRUDemo`

---

## ⚙️ Class Design

### 🔁 `Node`
Represents a node in the doubly linked list with:
- `key`: used for identification in the cache
- `value`: stored data
- `prev`, `next`: pointers for doubly linked structure

### 🧠 `LRU`
The main LRU cache class:
- `cache`: dictionary for O(1) key access
- `head` and `tail`: dummy nodes for managing linked list endpoints
- `put()`: adds/updates key-value pairs
- `get()`: retrieves a value and moves it to the front
- `move_to_head()`, `remove_node()`, `remove_tail()`: helper methods

### 🧪 `LRUDemo`
Contains static method to demonstrate functionality:
- Inserts multiple key-value pairs
- Accesses keys in different orders
- Shows automatic eviction

---



