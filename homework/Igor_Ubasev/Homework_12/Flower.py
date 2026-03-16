class Flower:
    """Базовый класс для всех цветов"""

    def __init__(self, name, color, stem_length, cost, freshness, lifetime):
        self.name = name  # Название вида (Роза, Тюльпан...)
        self.color = color  # Цвет
        self.stem_length = stem_length  # Длина стебля (см)
        self.cost = cost  # Стоимость
        self.freshness = freshness  # Свежесть (0-100%)
        self.lifetime = lifetime  # Время жизни (дней)

    def __repr__(self):
        return (
            f"{self.name}({self.color}, {self.stem_length}см, "
            f"{self.cost}₽, {self.freshness}%, {self.lifetime}дн.)"
        )


class Rose(Flower):
    """Класс Роза"""

    def __init__(self, color, stem_length, cost, freshness):
        # Розы обычно живут 5 дней
        super().__init__("Роза", color, stem_length, cost, freshness, lifetime=5)


class Tulip(Flower):
    """Класс Тюльпан"""

    def __init__(self, color, stem_length, cost, freshness):
        # Тюльпаны обычно живут 7 дней
        super().__init__("Тюльпан", color, stem_length, cost, freshness, lifetime=7)


class Orchid(Flower):
    """Класс Орхидея"""

    def __init__(self, color, stem_length, cost, freshness):
        # Орхидеи живут долго, около 14 дней
        super().__init__("Орхидея", color, stem_length, cost, freshness, lifetime=14)


class Bouquet:
    """Класс Букет, хранящий список цветов"""

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        """Добавить цветок в букет"""
        self.flowers.append(flower)

    def get_total_cost(self):
        """Вычислить общую стоимость букета"""
        return sum(flower.cost for flower in self.flowers)

    def get_wilting_time(self):
        """
        Определить время увядания букета
        (среднее время жизни цветов)
        """
        if not self.flowers:
            return 0
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        return round(total_lifetime / len(self.flowers), 2)

    def sort_flowers(self, parameter):
        """
        Сортировка цветов в букете.

        Args:
            parameter: 'freshness', 'color', 'stem_length', 'cost'
        """
        if parameter == 'freshness':
            # Свежие вперед
            self.flowers.sort(key=lambda f: f.freshness, reverse=True)
        elif parameter == 'color':
            self.flowers.sort(key=lambda f: f.color)
        elif parameter == 'stem_length':
            self.flowers.sort(key=lambda f: f.stem_length)
        elif parameter == 'cost':
            self.flowers.sort(key=lambda f: f.cost)
        else:
            print("Неизвестный параметр сортировки")
            return

        print(f"Букет отсортирован по параметру: {parameter}")

    def find_flowers_by_lifetime(self, min_days, max_days):
        """Поиск цветов в букете по диапазону времени жизни"""
        found = [f for f in self.flowers if min_days <= f.lifetime <= max_days]
        return found

    def __repr__(self):
        return f"Букет ({len(self.flowers)} цветов): {self.flowers}"


# ==========================================
# ДЕМОНСТРАЦИЯ РАБОТЫ ПРОГРАММЫ
# ==========================================

if __name__ == "__main__":
    # Создаем экземпляры цветов разных видов
    r1 = Rose(color="Красный", stem_length=50, cost=150, freshness=90)
    r2 = Rose(color="Белый", stem_length=45, cost=140, freshness=80)
    t1 = Tulip(color="Желтый", stem_length=30, cost=100, freshness=95)
    t2 = Tulip(color="Красный", stem_length=35, cost=110, freshness=60)
    o1 = Orchid(color="Фиолетовый", stem_length=60, cost=300, freshness=100)

    # Создаем букет
    my_bouquet = Bouquet()

    # Добавляем цветы в букет
    my_bouquet.add_flower(r1)
    my_bouquet.add_flower(r2)
    my_bouquet.add_flower(t1)
    my_bouquet.add_flower(t2)
    my_bouquet.add_flower(o1)

    print("--- Информация о букете ---")
    print(my_bouquet)
    print(f"Общая стоимость букета: {my_bouquet.get_total_cost()} руб.")
    print(f"Среднее время увядания букета: {my_bouquet.get_wilting_time()} дн.")
    print()

    # Сортировка по стоимости
    print("--- Сортировка по стоимости ---")
    my_bouquet.sort_flowers('cost')
    print(my_bouquet)
    print()

    # Сортировка по свежести
    print("--- Сортировка по свежести ---")
    my_bouquet.sort_flowers('freshness')
    print(my_bouquet)
    print()

    # Поиск цветов (например, которые живут от 5 до 7 дней)
    print("--- Поиск цветов (время жизни от 5 до 7 дней) ---")
    found_flowers = my_bouquet.find_flowers_by_lifetime(5, 7)
    if found_flowers:
        for f in found_flowers:
            print(f"Найден: {f}")
    else:
        print("Цветы не найдены")
