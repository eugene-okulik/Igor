import random

salary = int(input("Какая у вас зарплата: "))
bonus = random.choice([True, False])
if True == bonus :
    print(f"${salary+random.randint(1, 10000)}")
