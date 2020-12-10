# Статистика - statistics

def minimum(b):
    return str(min(b))

def maximum(b):
    return str(max(b))

def median(b):
    b.sort()
    if len(b)%2 == 0:
        return str((b[len(b)//2] + b[len(b)//2 -1])/2)
    return str(b[len(b)//2])

def summa(b):
    return str(sum(b))

def firstmostfrequent(b):
    d = dict()
    for i in b:
        if i not in d:
            d[i] = 0
        d[i] += 1
    mx , out = 0, ""
    for i in d:
        if d[i] > mx:
            mx = d[i]
            out = str(i)
    return out

def WTF(s, a, b):
    if len(s)>=5:
        if s[:3] == "min":
            b.append(int(s[4::]))
            return minimum(b)
        if s[:3] == "max":
            b.append(int(s[4::]))
            return maximum(b)
        if s[:3] == "sum":
            b.append(int(s[4::]))
            return summa(b)
        if len(s) >= 8 and s[:6] == "median":
            b.append(int(s[7::]))
            return median(b)
        if len(s) >= 19 and s[:17] == "firstmostfrequent":
            b.append(int(s[18::]))
            return firstmostfrequent(b)
                     
    return "Fail"

def statistics(a):
    a = a.split()
    b = []
    for i in range(1, len(a)):
        b.append(int(a[i]))
    return WTF(a[0].lower(), a, b)

