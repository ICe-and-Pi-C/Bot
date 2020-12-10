
# coding: utf-8

# In[ ]:


# Шифр - cypher

def primeMultiplicator(a, prime):
    ar = list()
    d = dict()
    for i in range(26):
        ar.append(chr(ord('a') + i))
        d[chr(ord('a') + i)] = len(ar)-1
    for i in range(10):
        ar.append(chr(ord('0') + i))
        d[chr(ord('0') + i)] = len(ar)-1
    ar.append('\'')
    d['\''] = 36
    d[' '] = 37
    ar.append(' ')
    ans = ""
    rev = dict()
    for i in ar:
        rev[ar[(prime * (d[i] + 1 )) % 39 - 1]] = i
    for i in a:
        ans+=rev[i]
    return(ans)

def Caesar(code, a):
    out = ''
    ar = []
    d = dict()
    for i in range(26):
        ar.append(chr(ord('a') + i))
        d[chr(ord('a') + i)] = len(ar) - 1
    for i in range(10):
        ar.append(chr(ord('0')+i))
        d[chr(ord('0')+i)] = len(ar) - 1
    ar.append('\'')
    d['\''] = 36
    ar.append(' ')
    d[' '] = 37
    for i in range(len(a)):
        out += ar[(d[a[i]] - code + len(ar))% len(ar)]
    return out

def Vigenere(a, s):
    ans = ""
    ar = []
    d = dict()
    for i in range(26):
        ar.append(chr(ord('a') + i))
        d[chr(ord('a') + i)] = len(ar) - 1
    for i in range(10):
        ar.append(chr(ord('0')+i))
        d[chr(ord('0')+i)] = len(ar) - 1
    ar.append('\'')
    d['\''] = 36
    ar.append(' ')
    d[' '] = 37
    for i in range(len(a)):
        ans += ar[(d[a[i]] + 38 - d[s[i%len(s)]]) % 38]
    return ans

def Cypher(s):
    a = s.split('|')
    if 'Caesar' in a[0]:
        q = a[0].split()
        return Caesar(int(q[1][5::]), a[1])
    elif 'prime multiplicator' in a[0]:
        q = int(a[0].split()[1].split('=')[1])
        return primeMultiplicator(a[1], q)
    elif 'reversed' in a[0]:
        return a[1][::-1]
    elif "Vigenere's" in a[0]:
        return Vigenere(a[1], a[0].split('=')[1])
    else:
        return "Fail"

