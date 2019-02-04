import cProfile
import pygame
import pygame.freetype

import tools
import colors
import solve
import constants as ct

DISPLAY = pygame.display.set_mode((ct.display_width, ct.display_height), pygame.HWSURFACE)
CLOCK = pygame.time.Clock()

def main():
    if ct.debug is True:
        pr = cProfile.Profile()
        pr.enable()

    global DISPLAY
    global CLOCK

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                if ct.debug is True:
                    pr.disable()
                    pr.dump_stats('profile.pstat')
            elif event.type == pygame.KEYDOWN:
                if event.key == 13:  # Enter key
                    print("Staring to solve...")
                    if solve.search(solve.board):
                        print("\n\nSolution found:")
                        solve.display(solve.board)
                        print("Grid solved in: {0} cycles".format(solve.cycles))
                    else:
                        print("\n\nCould not find a solution")

        draw_frame()


def draw_frame(screen=DISPLAY):
    screen.fill((0, 0, 0))

    fps_font = pygame.font.SysFont('Calibri', 24)
    fps = fps_font.render(str(int(CLOCK.get_fps())), False, colors.color('WHITE'))
    screen.blit(fps, (12, 12))

    for vline in tools.range1(0, 9):
        if vline % 3 == 0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.rect(screen,
                         colors.color('#FFFFFF'),
                         pygame.Rect(((ct.display_width / 9) * vline) - thickness, 0, thickness * 2, ct.display_height))

    for hline in tools.range1(0, 9):
        if hline % 3 == 0:
            thickness = 5
        else:
            thickness = 1
        pygame.draw.rect(screen,
                         colors.color('#FFFFFF'),
                         pygame.Rect(0, ((ct.display_width / 9) * hline) - thickness, ct.display_width, thickness * 2))

    for cell in solve.board:
        if cell['value'] is not '0':
            if len(cell['possible_values']) > 0 and cell['possible_values'][0] is not '':
                dvalue = cell['value']
                dcolor = '#88ade8'
            else:
                dvalue = cell['value']
                dcolor = 'WHITE'

            xpos = tools.safe_cast(cell["index"][1:], int) * (ct.display_width/9) - \
                   (ct.display_width/18) - 15
            ypos = ((tools.safe_cast(ord(cell["index"][:1]), int))-64) * (ct.display_height/9) - \
                   (ct.display_height/18) - 15
            tools.draw_text(screen=screen, text=dvalue, x=xpos, y=ypos, size=42, color=colors.color(dcolor))

    pygame.display.update()
    CLOCK.tick()

def pre_init():
    solve_grid = None
    print("Soduku Solver v3")

    with open("Grids.txt") as file:
        grids = [grid.rstrip('\n') for grid in file]

    for grid in grids:
        print("[{id}] {val}".format(id=grids.index(grid), val=grid))

    while solve_grid not in [grids.index(grid) for grid in grids]:
        solve_grid = tools.safe_cast(input("Choose a grid to solve: "), int)

    if len(grids[solve_grid]) is not 81:
        print("Invalid sudoku grid")
        exit()

    solve.parse(grids[solve_grid])


if __name__ == '__main__':
    pre_init()

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Sudoku")

    main()
