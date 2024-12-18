from collections import defaultdict


keylout_shift = {
    'lfi5': [('~', '!'), ('$','%')],
    'lfi4': [('@'), ('7')],
    'lfi3': [('#'), ('5')],
    'lfi2': [('$', '%'), ('3','1')],
    'rfi2': [('^', '&'), ('9','0')],
    'rfi3': [('*'), ('2')],
    'rfi4': [('('), ('4')],
    'rfi5': [(')', '_', '+'),
             ('6', '8', '#')]
        }

keylout_dd = {
    'lfi5': [('ё', '1', 'й', 'ф', 'я'),
             ('$', '%', 'б', 'ч', 'ш')],
    'lfi4': [('2', 'ц', 'ы', 'ч'), ('[', 'ы', 'и', 'х')],
    'lfi3': [('3', 'у', 'в', 'с'), ('{', 'о', 'е', 'й')],
    'lfi2': [('4', 'к', 'а', 'м', '5', 'е', 'п', 'и'),
             ('}', '(', 'у', 'а', 'к', 'ь', ',', '_')],
    'lfi1': [(' '), (' ')],
    'rfi2': [('6', 'н', 'р', 'т', '7', 'г', 'о', 'ь'),
             ('=', 'ё', '.', '/', '*', '^', 'н', 'р')],
    'rfi3': [('8', 'ш', 'л', 'б'), (')', 'д', 'т', 'м')],
    'rfi4': [('9', 'щ', 'д', 'ю'), ('+', 'я', 'с', 'ф')],
    'rfi5': [('0', 'з', 'ж', '?', '-', 'х', 'э', '=', 'ъ', '\\'),
             (']', 'г', 'в', 'п', '!', 'ж', 'з', 'щ', 'ц', 'ъ')]
    }

def load_text(filename):
    """
    Загружает текст из файла и возвращает его в виде строки.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def analyze_finger_loads(text, keylout_dd, keylout_shift):
    """
    Подсчитывает нагрузку на каждый палец на основе текста и раскладок клавиатуры.

    Параметры:
    - text: строка текста, для которой производится анализ.
    - keylout_dd: словарь, где ключи — названия пальцев, а значения — списки символов, доступных для каждого пальца в раскладках ЙЦУКЕН и ВЫЗОВ.
                  Каждое значение представляет собой список с двумя вложенными списками:
                  первый — символы для ЙЦУКЕН, второй — для ВЫЗОВ.
    - keylout_shift: словарь, где ключи — названия пальцев, а значения — списки символов, которые используются при зажатой клавише Shift
                     для раскладок ЙЦУКЕН и ВЫЗОВ.

    Возвращает:
    - два словаря, где ключи — пальцы, а значения — суммарное количество нажатий для каждого пальца на основе текста:
      - finger_loads_ycu: словарь для раскладки ЙЦУКЕН
      - finger_loads_vyzov: словарь для раскладки ВЫЗОВ
    """
    finger_loads_ycu = defaultdict(int)  # Для ЙЦУКЕН
    finger_loads_vyzov = defaultdict(int)  # Для ВЫЗОВ

    # Объединение символов с их частотами
    symbol_counts = analyze_text_symbols(text, keylout_dd, keylout_shift)

    # Распределение символов по пальцам для обеих раскладок
    for finger, layouts in keylout_dd.items():
        # Если для пальца есть только одна раскладка, то добавляем пустую раскладку для второй
        if len(layouts) == 1:
            symbols_ycu = layouts[0]
            symbols_vyzov = []
        else:
            symbols_ycu, symbols_vyzov = layouts

        # Считаем частоты для каждой раскладки
        for symbol in symbols_ycu:
            finger_loads_ycu[finger] += symbol_counts.get(symbol, 0)
        for symbol in symbols_vyzov:
            finger_loads_vyzov[finger] += symbol_counts.get(symbol, 0)

    return finger_loads_ycu, finger_loads_vyzov

def analyze_text_symbols(text, keylout_dd, keylout_shift):
    """
    Подсчитывает количество нажатий для каждого символа на основе текста и раскладок клавиатуры.

    Параметры:
    - text: строка текста, для которой производится подсчет частот символов.
    - keylout_dd: словарь, где ключи — названия пальцев, а значения — списки символов, доступных для каждого пальца в раскладках ЙЦУКЕН и ВЫЗОВ.
                  Каждое значение представляет собой список с двумя вложенными списками:
                  первый — символы для ЙЦУКЕН, второй — для ВЫЗОВ.
    - keylout_shift: словарь, где ключи — названия пальцев, а значения — списки символов, которые используются при зажатой клавише Shift
                     для раскладок ЙЦУКЕН и ВЫЗОВ.

    Возвращает:
    - symbol_counts: словарь, где ключи — символы, а значения — количество нажатий каждого символа на основе текста.
    """
    symbol_counts = defaultdict(int)

    # Создание множества всех символов из раскладки для быстрого поиска
    all_keys = set(key for groups in keylout_dd.values() for group in groups for key in group)
    shift_keys = set(key for groups in keylout_shift.values() for group in groups for key in group)

    # Пройтись по каждому символу текста и обновить счетчики
    for char in text:
        if char in all_keys or char in shift_keys:
            symbol_counts[char] += 1

    return symbol_counts


def call():
    # Загрузка текста из файла
    text = load_text("voina-i-mir.txt")

    # Анализ нагрузки на пальцы
    finger_loads_ycu, finger_loads_vyzov = analyze_finger_loads(text, keylout_dd, keylout_shift)

    return finger_loads_vyzov