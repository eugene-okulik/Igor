import csv
import os
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv

# 1. Загрузка .env
env_path = Path(__file__).parent.parent / '.env'
if not env_path.exists():
    print(f"Файл .env не найден по пути {env_path}")
    exit(1)
load_dotenv(dotenv_path=env_path)

# 2. Подключение к БД
conn = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME')
)
cursor = conn.cursor(dictionary=True, buffered=True)

# 3. Поиск CSV-файла data.csv
project_root = Path(__file__).parent.parent
possible_paths = [
    project_root / 'homework' / 'eugene_okulik' / 'Lesson_16' / 'hw_data'
    / 'data.csv',
    project_root / 'Igor' / 'homework' / 'eugene_okulik' / 'Lesson_16'
    / 'hw_data' / 'data.csv',
    project_root / 'Igor' / 'homework' / 'eugene_okulik' / 'Lesson_16'
    / 'data.csv',
    project_root / 'homework' / 'eugene_okulik' / 'Lesson_16' / 'data.csv',
]

csv_file = None
for path in possible_paths:
    if path.exists() and path.is_file():
        csv_file = path
        break

if not csv_file:
    print("CSV файл 'data.csv' не найден. Проверьте пути:")
    for p in possible_paths:
        print(f"  - {p}")
    exit(1)

print(f"Найден CSV: {csv_file}")

# 4. Проверка заголовков CSV
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    expected_headers = {
        'name', 'second_name', 'group_title', 'book_title',
        'subject_title', 'lesson_title', 'mark_value'
    }
    actual_headers = set(reader.fieldnames)
    if not expected_headers.issubset(actual_headers):
        print("Ошибка: CSV-файл содержит неверные заголовки.")
        print(f"Ожидалось: {expected_headers}")
        print(f"Получено: {actual_headers}")
        exit(1)

# 5. Чтение и сравнение
missing = []
with open(csv_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Очистка ключей и значений от пробелов
        row = {k.strip(): v.strip() for k, v in row.items()}
        name = row['name']
        second_name = row['second_name']
        group_title = row['group_title']
        book_title = row['book_title']
        subject_title = row['subject_title']
        lesson_title = row['lesson_title']
        mark_value = row['mark_value']

        # 1. Найти студента
        cursor.execute(
            "SELECT id FROM students WHERE name = %s AND second_name = %s",
            (name, second_name)
        )
        student = cursor.fetchone()
        cursor.fetchall()
        if not student:
            missing.append(row)
            continue
        student_id = student['id']

        # 2. Проверить группу студента
        cursor.execute("""
            SELECT 1 FROM students s
            JOIN `groups` g ON s.group_id = g.id
            WHERE s.id = %s AND g.title = %s
        """, (student_id, group_title))
        group_exists = cursor.fetchone()
        cursor.fetchall()
        if not group_exists:
            missing.append(row)
            continue

        # 3. Проверить книгу студента
        cursor.execute(
            "SELECT 1 FROM books WHERE taken_by_student_id = %s AND title = %s",
            (student_id, book_title)
        )
        book_exists = cursor.fetchone()
        cursor.fetchall()
        if not book_exists:
            missing.append(row)
            continue

        # 4. Найти предмет
        cursor.execute(
            "SELECT id FROM subjects WHERE title = %s",
            (subject_title,)
        )
        subject = cursor.fetchone()
        cursor.fetchall()
        if not subject:
            missing.append(row)
            continue
        subject_id = subject['id']

        # 5. Найти урок
        cursor.execute(
            "SELECT id FROM lessons WHERE title = %s AND subject_id = %s",
            (lesson_title, subject_id)
        )
        lesson = cursor.fetchone()
        cursor.fetchall()
        if not lesson:
            missing.append(row)
            continue
        lesson_id = lesson['id']

        # 6. Проверить оценку
        cursor.execute(
            "SELECT 1 FROM marks WHERE student_id = %s AND lesson_id = %s "
            "AND value = %s",
            (student_id, lesson_id, mark_value)
        )
        mark_exists = cursor.fetchone()
        cursor.fetchall()
        if not mark_exists:
            missing.append(row)
            continue

# 6. Вывод результатов
if missing:
    print("В базе данных отсутствуют следующие строки из CSV:")
    for i, row in enumerate(missing, 1):
        print(f"{i}. {row}")
else:
    print("Все строки из CSV присутствуют в базе данных.")

cursor.close()
conn.close()
