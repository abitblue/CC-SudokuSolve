# CC-SudokuSolve

## Overview
- Solves sudoku grid
- Made for a showcase
- Code will not be maintained

## Requirements:
- pygame

## Usage:
##### Start Up Guide
- Run main.py and choose a grid to solve
- Press enter in the window to start solving

##### Settings
- Edit file `constants.py`:
    * `draw_while_solve = True`
        * If true, allows drawing of the grid while the grid is solved
    * `debug = True`
        * If true, creates a `profile.pstat` cProfile file upon closing the program using the proper close button

## TODO:
- Optimize `solve.py:81(is_safe)`
- Change data structure to numpy array
- Implement multiprocessing support so solving is not bottlenecked by window's FPS