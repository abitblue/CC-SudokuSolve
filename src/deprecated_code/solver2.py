import time

                                                                                            # Cycles        Secs
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300' # 1887          0.0526
grid2 = '020810740700003100090002805009040087400208003160030200302700060005600008076051090' # 110           0.00563

# Hard
grid3 = '38.6.......9.......2..3.51......5....3..1..6....4......17.5..8.......9.......7.32' # 3315272       82.5
grid4 = '8..7....4.5....6............3.97...8....43..5....2.9....6......2...6...7.71..83.2' # 517638        12.1
grid5 = '....75....1..2.....4...3...5.....3.2...8...1.......6.....1..48.2........7........' # 28232878      723

# Hardest
grid6 = '..53.....8......2..7..1.5..4....53...1..7...6..32...8..6.5....9..4....3......97..' # 267667        7.72

# Global Variables
def str_cross(values1, values2):
    return [value1 + value2 for value1 in values1 for value2 in values2]


solve_grid = grid6
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
cell_indexes = str_cross(rows, cols)
board = []
cycles = 0


def main():
    print("Sudoku Solver v2")
    print('Solving grid:', solve_grid, "\n\n")

    start_time = time.time()

    parse(solve_grid)

    print("Solving....")

    if search(board):
        print("\n\nSolution found:")
        display(board)
    else:
        print("\n\nCould not find a solution")

    end_time = time.time()
    print("Grid solved in", (end_time - start_time), "seconds.")
    print("Cycles:", cycles)


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
    print('\n')

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
    print('\n')


def constrain(a_grid):
    for cell in a_grid:
        if cell["value"] is not '0':
            row = cell["index"][:1]
            col = cell["index"][1:]
            set_num = cell["set"]
            value = cell["value"]

            # Check Row, Col, and Set:
            for item in a_grid:
                if row in item["index"] or col in item["index"] or set_num in item["set"]:
                    try:
                        item["possible_values"].remove(value)
                    except ValueError:
                        pass


def parse(values):
    print('Parsing grid and initializing variables:')
    start_time = time.time()
    values = values.replace('.', '0')

    if len(values) is not 81:
        print("Invalid sudoku grid")
        exit()

    for num in range(len(cell_indexes)):
        new_cell = {}
        new_cell["index"] = cell_indexes[num]
        new_cell["set"] = get_set(cell_indexes[num])
        new_cell["value"] = values[num]

        if values[num] is not '0':
            new_cell["possible_values"] = ['']
        else:
            new_cell["possible_values"] = [digit for digit in digits]

        board.append(new_cell)

    constrain(board)
    display(board)

    possibilities = 1
    for cell in board:
        if cell["possible_values"][0] is not '':
            possibilities *= len(cell["possible_values"])

    end_time = time.time()
    print("Parsed grid in", (end_time - start_time), "seconds:")
    print("Number of board possibilities:", "{:.2e}".format(possibilities))
    print(board)


def is_safe(a_grid, try_index, value):
    safe = True

    for cell in a_grid:
        cell_row = cell["index"][:1]
        cell_col = cell["index"][1:]
        cell_set = cell["set"]

        if (cell_row in a_grid[try_index]["index"]) \
                or (cell_col in a_grid[try_index]["index"]) \
                or (cell_set in a_grid[try_index]["set"]):
            if value in cell["value"]:
                safe = False

    return safe


def enum_cycle():
    global cycles
    cycles = cycles + 1


def search(a_grid):
    if all(cell['value'] is not '0' for cell in a_grid):
        return True

    try_index = 0

    for cell in a_grid:
        if cell["value"] is '0':
            try_index = a_grid.index(cell)

    for value in a_grid[try_index]["possible_values"]:
        enum_cycle()

        if is_safe(a_grid, try_index, value):

            #print("Safe value ", value, "at", a_grid[try_index]["index"])
            a_grid[try_index]["value"] = value

            if search(a_grid):
                return True
            else:
                #print("Failure with", value, "at", a_grid[try_index]["index"], ", Position", try_index)
                pass

            a_grid[try_index]["value"] = '0'
        else:
            #print("Unsafe value ", value, "at", a_grid[try_index]["index"])
            pass

    return False


main()
