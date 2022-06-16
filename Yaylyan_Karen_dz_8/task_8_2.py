import re


def log_parse(log_request):
    pattern_ip_v4 = r'^((?:\d+\.){3}\d+) - - \[(.*?)\] "(\w+) ((?:/\w+){2}) \w+/\d\.\d" (\d+) (\d+)'
    pattern_ip_v6 = r'^(\w+(?::+\w+){,7}) - - \[(.*?)\] "(\w+) ((?:/\w+){2}) \w+/\d\.\d" (\d+) (\d+)'
    pattern = pattern_ip_v4 + '|' + pattern_ip_v6

    RE_GET_PARSER = re.compile(pattern)
    result = RE_GET_PARSER.findall(log_request)

    result = list(result[0])
    if result[0]:
        result = result[:-6]
    else:
        result = result[6:]
    return result


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(log_parse(line))
