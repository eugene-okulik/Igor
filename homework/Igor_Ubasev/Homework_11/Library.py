class Book:
    def __init__(
            self,
            page_material,
            presence_of_text,
            book_title,
            author,
            number_of_pages,
            isbn,
            flag_reserved=False
    ):
        self.page_material = page_material
        self.presence_of_text = presence_of_text
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.flag_reserved = flag_reserved


book1 = Book(
    "бумага",
    True,
    "Война и мир",
    "Лев Толстой",
    1300,
    "978-5-699-12345-6",
    False
)
book2 = Book(
    "бумага",
    True,
    "Преступление и наказание",
    "Фёдор Достоевский",
    672,
    "978-5-699-54321-0",
    False
)
book3 = Book(
    "электронная",
    True,
    "Мастер и Маргарита",
    "Михаил Булгаков",
    480,
    "978-5-699-98765-4",
    False
)
book4 = Book(
    "бумага",
    True,
    "1984",
    "Джордж Оруэлл",
    328,
    "978-5-699-11111-1",
    False
)
book5 = Book(
    "аудио",
    True,
    "Гарри Поттер",
    "Дж.К. Роулинг",
    0,
    "978-5-699-22222-2",
    False
)
book6 = Book(
    "бумага",
    False,
    "Пустая тетрадь",
    "Неизвестен",
    96,
    "978-5-699-33333-3",
    True
)

books = [book1, book2, book3, book4, book5, book6]

for book in books:
    status = "зарезервирована" if book.flag_reserved else ""
    print(
        f"'Название: {book.book_title}', "
        f"'Автор: {book.author}', "
        f"'Страниц: {book.number_of_pages}', "
        f"'Материал: {book.page_material}', "
        f"{status}"
    )


class SchoolTextbook(Book):
    def __init__(
            self,
            book_title,
            author,
            number_of_pages,
            subject,
            school_class,
            availability_tasks,
            flag_reserved=False
    ):
        super().__init__(
            page_material=None,
            presence_of_text=None,
            book_title=book_title,
            author=author,
            number_of_pages=number_of_pages,
            isbn=None,
            flag_reserved=flag_reserved
        )
        self.subject = subject
        self.school_class = school_class
        self.availability_tasks = availability_tasks


textbook1 = SchoolTextbook(
    "Математика",
    "Иванов",
    200,
    "Математика",
    9,
    True,
    False
)
textbook2 = SchoolTextbook(
    "История",
    "Петров",
    300,
    "История",
    10,
    False,
    False
)
textbook3 = SchoolTextbook(
    "География",
    "Сидоров",
    400,
    "География",
    8,
    True,
    True
)
textbook4 = SchoolTextbook(
    "Геометрия",
    "Журавлев",
    500,
    "Геометрия",
    9,
    False,
    False
)

textbooks = [textbook1, textbook2, textbook3, textbook4]

for textbook in textbooks:
    status = "зарезервирована" if textbook.flag_reserved else ""
    print(
        f"'Название: {textbook.book_title}', "
        f"'Автор: {textbook.author}', "
        f"'Страниц: {textbook.number_of_pages}', "
        f"'Предмет: {textbook.subject}', "
        f"'Класс: {textbook.school_class}', "
        f"{status}"
    )
