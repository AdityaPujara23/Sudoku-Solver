import validate.py
import solve.py

def main():
    #import sudoku
    sudoku = input("Enter the sudoku to validate and solve:")

    # validate the sudoku
    if Validate(sudoku) is False:
        print("Sudoku is invalid.")
    else:
        return solve(sudoku)
