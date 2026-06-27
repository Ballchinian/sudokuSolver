# Sudoku

A Sudoku solver that fills in a grid by elimination. It looks at every empty square, rules out anything already used in the same row, column, or 3×3 box, and whenever that leaves a square with exactly one number it could be, it drops that number in — then goes round again until nothing else can be pinned down.

## How it works

It solves the way you'd do the easy ones by hand. Three checks do the work: the row check strips out every number already sitting in that row, the column check does the same down the column, and the box check walks back to the top-left corner of the square's 3×3 block and clears out everything already in there. Run a square through all three and you're left with the numbers it could still legally be.

A square with a single candidate left is a certainty, so it gets filled in, and filling it in can hand you new certainties elsewhere, so the whole grid is swept again and again until a full pass changes nothing.

It only ever fills the dead certainties, though. It never guesses. So it'll finish any puzzle that can be cracked by elimination alone and stall on the harder ones that need a leap. If it stalls, you get the grid back with as much filled in as it could manage, rather than an error.

## Input

The puzzle is a 9×9 grid: a list of nine rows, each a list of nine numbers, with `0` for a blank. It's solved in place, and the same grid is handed back.

```python
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
```

## Running it

A single function with no dependencies, so any Python 3 will do.

```python
sudoku(puzzle)   # fills the blanks in place and returns the grid
```
