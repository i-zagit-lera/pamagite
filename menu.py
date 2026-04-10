import pygame
import pygame_menu
import subprocess #из одного файла запускаем другой
import sys

from pygame_menu.examples.other.widget_positioning import my_theme
from pygame_menu.examples.simple import set_difficulty


def start_game():
    print('Игра началась')
selected_difficulty = "green" # переменная, где будет храниться выбранная сложность

def set_difficulty(value, difficulty): # функция вызывается при смене сложности
    global selected_difficulty # говорим, что будем менять глобальную переменную
    selected_difficulty = difficulty # сохраняем выбранную сложность
    print(selected_difficulty)

def start_the_game(): # функция запуска игры
    subprocess.Popen([sys.executable, "my_game.py", selected_difficulty]) # запускаем main.py и передаем туда сложность
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("меню")

my_theme = pygame_menu.themes.THEME_SOLARIZED.copy() #устанавливаем тему
my_theme.widget_margin = (0, 40)#расстояние между строк
menu = pygame_menu.Menu("добро пожаловать",500, 400, theme=my_theme)
menu.add.text_input("Введите имя: ", default='Егор')
menu.add.selector('Выбрать сложность: ', [('easy', "0"), ('medium', "1"), ('hard', "2")], onchange=set_difficulty)
menu.add.button('запустить', start_the_game)
menu.add.button('Выйти', pygame_menu.events.EXIT)
menu.mainloop(window)
