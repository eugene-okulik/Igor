my_dict = {
    "tuple": (10, 36, "test", 2.67, True),
    "llist": [12, 53, None, "test_2", False, 5.62],
    "dict": {"one": "value", "two": "value2", "three": "value3", "four": 6.78, "five": 1},
    "set": {99, 38, None, 'test_3', True, 2.42}}
my_dict["llist"].append(55)
my_dict["llist"].pop(1)
my_dict["dict"]["i am a tuple"] = "шесть"
my_dict["dict"].pop("one")
my_dict["set"].add("тест")
my_dict["set"].pop()
print(my_dict["tuple"][-1])
print(*my_dict.items(), sep='\n')
