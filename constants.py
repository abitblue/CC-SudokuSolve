from src.utils import tools

display_height = 720
display_aspect = 1
display_width = int(display_height * display_aspect)

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
cell_indexes = tools.str_cross(rows, cols)

draw_while_solve = True
debug = False
