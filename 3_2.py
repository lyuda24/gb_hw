def num_translate_adv(items, key):
    """translate nums"""
    for keys in items:
        if key[0].isupper():
            key = key.lower()
            return items.get(key).capitalize()
        else:
            return items.get(key)


translate = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

print(num_translate_adv(translate, 'Ten'))
