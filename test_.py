import validate
import solve
import json
import os

def main():
    #fetching the sudoku
    path = os.path.abspath("sudoku.json")

    with open(path) as data_:
        data = json.load(data_)

    sudoku = data['sudoku']

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
        
def test_main():
  res = main()
  assert 'Sudoku valid. Solved:' in res
