import sys
import pygame
import colors


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        print("Unexpected error:", sys.exc_info()[0])
        return default


def range1(start, end):
    return range(start, end + 1)


def draw_text(screen, text, x, y, size=36, color=colors.color('WHITE'), font_type='PressStart2P.ttf'):
    try:
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))
    except Exception as e:
        print("Unexpected error:", sys.exc_info()[0])
        raise e


def str_cross(values1, values2):
    return [value1 + value2 for value1 in values1 for value2 in values2]


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
