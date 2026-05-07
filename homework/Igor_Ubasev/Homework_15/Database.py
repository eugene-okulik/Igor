import mysql.connector
from mysql.connector import Error


# Подключение к базе данных
def create_connection():
    try:
        conn = mysql.connector.connect(
            host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port=25060,
            user='st-onl',
            password='AVNS_tegPDkI5BlB2lW5eASC',
            database='st-onl'
        )
        return conn
    except Error as e:
        print(f"❌ Ошибка подключения: {e}")
        return None


# 1. Создание студента
def create_student(cursor, name, second_name, group_id=None):
    query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
    values = (name, second_name, group_id)
    cursor.execute(query, values)
    return cursor.lastrowid


# 2. Создание группы
def create_group(cursor, title, start_date, end_date):
    query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
    values = (title, start_date, end_date)
    cursor.execute(query, values)
    return cursor.lastrowid


# 3. Обновление группы студента
def update_student_group(cursor, student_id, group_id):
    query = "UPDATE students SET group_id = %s WHERE id = %s"
    values = (group_id, student_id)
    cursor.execute(query, values)


# 4. Создание книги
def create_book(cursor, title, taken_by_student_id=None):
    query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
    values = (title, taken_by_student_id)
    cursor.execute(query, values)
    return cursor.lastrowid


# 5. Создание предмета
def create_subject(cursor, title):
    query = "INSERT INTO subjects (title) VALUES (%s)"
    cursor.execute(query, (title,))
    return cursor.lastrowid


# 6. Создание занятия (урока)
def create_lesson(cursor, title, subject_id):
    query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
    values = (title, subject_id)
    cursor.execute(query, values)
    return cursor.lastrowid


# 7. Создание оценки
def create_mark(cursor, value, lesson_id, student_id):
    query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
    values = (value, lesson_id, student_id)
    cursor.execute(query, values)
    return cursor.lastrowid


# 8. Получение всех оценок студента
def get_student_marks(cursor, student_id):
    query = "SELECT value FROM marks WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    return cursor.fetchall()


# 9. Получение всех книг студента
def get_student_books(cursor, student_id):
    query = "SELECT title FROM books WHERE taken_by_student_id = %s"
    cursor.execute(query, (student_id,))
    return cursor.fetchall()


# 10. Полная информация о студенте (JOIN-запрос)
def get_full_student_info(cursor, student_id):
    query = """
        SELECT
            s.name AS 'Имя',
            s.second_name AS 'Фамилия',
            g.title AS 'Группа',
            b.title AS 'Книги',
            m.value AS 'Оценки',
            l.title AS 'Лекции',
            s2.title AS 'Предметы'
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON m.student_id = s.id
        LEFT JOIN lessons l ON l.id = m.lesson_id
        LEFT JOIN subjects s2 ON s2.id = l.subject_id
        WHERE s.id = %s
    """
    cursor.execute(query, (student_id,))
    return cursor.fetchall()


