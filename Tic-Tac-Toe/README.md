# 🎮 Tic Tac Toe – Low Level Design (LLD)

This is a simple Python implementation of a customizable Tic Tac Toe game using Object-Oriented Programming. The game supports any `n x n` board size and two players.

---

## 📚 Features

- Dynamic board size (e.g., 3x3, 4x4, etc.)
- Two human players
- Toss mechanism to decide the first move
- Move validation and win/draw detection
- Clean separation of concerns using OOP principles

---

## 🏗️ Design Overview

### Classes Implemented:

- **`Board`**: Handles board initialization, display, placing moves, and checking win/draw conditions.
- **`Player`**: Stores player name and assigned symbol (X or O).
- **`Game`**: Orchestrates the gameplay including toss, turns, and game loop.

---

## 🧪 Example Gameplay

```python
game = Game("Alice", "Bob", 3)
game.perform_toss()
game.start_game()
