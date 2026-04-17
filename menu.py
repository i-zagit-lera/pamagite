import pygame
import pygame_menu
import subprocess
import sys

def start_the_game():
    # Запускаем my_game.py и передаём выбранную сложность
    subprocess.Popen([sys.executable, "my_game.py", selected_difficulty])

def set_difficulty(value, difficulty):
    global selected_difficulty
    selected_difficulty = difficulty
    print(f"Сложность установлена: {selected_difficulty}")

# Инициализация Pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Меню")

# Тема меню
my_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
my_theme.widget_margin = (0, 40)

# Создаём меню
menu = pygame_menu.Menu("Добро пожаловать", 500, 400, theme=my_theme)

# Поле ввода имени
menu.add.text_input("Введите имя: ", default='Егор')

# Селектор сложности – значения передаются как строки
menu.add.selector(
    'Выбрать сложность: ',
    [('easy', "0"), ('medium', "1"), ('hard', "2")],
    onchange=set_difficulty,
    default=0  # устанавливаем первый пункт как выбранный по умолчанию
)

# Кнопка запуска игры
menu.add.button('Запустить', start_the_game)
menu.add.button('Выйти', pygame_menu.events.EXIT)

# Явно установим начальное значение сложности (чтобы переменная была определена)
selected_difficulty = "0"   # соответствует 'easy'
set_difficulty(None, "0")   # инициализируем глобальную переменную

# Запуск цикла меню
menu.mainloop(window)
