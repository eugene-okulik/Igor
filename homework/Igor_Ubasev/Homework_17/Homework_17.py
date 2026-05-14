import argparse
import os
import re

# Попробуем подключить colorama для цветного вывода
try:
    from colorama import Fore, Style, init

    init(autoreset=True)
    COLOR_SUPPORT = True
except ImportError:
    COLOR_SUPPORT = False

# Регулярное выражение для строки, начинающейся с времени
TIMESTAMP_PATTERN = re.compile(
    r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[,.]\d{3}'
)


def collect_files(path):
    """Собрать все файлы из папки или вернуть один файл."""
    if os.path.isfile(path):
        return [path]
    elif os.path.isdir(path):
        files = []
        for entry in os.listdir(path):
            full = os.path.join(path, entry)
            if os.path.isfile(full):
                files.append(full)
        return files
    else:
        raise ValueError(f"Путь не существует: {path}")


def parse_blocks(filepath):
    """Разобрать файл на блоки с метаданными."""
    blocks = []
    current_block = None
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line_no, line in enumerate(f, start=1):
            if TIMESTAMP_PATTERN.match(line):
                # Начинается новый блок
                if current_block is not None:
                    blocks.append(current_block)
                current_block = {
                    'time': line.strip(),
                    'start_line': line_no,
                    'lines': [line]
                }
            else:
                if current_block is not None:
                    current_block['lines'].append(line)
                else:
                    # Самые первые строки файла без временной метки –
                    # начинаем блок с пометкой "NO_TIMESTAMP"
                    current_block = {
                        'time': 'NO_TIMESTAMP',
                        'start_line': line_no,
                        'lines': [line]
                    }
        if current_block is not None:
            blocks.append(current_block)
    return blocks


def find_context(block_text, search_word):
    """
    Вернуть контекст найденного слова: слова до и после,
    а также позицию для вычисления номера строки.
    """
    idx = block_text.find(search_word)
    if idx == -1:
        return None

    words = block_text.split()
    # Найдём индекс слова, содержащего искомую подстроку
    word_index = None
    for i, w in enumerate(words):
        if search_word in w:
            word_index = i
            break
    if word_index is None:
        return None

    # Берём по 5 слов до и после
    start = max(0, word_index - 5)
    end = min(len(words), word_index + 6)  # +6: слово + 5 после
    context_words = words[start:end]

    # Подсветка найденного слова
    highlighted_context = []
    for i, w in enumerate(context_words):
        if search_word in w and i == (word_index - start):
            if COLOR_SUPPORT:
                highlighted_context.append(
                    f"{Fore.YELLOW}{w}{Style.RESET_ALL}"
                )
            else:
                highlighted_context.append(f"**{w}**")
        else:
            highlighted_context.append(w)

    context_str = ' '.join(highlighted_context)

    return {
        'context': context_str,
        'word_index_in_block': word_index,
        'start': start,
        'end': end
    }


def main():
    parser = argparse.ArgumentParser(
        description='Поиск ошибок в логах по ключевому слову'
    )
    parser.add_argument(
        'path', help='Путь к папке или файлу с логами'
    )
    parser.add_argument(
        '--text', required=True, help='Текст для поиска'
    )
    parser.add_argument(
        '--first', action='store_true',
        help='Вывести только первое совпадение'
    )
    args = parser.parse_args()

    try:
        files = collect_files(args.path)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    if not files:
        print("Файлы не найдены.")
        return

    found_any = False
    for filepath in files:
        blocks = parse_blocks(filepath)
        for block in blocks:
            # Собираем весь текст блока в одну строку для контекстного поиска
            block_text = ' '.join(
                line.strip() for line in block['lines']
            )
            if args.text not in block_text:
                continue

            # Ищем контекст
            result = find_context(block_text, args.text)
            if not result:
                continue

            # Определяем точную строку, где находится слово
            target_word_global_index = (
                    result['start']
                    + (result['word_index_in_block'] - result['start'])
            )
            cumulative_words = 0
            found_line = block['start_line']
            for i, line in enumerate(block['lines']):
                words_in_line = len(line.split())
                if cumulative_words + words_in_line > target_word_global_index:
                    found_line = block['start_line'] + i
                    break
                cumulative_words += words_in_line
            else:
                found_line = (
                        block['start_line'] + len(block['lines']) - 1
                )  # последняя строка блока

            # Вывод результата
            print(f"Файл: {filepath}")
            print(f"Время ошибки: {block['time']}")
            print(f"Строка: {found_line}")
            print(f"Контекст: {result['context']}")
            print("-" * 60)

            found_any = True
            if args.first:
                return

    if not found_any:
        print(f"Текст '{args.text}' не найден ни в одном файле.")


if __name__ == '__main__':
    main()
