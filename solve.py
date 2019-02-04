import time

import main
import constants as ct
import tools

board = []
cycles = 0


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
    start_time = time.time()
    print('\nParsing grid and initializing variables...')

    values = values.replace('.', '0')

    for num in range(len(ct.cell_indexes)):
        new_cell = {}
        new_cell["index"] = ct.cell_indexes[num]
        new_cell["set"] = tools.get_set(ct.cell_indexes[num])
        new_cell["value"] = values[num]

        if values[num] is not '0':
            new_cell["possible_values"] = ['']
        else:
            new_cell["possible_values"] = [digit for digit in ct.digits]

        board.append(new_cell)

    constrain(board)
    display(board)

    end_time = time.time()
    print("Parsed grid in", (end_time - start_time), "seconds:")
    print(board)


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
    print('\n')


def enum_cycle():
    global cycles
    cycles = cycles + 1


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


def search(a_grid, dd=ct.draw_while_solve):
    if all(cell['value'] is not '0' for cell in a_grid):
        return True

    try_index = 0

    for cell in a_grid:
        if cell["value"] is '0':
            try_index = a_grid.index(cell)

    for value in a_grid[try_index]["possible_values"]:
        enum_cycle()

        if is_safe(a_grid, try_index, value):
            a_grid[try_index]["value"] = value
            # print("Safe value ", value, "at", a_grid[try_index]["index"])
            if dd is True:
                main.draw_frame()
            else:
                pass

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
