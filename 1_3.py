percent = []
for num in range(1, 101):
    percent.append(num)

n = 0
while n < len(percent):
    n += 1
    if 11 <= n <= 14:
        word = 'процентов'
    elif n % 10 == 1:
        word = 'процент'
    elif 2 <= n % 10 <= 4:
        word = 'процента'
    else:
        word = 'процентов'
    print(n, word)
