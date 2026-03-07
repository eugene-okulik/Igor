import random

salary = int(input("Какая у вас зарплата: "))
bonus = random.choice([True, False])
if bonus is True:
    print(f"${salary + random.randint(1, 10000)}")
