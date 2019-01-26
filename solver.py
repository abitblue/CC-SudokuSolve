# Created by Ryan Yang

# Global Variables:

# Easy
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid2 = '020810740700003100090002805009040087400208003160030200302700060005600008076051090'

# Hard
grid3 = '38.6.......9.......2..3.51......5....3..1..6....4......17.5..8.......9.......7.32'

grid = []


def str_cross(values1, values2):
    return [value1 + value2 for value1 in values1 for value2 in values2]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
cell_indexes = str_cross(rows, cols)


def main():
    print("Sudoku Solver v1")

    solve_grid = grid2

    print('Solving grid:', solve_grid, "\n\n")
    parse(solve_grid)

    while not is_complete(grid):
        check_values(grid)
        print(grid)

    display(grid)


def parse(values):
    print('Parsing grid and initializing variables:')

    values = values.replace('.', '0')

    for num in range(len(cell_indexes)):
        new_cell = {}
        new_cell["index"] = cell_indexes[num]
        new_cell["set"] = get_set(cell_indexes[num])
        new_cell["value"] = values[num]

        if values[num] is not '0':
            new_cell["possible_values"] = ['']
        else:
            new_cell["possible_values"] = [digit for digit in digits]

        grid.append(new_cell)
    display(grid)
    print('\nParsed Grid:', grid)


def check_values(a_grid):
    for cell in a_grid:
        if cell["value"] is not '0':
            row = cell["index"][:1]
            col = cell["index"][1:]
            set_num = cell["set"]
            value = cell["value"]

            # Check Row:
            for item in a_grid:
                if row in item["index"]:
                    try:
                        item["possible_values"].remove(value)
                    except ValueError:
                        pass

            # Check Col:
            for item in a_grid:
                if col in item["index"]:
                    try:
                        item["possible_values"].remove(value)
                    except ValueError:
                        pass

            # Check Set:
            for item in a_grid:
                if set_num in item["set"]:
                    try:
                        item["possible_values"].remove(value)
                    except ValueError:
                        pass

        if len(cell["possible_values"]) == 1 and cell["value"] is '0':
            cell["value"] = str(cell["possible_values"][0])
            cell["possible_values"] = ['']


def is_complete(a_grid):
    num_incomplete = 0
    for item in a_grid:
        if item["value"] is '0':
            num_incomplete = num_incomplete + 1
    if num_incomplete == 0:
        return True
    else:
        print(num_incomplete)
        return False


def get_set(index):
    if index in str_cross('ABC', '123'): return '1'
    elif index in str_cross('ABC', '456'): return '2'
    elif index in str_cross('ABC', '789'): return '3'
    elif index in str_cross('DEF', '123'): return '4'
    elif index in str_cross('DEF', '456'): return '5'
    elif index in str_cross('DEF', '789'): return '6'
    elif index in str_cross('GHI', '123'): return '7'
    elif index in str_cross('GHI', '456'): return '8'
    elif index in str_cross('GHI', '789'): return '9'


def display(a_grid):
    for cell in a_grid:
        try:
            next_cell_row = a_grid[(a_grid.index(cell))+1]["index"][:1]
        except IndexError:
            pass

        current_cell_row = cell["index"][:1]
        col = cell["index"][1:]
        value = (cell["value"])

        if next_cell_row is 'I' and current_cell_row is 'A':
            next_cell_row = 'A'

        print(''.join(value).center(2) + ('| ' if col in '36' else '')\
              + ('\n' if next_cell_row is not current_cell_row else '')\
              + ('------+-------+------ \n' if (next_cell_row is not current_cell_row) and \
                                            (next_cell_row in 'DG') else ''), end='')


main()
