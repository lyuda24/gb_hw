import re

email_adress1 = 'somepeople33@gmail.com'
email_adress2 = 'illuminator2000@mail.ru'
email_adress3 = 'illuminator2000@mailru'


def email_parse(args):
    my_dict = dict()
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(args)
    if not result:
        raise ValueError(f'Электронный адрес не валиден: {args}')
    return result.groupdict()


print(email_parse(email_adress1))
print(email_parse(email_adress2))
print(email_parse(email_adress3))
