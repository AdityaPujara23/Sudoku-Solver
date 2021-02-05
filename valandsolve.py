import validate
import solve

def main():
    #example sudoku (to change this to another sudoku, copy your list of lists sudoku here by replacing the existing list of lists)
    sudoku = [["5","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]

    # validate the sudoku
    validation = (validate.run(sudoku)).Validate()
    if validation is False:
        print("Sudoku is invalid.")
    else:
        print("Sudoku valid. Solved:")
        solve.solve(sudoku)
        for list_ in sudoku:
            print(list_)
        return
main()
