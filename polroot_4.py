
# coding: utf-8

# In[ ]:


# Корни полинома - polinomial-root

def readPolynom(s):
    i= 0
    s = s.split('+')
    d = dict()
    for i in range(len(s)):
        s[i] = s[i].strip()
        j = 0
        q = s[i].split('^')
        q1 = q[0].split('*')
        if (len(q) == 2):
            q1.append(int(q[-1]))
        if (q1[0][0] == '('):
            q1[0] = float(q1[0][1:len(q1[0]) - 1])
        else:
            q1[0] = float(q1[0])
        if (len(q1) == 1):
            d[0] = q1[0]
        elif (len(q1) == 2):
            d[1] = q1[0]
        else:
            d[q1[2]] = q1[0]
    return d

def f(d, x):
    ans = 0
    for i in d:
        ans += (x**i)*d[i]
    return ans

def doPolynom(s):
    d = readPolynom(s)
    eps = 1e-9
    l = -1000
    r = -1000
    lf = f(d, l)
    for i in range(-1000, 1000, 1):
        for j in range(1, 11):
            if (f(d, i + 1/10 * j) * lf) <= 0:
                r = i +1 / 10 * j
                break
    #for i in range(-1000, 1000):
    #   if (f(d, i) * lf) <= 0:
    #       r = i
    #       break
    # Вторая версия - последняя           
    
    if (r == -1000):
        return "no roots"
    if (lf > 0):
        l, r = r, l
    for _ in range(1000):
   #for _ in range(100): 
        m = (l + r)/2
        if (f(d,m) > 0):
            r = m
        else:
            l = m
    return str(l)

def doPolynom_v2(s):
    d = readPolynom(s)
    eps = 1e-9
    l = -1000
    r = -1000
    lf = f(d, l)
    for i in range(-1000, 1000):
        if (f(d, i) * lf) <= 0:
            r = i
            break
    if (r == -1000):
        return "no roots"
    if (lf > 0):
        l, r = r, l
    for _ in range(100):
        m = (l + r)/2
        if (f(d,m) > 0):
            r = m
        else:
            l = m
    return str(l)

