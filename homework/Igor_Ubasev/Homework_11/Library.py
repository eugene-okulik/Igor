class Book:
    def __init__(self, page_material, presence_of_text, book_title, author, number_of_pages, isbn, flag_reserved=False):
        self.page_material = page_material
        self.presence_of_text = presence_of_text
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.flag_reserved = flag_reserved


book1 = Book("бумага", True, "Война и мир", "Лев Толстой", 1300, "978-5-699-12345-6", False)
book2 = Book("бумага", True, "Преступление и наказание", "Фёдор Достоевский", 672, "978-5-699-54321-0", False)
book3 = Book("электронная", True, "Мастер и Маргарита", "Михаил Булгаков", 480, "978-5-699-98765-4", False)
book4 = Book("бумага", True, "1984", "Джордж Оруэлл", 328, "978-5-699-11111-1", False)
book5 = Book("аудио", True, "Гарри Поттер", "Дж.К. Роулинг", 0, "978-5-699-22222-2", False)
book6 = Book("бумага", False, "Пустая тетрадь", "Неизвестен", 96, "978-5-699-33333-3", True)

books = [book1, book2, book3, book4, book5, book6]
for book in books:
    status = "зарезервирована" if book.flag_reserved else ""
    print(
        f"'Название: {book.book_title}', 'Автор: {book.author}', 'Страниц:{book.number_of_pages}', 'Материал:{book.page_material}', {status}")


class School_textbooks(Book):
    def __init__(self, book_title, author, number_of_pages, subject, school_class, availability_tasks,
                 flag_reserved=False):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.subject = subject
        self.school_class = school_class
        self.availability_tasks = availability_tasks
        self.flag_reserved = flag_reserved


textbook = School_textbooks("Математика", "Иванов", 200, "Математика", 9, True, False)
textbook2 = School_textbooks("История", "Петров", 300, "История", 10, False, False)
textbook3 = School_textbooks("География", "Сидоров", 400, "География", 8, True, True)
textbook4 = School_textbooks("Геометрия", "Журавлев", 500, "Геометрия", 9, False, False)
textbook1 = [textbook, textbook2, textbook3, textbook4]
for textbooks in textbook1:
    status = "зарезервирована" if textbooks.flag_reserved else ""
    print(
        f"'Название: {textbooks.book_title}', 'Автор: {textbooks.author}', 'Страниц:{textbooks.number_of_pages}', 'Предмет:{textbooks.subject}', 'Класс:{textbooks.school_class}', {status}")
