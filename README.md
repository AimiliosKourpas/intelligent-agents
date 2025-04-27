---

# Intelligent Agents - Generic Planner

---

## 📜 Project Description
This project implements a **Generic Planner** capable of solving different AI planning problems without requiring changes to the core code. Specifically, it tackles two classic problems:

- **Block World**
- **Water Jug Problem**

Both problems are addressed using Artificial Intelligence search algorithms such as **A\***, **Best-First Search**, and **Breadth-First Search**.

---

## 🔥 What is a Generic Planner?
A **Generic Planner** produces an action sequence to transition an agent from an initial to a goal state. It’s called *generic* because it does not need modifications to solve different problems — only different problem descriptions and available actions are needed.

**Advantages:**
- High flexibility across problems
- Easier maintenance and scalability

**Disadvantages:**
- May have lower performance compared to specialized planners
- Increased implementation complexity

---

## 🧩 Problem Descriptions

### Block World
A classic AI domain involving stacking wooden blocks according to certain rules.

**Rules and Constraints:**
- Only one block can be moved at a time.
- A block can only be placed on the table or atop another block.
- Blocks covered by others must be uncovered first.

**Goal:**  
Create specific stacks of blocks matching a target configuration.

---

### Water Jug Problem
The Water Jug Puzzle involves measuring out specific amounts of water using jugs of different capacities.

**Rules and Actions:**
- Fill a jug to its maximum capacity.
- Empty a jug completely.
- Pour water from one jug to another.

**Goal:**  
Reach a specified volume of water in one or more jugs.

---

## 🧠 Theoretical Foundation

The planner uses two major AI search algorithms:
- **A\* Search Algorithm**: Combines path cost and heuristic estimation to efficiently find optimal paths.
- **Best-First Search Algorithm**: Explores nodes with the most promising heuristic evaluation first.
- **Breadth-First Search (BFS)**: Used particularly for solving the Water Jug Problem by systematically exploring neighbor nodes layer by layer.

The implementation focuses on:
- **State Representation:** Using clear structures to represent world states.
- **Transition Modeling:** Defining available actions for state changes.
- **Goal Checking:** Verifying if the goal state is achieved after action sequences.

Programming Language: **Python**

---

## ⚙️ How the Application Works

When starting the application:
- The user is presented with a menu (from `menu.py`) to select:
  - **1** → Solve the Water Jug Problem
  - **2** → Solve the Block World Problem
  - **Q** → Quit

### Solving Water Jug Problem
- User inputs jug capacities and target volume.
- BFS (`bfs()` function in `SearchAlgorithms.py`) finds the sequence of operations to achieve the target.

### Solving Block World
- User inputs block arrangement data.
- The planner uses either **A\*** or **Best-First Search** to organize the blocks into the desired configuration.

---

## 🛠 Installation Guide
1. Clone the repository.
2. Ensure you have **Python 3.x** installed.
3. Run:
   ```bash
   python main.py
   ```
4. No additional installations or environments are required!

---

## 📸 Screenshots
- Example Water Jug Problem solutions
  
![Screenshot 2025-04-27 at 8 48 17 PM](https://github.com/user-attachments/assets/32598dbc-332d-419c-aab5-5133d62c80eb)

- Example Block World arrangements

![Screenshot 2025-04-27 at 8 49 03 PM](https://github.com/user-attachments/assets/9bcde4b6-1002-4594-9fa0-a8ef28e612df)


---

## 📚 References
- [Blocks World (Wikipedia)](https://en.wikipedia.org/wiki/Blocks_world)
- [Water Pouring Puzzle (Wikipedia)](https://en.wikipedia.org/wiki/Water_pouring_puzzle)

---
