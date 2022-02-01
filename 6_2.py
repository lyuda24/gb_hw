my_dict = dict()
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        sp = line.split(' ')
        ip = sp[0]
        if ip not in my_dict:
            my_dict[ip] = 1
        else:
            my_dict[ip] += 1

m = 0
k = ''
for key, value in my_dict.items():
    if value > m:
        m = value
        k = key
print(k, m)