# ОСНОВНАЯ ПРОГРАММА
def main():
    conn = create_connection()
    if not conn:
        return

    cursor = conn.cursor()

    try:
        print("=" * 60)
        print("📚 НАЧАЛО РАБОТЫ С БАЗОЙ ДАННЫХ")
        print("=" * 60)

        # ===== 1. СОЗДАНИЕ СТУДЕНТА =====
        print("\n1️⃣ Создаём студента...")
        student_id = create_student(cursor, 'Ivan', 'Ivanov', None)
        conn.commit()
        print(f"   ✅ Студент создан с ID: {student_id}")

        # ===== 2. СОЗДАНИЕ КНИГ И ВЫДАЧА СТУДЕНТУ =====
        print("\n2️⃣ Создаём книги и выдаём студенту...")
        books = ['Маша и Медведь', 'Лиса и Петух', 'Три медведя']
        book_ids = []

        for book_title in books:
            book_id = create_book(cursor, book_title, student_id)
            book_ids.append(book_id)
            print(
                f"   ✅ Книга '{book_title}' создана с ID: {book_id}, "
                f"выдана студенту {student_id}"
            )

        conn.commit()

        # ===== 3. СОЗДАНИЕ ГРУППЫ =====
        print("\n3️⃣ Создаём группу...")
        group_id = create_group(cursor, 'Python Engineer', 'feb 2026', 'aug 2026')
        conn.commit()
        print(f"   ✅ Группа создана с ID: {group_id}")

        # ===== 4. ОПРЕДЕЛЯЕМ СТУДЕНТА В ГРУППУ =====
        print("\n4️⃣ Определяем студента в группу...")
        update_student_group(cursor, student_id, group_id)
        conn.commit()
        print(f"   ✅ Студент ID {student_id} определён в группу ID {group_id}")

        # ===== 5. СОЗДАНИЕ ПРЕДМЕТОВ =====
        print("\n5️⃣ Создаём учебные предметы...")
        subjects = ['Algebra', 'Geografic', 'Geometria']
        subject_ids = {}

        for subject_title in subjects:
            subject_id = create_subject(cursor, subject_title)
            subject_ids[subject_title] = subject_id
            print(f"   ✅ Предмет '{subject_title}' создан с ID: {subject_id}")

        conn.commit()

        # ===== 6. СОЗДАНИЕ ЗАНЯТИЙ ДЛЯ КАЖДОГО ПРЕДМЕТА =====
        print("\n6️⃣ Создаём занятия для каждого предмета...")

        lessons_data = [
            ('Algebra_1', 'Algebra'),
            ('Algebra_2', 'Algebra'),
            ('Geografic_1', 'Geografic'),
            ('Geografic_2', 'Geografic'),
            ('Geometria_1', 'Geometria'),
            ('Geometria_2', 'Geometria')
        ]

        lesson_ids = []

        for lesson_title, subject_title in lessons_data:
            subject_id = subject_ids[subject_title]
            lesson_id = create_lesson(cursor, lesson_title, subject_id)
            lesson_ids.append(lesson_id)
            print(
                f"   ✅ Занятие '{lesson_title}' создано с ID: {lesson_id} "
                f"(предмет: {subject_title})"
            )

        conn.commit()

        # ===== 7. ВЫСТАВЛЕНИЕ ОЦЕНОК СТУДЕНТУ =====
        print("\n7️⃣ Выставляем оценки студенту...")
        marks_values = [5, 3, 4, 2, 5, 4]

        for i, lesson_id in enumerate(lesson_ids):
            mark_id = create_mark(cursor, marks_values[i], lesson_id, student_id)
            print(
                f"   ✅ Оценка {marks_values[i]} за занятие ID {lesson_id} "
                f"создана с ID: {mark_id}"
            )

        conn.commit()

        # ===== 8. ВСЕ ОЦЕНКИ СТУДЕНТА =====
        print("\n8️⃣ Все оценки студента:")
        marks = get_student_marks(cursor, student_id)
        for mark in marks:
            print(f"   📊 Оценка: {mark[0]}")

        # ===== 9. ВСЕ КНИГИ СТУДЕНТА =====
        print("\n9️⃣ Все книги студента:")
        books_list = get_student_books(cursor, student_id)
        for book in books_list:
            print(f"   📖 Книга: {book[0]}")

        # ===== 10. ПОЛНАЯ ИНФОРМАЦИЯ О СТУДЕНТЕ (JOIN) =====
        print("\n🔟 Полная информация о студенте (JOIN-запрос):")
        print("-" * 80)

        full_info = get_full_student_info(cursor, student_id)

        if full_info:
            for row in full_info:
                print(f"   👤 Имя: {row[0]}")
                print(f"   📛 Фамилия: {row[1]}")
                print(f"   👥 Группа: {row[2]}")
                print(f"   📚 Книги: {row[3]}")
                print(f"   🎓 Оценки: {row[4]}")
                print(f"   📖 Лекции: {row[5]}")
                print(f"   📚 Предметы: {row[6]}")
                print("-" * 40)

        print("\n" + "=" * 60)
        print("✅ ВСЕ ОПЕРАЦИИ УСПЕШНО ВЫПОЛНЕНЫ!")
        print(f"📌 Итоговый ID студента: {student_id}")
        print(f"📌 ID группы: {group_id}")
        print("=" * 60)

    except Error as e:
        print(f"\n❌ Ошибка при выполнении запроса: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
        print("\n🔌 Соединение с базой данных закрыто.")


if __name__ == "__main__":
    main()
    