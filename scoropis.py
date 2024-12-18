import matplotlib.pyplot as plt
import itertools
import math
import os
from collections import defaultdict
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Создание окна для выбора файла
def get_file_path():
    Tk().withdraw()  # Скрыть главное окно
    return askopenfilename(title="Выберите текстовый файл", filetypes=[("Text files", "*.txt")])


def process_word(finger_mapping, word, finger_counts, var):
    right_side = ''.join(value for key, value in finger_mapping.items() if key.startswith('Правый'))
    left_side = ''.join(value for key, value in finger_mapping.items() if key.startswith('Левый'))

    for char in word:
        if char.isupper():  # Если заглавная буква
            if char.lower() in left_side:
                finger_counts['Левый мизинец'] += 1
            elif char.lower() in right_side:
                finger_counts['Правый мизинец'] += 1
            char = char.lower()  # Приводим к нижнему регистру для дальнейшей обработки

        if var == 1:
            if char in '02345':
                finger_counts['Левый мизинец'] += 1  # (Shift)
            if char in '16789':
                finger_counts['Правый мизинец'] += 1  # (Shift)

        if var == 2:
            if char in '!"№;%:':
                finger_counts['Левый мизинец'] += 1  # (Shift)
            if char in '&*()?':
                finger_counts['Правый мизинец'] += 1  # (Shift)

        if var == 3:
            if char in ';-"()-+':
                finger_counts['Левый мизинец'] += 1  # (Shift)
            if char in 'ъ№%?!:':
                finger_counts['Правый мизинец'] += 1  # (Shift)

        for finger, chars in finger_mapping.items():
            if char in chars:
                finger_counts[finger] += 1


def process_file(finger_mapping, file_path, var):
    # Инициализация счетчика нажатий
    finger_counts = defaultdict(int)
    finger_counts['Правый мизинец'] = -1  # Начальное значение для правого мизинца

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            finger_counts['Правый мизинец'] += 1  # Фиксируем переход на следующую строку (Enter)
            line = line.strip()  # Удаляем пробелы в начале и в конце
            if not line:
                continue  # Пропускаем строку, если она пустая

            # Разделяем строку на слова и обрабатываем каждое слово
            words = line.split()
            for word in words:
                process_word(finger_mapping, word, finger_counts, var)
                finger_counts['Левый большой'] += 1
    print(list(finger_counts.values()))
    return list(finger_counts.values())


finger_scoropis = {
    'Левый указательный': '?!.,аоыю45',
    'Левый средний': 'ъяех3',
    'Левый безымянный': 'ёьиэ2',
    'Левый мизинец': '.*йуф1',
    'Правый указательный': '-звлнбм67',
    'Правый средний': 'кт\'с8',
    'Правый безымянный': '(дсг9',
    'Правый мизинец': ')-«чшщрйж\"0'
}
