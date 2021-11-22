from random import choice


def get_jokes(first_words, second_words, third_words):
    first_word = choice(first_words)
    second_word = choice(second_words)
    third_word = choice(third_words)
    return (f'{first_word} {second_word} {third_word}')


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(nouns, adverbs, adjectives))
