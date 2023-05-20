from datetime import datetime


def nearest_date(*dates: tuple) -> str:
    try:
        dates = (''.join(list(dates))).split(' ')
        dates = [datetime.strptime(i, '%d.%m.%Y') for i in dates]
        now = datetime.now()
        dates.append(now)
        dates = sorted(dates)
        if now == max(dates):
            return datetime.strftime(dates[-2], '%d.%m.%Y')
        elif now == min(dates):
            return datetime.strftime(dates[1], '%d.%m.%Y')
        else:
            if dates[dates.index(now)+1]-now > dates[dates.index(now)-1]-now:
                return datetime.strftime(dates[dates.index(now)-1], '%d.%m.%Y')
            elif (dates[dates.index(now)+1]-now) == (dates[dates.index(now)-1]-now):
                return datetime.strftime(dates[dates.index(now) + 1], '%d.%m.%Y')
            else:
                return datetime.strftime(dates[dates.index(now) + 1], '%d.%m.%Y')
    except Exception:
        return ('Неверный формат данных')


print(nearest_date(input()))
