duration = int(input())

seconds_in_minute = 60
seconds_in_hour = seconds_in_minute*60
seconds_in_day = seconds_in_hour*24

days = duration // seconds_in_day
duration %= seconds_in_day
hours = duration // seconds_in_hour
duration %= seconds_in_hour
minutes = duration // seconds_in_minute
seconds = duration % seconds_in_minute

if days:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
elif hours:
    print(f'{hours} час {minutes} мин {seconds} сек')
elif minutes:
    print(f'{minutes} мин {seconds} сек')
else:
    print(f'{seconds} сек')
