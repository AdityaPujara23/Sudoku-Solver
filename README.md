# Sudoku-Solver
Algorithms which validate a 9x9 Sudoku Puzzle and solve it. Developed in Python3.

# Usage
## Convert Sudoku
* Convert your Sudoku into an array list as follows:

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

to:

``[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]``

## Place your Sudoku as the one to solved
* Clone this repository using:
``git clone https://github.com/AdityaPujara23/Sudoku-Solver.git``

* Change your directory in the terminal to the downloaded repo

* Copy your converted Sudoku to the following file:
``valandsolve.py``

where it states:
``sudoku = [["5","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]``

change this to:
``sudoku = //your converted sudoku//``

where ``//your converted sudoku`` is the sudoku you wish to solve!

## Watch the magic take place!
* Run the following command to validate and solve the sudoku:
```python3 valandsolve.py```
* If your Sudoku is valid, it will present the solution on the screen!
