my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.append(f'"{int(elem):02}"')
    elif elem.startswith('+') or elem.startswith('-') and elem[1:].isdigit():
        new_list.append(f'"{elem[0]}{int(elem[1:]):02}"')
    else:
        new_list.append(elem)

answer = ' '.join(new_list)
print(answer)
