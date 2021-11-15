my_sales = [57.8, 46.51, 97, 75.64, 84.51, 57.94, 47, 53.80, 49.06, 67.52, 57.64, 79, 85.43, 65.09, 37.96]

# a
for sale in my_sales:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end = ', ')

# b
print(id(my_sales))
my_sales.sort()
print(id(my_sales))
for sale in my_sales:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')

# c
my_sales.sort()
sales_reverse = list(reversed(my_sales))
for sale in sales_reverse:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')

# d
my_sales.sort()
expensive_five = my_sales[-5:]
for sale in expensive_five:
    rub = int(sale)
    kop = (sale - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end=', ')
