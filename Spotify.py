import sys
import os
import keyboard  # Импортируем модуль keyboard
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMessageBox


# Путь к папке и конфигурационному файлу
config_dir = r"C:\err"
config_file = os.path.join(config_dir, "config.txt")

if hasattr(sys, '_MEIPASS'):
    # Путь к плагинам для скомпилированного файла
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(sys._MEIPASS, 'platforms')

# Проверяем наличие папки и создаем её, если не существует
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# Если конфигурационный файл не существует, создаем его с дефолтным текстом
if not os.path.exists(config_file):
    default_config = "Ошибка параметров индексирования.\nОбратитесь к разработчику программы."
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(default_config)

# Функция для чтения текста ошибки из конфиг-файла
def read_error_message():
    with open(config_file, "r", encoding="utf-8") as f:
        error_message = f.read().strip()
    return error_message

# Функция для отображения окна ошибки
def show_error_window():
    app = QApplication(sys.argv)
    
    # Читаем текст ошибки из конфиг-файла
    error_message = read_error_message()

    # Создаем диалоговое окно с типом ошибки
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setWindowTitle("Ошибка")
    msg.setText(error_message)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    
    # Показываем окно ошибки
    msg.exec()

# Функция для отслеживания горячих клавиш
def detect_shortcut():
    while True:
        if keyboard.is_pressed('ctrl+win+alt'):
            show_error_window()

if __name__ == '__main__':
    detect_shortcut()
