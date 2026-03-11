def operation_selector(func):
    def wrapper(first, second, *args, **kwargs):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@operation_selector
def calc(first, second, operation):
    """Выполняет арифметическую операцию с двумя числами"""
    if operation == '+':
        result = first + second
        print(f"{first} + {second} = {result}")
        return result
    elif operation == '-':
        result = first - second
        print(f"{first} - {second} = {result}")
        return result
    elif operation == '*':
        result = first * second
        print(f"{first} * {second} = {result}")
        return result
    elif operation == '/':
        if second == 0:
            print("Ошибка: деление на ноль!")
            return None
        result = first / second
        print(f"{first} / {second} = {result}")
        return result
    else:
        print(f"Неизвестная операция: {operation}")
        return None


try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    calc(num1, num2, None)

except ValueError:
    print("Ошибка: пожалуйста, введите корректные числа")
