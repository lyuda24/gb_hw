my_list = []
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        sp = line.split(' ')
        my_list.append((sp[0], sp[5].strip('"'), sp[6]))
print(my_list, end='\n')
