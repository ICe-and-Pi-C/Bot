# Момент - moment

from datetime import datetime, date, time

def getMoment(s):
    s = s.split()
    s[0] = s[0].split(':')
    s[1] = s[1].split('.')
    d = date(int(s[1][2]), int(s[1][1]), int(s[1][0]))
    t = time(int(s[0][0]), int(s[0][1]))
    dt = datetime.combine(d, t)
    return dt.strftime("%d %B %H:%M").replace("November","ноября")

