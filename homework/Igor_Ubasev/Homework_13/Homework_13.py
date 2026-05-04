import re
from datetime import datetime, timedelta


def process_dates_from_file(file_path):
    """
    Читает файл, парсит даты и выполняет действия из каждой строки
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # Пропускаем пустые строки
        if not line.strip():
            continue

        # Разделяем строку на части: номер с датой и описание
        # Формат: "1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже"
        parts = line.strip().split(' - ')
        if len(parts) != 2:
            continue

        number_with_date = parts[0]  # "1. 2023-11-27 20:34:13.212967"
        # description = parts[1]  # УДАЛЕНО: переменная не использовалась

        # Извлекаем номер и дату
        # Номер заканчивается на точку, поэтому split('. ', 1) - разделяем по точке с пробелом
        number_str, date_str = number_with_date.split('. ', 1)
        number = int(number_str)

        # Преобразуем строку в объект datetime с микросекундами
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        # Выполняем действие в зависимости от номера
        if number == 1:
            # "распечатать эту дату, но на неделю позже"
            week_later = date_obj + timedelta(weeks=1)
            print(f"Дата №{number}: {date_str}")
            print(f"Дата на неделю позже: {week_later.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

        elif number == 2:
            # "распечатать какой это будет день недели"
            weekday = date_obj.strftime("%A")
            weekdays_ru = {
                'Monday': 'Понедельник',
                'Tuesday': 'Вторник',
                'Wednesday': 'Среда',
                'Thursday': 'Четверг',
                'Friday': 'Пятница',
                'Saturday': 'Суббота',
                'Sunday': 'Воскресенье'
            }
            print(f"Дата №{number}: {date_str}")
            print(f"День недели: {weekdays_ru.get(weekday, weekday)}")

        elif number == 3:
            # "распечатать сколько дней назад была эта дата"
            now = datetime.now()
            days_ago = (now - date_obj).days
            print(f"Дата №{number}: {date_str}")
            print(f"Эта дата была {days_ago} дней назад")

        print("-" * 50)


if __name__ == "__main__":
    # Используем относительный путь к файлу
    file_path = r'D:\AutoTest\Projects\Igor\homework\eugene_okulik\hw_13\data.txt'
    process_dates_from_file(file_path)
