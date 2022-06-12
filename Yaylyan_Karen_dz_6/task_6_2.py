with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_count = {}
    for line in f:
        line = line.strip().split()
        ip = line[0]
        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

spammer = max(ip_count.items(), key=lambda x: x[1])[0]
print(spammer)
