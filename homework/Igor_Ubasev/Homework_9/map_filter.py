import statistics

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def new_temperatures(x):
    return x > 28


new_list = list(filter(new_temperatures, temperatures))
new_conversion = list(map(int, new_list))
print(f'Самая высокая температура: {max(new_conversion)}\n'
      f'Самая низкая температура: {min(new_conversion)}\n'
      f'Средняя температура: {statistics.mean(new_conversion)}\n'
      )
