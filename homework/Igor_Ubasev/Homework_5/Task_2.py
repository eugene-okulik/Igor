a = "результат операции: 42"
colon_index = a.index(":")
number_str = a[colon_index + 2:]
number = int(number_str)
b = number + 10
print(b)

c = "результат операции: 514"
colon_index = c.index(":")
number_str = c[colon_index + 2:]
number = int(number_str)
d = number + 10
print(d)

e = "результат работы программы: 9"
colon_index = e.index(":")
number_str = e[colon_index + 2:]
number = int(number_str)
f = number + 10
print(f)
