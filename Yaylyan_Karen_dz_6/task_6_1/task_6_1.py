with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    parsed_logs = []
    for line in f:
        line = line.strip().split()
        parsed_logs.append((line[0], line[5][1:], line[6]))

print(parsed_logs)
