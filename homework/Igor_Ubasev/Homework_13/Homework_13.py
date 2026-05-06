from datetime import datetime, timedelta
from pathlib import Path


def find_data_file():
    """Автоматически находит файл data.txt в репозитории"""
    script_dir = Path(__file__).parent

    # Пробуем разные варианты
    candidates = [
        script_dir / 'homework' / 'eugene_okulik' / 'hw_13' / 'data.txt',
        script_dir.parent / 'homework' / 'eugene_okulik' / 'hw_13' / 'data.txt',
        Path.cwd() / 'homework' / 'eugene_okulik' / 'hw_13' / 'data.txt',
    ]

    for path in candidates:
        if path.exists():
            print(f"✅ Файл найден: {path}")
            return path

    # Поднимаемся вверх в поисках папки homework
    current = script_dir
    for _ in range(10):
        if (current / 'homework').exists():
            found = current / 'homework' / 'eugene_okulik' / 'hw_13' / 'data.txt'
            print(f"✅ Файл найден: {found}")
            return found
        current = current.parent

    raise FileNotFoundError(
        f"\n❌ Файл не найден!\n"
        f"Искали в:\n  {candidates[0]}\n  {candidates[1]}\n  {candidates[2]}\n"
        f"\nТекущая директория: {Path.cwd()}\n"
        f"Директория скрипта: {script_dir}\n"
        f"\nФайл должен лежать здесь: homework/eugene_okulik/hw_13/data.txt"
    )


def process_dates_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if not line.strip():
            continue

        parts = line.strip().split(' - ')
        if len(parts) != 2:
            continue

        number_with_date = parts[0]
        description = parts[1]

        number_str, date_str = number_with_date.split('. ', 1)
        number = int(number_str)

        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        if number == 1:
            week_later = date_obj + timedelta(weeks=1)
            print(f"Дата №{number}: {date_str}")
            print(f"Действие: {description}")
            print(f"Дата на неделю позже: {week_later.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
            print(f"Проверка: {date_obj} + 7 дней = {week_later}")

        elif number == 2:
            weekday = date_obj.strftime("%A")
            weekdays_ru = {
                'Monday': 'Понедельник', 'Tuesday': 'Вторник',
                'Wednesday': 'Среда', 'Thursday': 'Четверг',
                'Friday': 'Пятница', 'Saturday': 'Суббота', 'Sunday': 'Воскресенье'
            }
            print(f"Дата №{number}: {date_str}")
            print(f"Действие: {description}")
            print(f"День недели: {weekdays_ru.get(weekday, weekday)}")

        elif number == 3:
            now = datetime.now()
            days_ago = (now - date_obj).days
            print(f"Дата №{number}: {date_str}")
            print(f"Действие: {description}")
            print(f"Сейчас: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Эта дата была {days_ago} дней назад")

        print("-" * 50)


if __name__ == "__main__":
    try:
        file_path = find_data_file()
        process_dates_from_file(str(file_path))
    except FileNotFoundError as e:
        print(e)
        