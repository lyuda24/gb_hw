duration = int(input('Введите время в секундах: '))

days = duration // (60 * 60 * 24)
hours = (duration - days * (60 * 60 * 24)) // (60 * 60)
min = (duration - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
sec = (duration - days * (60 * 60 * 24) - hours * (60 * 60) - min * 60)

if days == 0:
    if hours == 0:
        if min == 0:
            print(sec, 'сек')
        else:
            print(min, 'мин', sec, 'сек')
    else:
        print(hours, 'час', min, 'мин', sec, 'сек')
else:
    print(days, 'дн', hours, 'час', min, 'мин', sec, 'сек')
