PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


items = [line.split() for line in PRICE_LIST.split('\n')]
price_dict = {name: int(price.replace('р', '')) for name, price in items}

print(price_dict)
