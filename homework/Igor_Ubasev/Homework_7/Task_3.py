lines = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]
def process_line(line):
    colon_pos = line.index(':')
    number = int(line[colon_pos + 1:].strip())
    return number + 10
results = []
for line in lines:
    results.append(process_line(line))
for result in results:
    print(result)
