from enum import Enum


class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TEALBLUE = (136, 173, 232)


def color(color):
    if len(color) is 7 and color[0] is '#':
        scolor = color.lstrip('#')
        return tuple(int(scolor[i:i + 2], 16) for i in (0, 2, 4))
    else:
        return Colors[color].value
