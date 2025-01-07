# Tower of Hanoi

This project contains two implementations of the Tower of Hanoi problem:

1. `iterative.py`: Solves the Tower of Hanoi problem using an iterative approach.
2. `recursion.py`: Solves the Tower of Hanoi problem using a recursive approach.

## Files

- `iterative.py`: Contains the iterative solution for the Tower of Hanoi problem.
- `recursion.py`: Contains the recursive solution for the Tower of Hanoi problem.

## How to Run

To run the iterative solution:

```bash
python iterative.py
```

To run the recursive solution:

```bash
python recursion.py
```

## Description

The Tower of Hanoi is a classic problem in computer science and mathematics. The objective is to move a stack of disks from one rod to another, following these rules:

1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or on an empty rod.
3. All disks start on one rod and must be moved to another rod, using a third rod as an auxiliary.

## Example

For a Tower of Hanoi problem with 3 disks:

- Move disk 1 from rod A to rod C
- Move disk 2 from rod A to rod B
- Move disk 1 from rod C to rod B
- Move disk 3 from rod A to rod C
- Move disk 1 from rod B to rod A
- Move disk 2 from rod B to rod C
- Move disk 1 from rod A to rod C
