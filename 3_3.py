def thesaurus(*values):
    my_dict = dict()
    for value in values:
        my_dict.setdefault(value[0], [])
        my_dict[value[0]].append(value)
    return my_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
