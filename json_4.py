
# coding: utf-8

# In[ ]:


#json

def CaesarForJson(a):
    out = ''
    abc = a.split("#")[1].split("abc=")[1]
    code = int(a.split("code=")[1].split("#")[0])
    a = a.split("#")[2]
    d = dict()
    ar = []
    for i in range(len(abc)):
        ar.append(abc[i])
        d[abc[i]] = i
    for i in range(len(a)):
        out += ar[(d[a[i]] - code + len(ar))% len(ar)]
    return out

def VigenereForJson(a):
    s = a.split("code=")[1].split("#")[0]
    abc = a.split("#")[1].split("abc=")[1]
    a = a.split('#')[2]
    ans = ""
    ar = []
    d = dict()
    for i in range(len(abc)):
        ar.append(abc[i])
        d[abc[i]] = i
    for i in range(len(a)):
        ans += ar[(d[a[i]] + len(abc) - d[s[i%len(s)]]) % len(abc)]
    return ans

def JsonTaskS(a):
    a = a.split('"')
    ans = 0
    for i in range(len(a)):
        if '|' in a[i]:
            p = a[i].split('|')[1]
            tp = a[i].split('|')[0]
            if tp == "cypher":
                if p[0]=="C":
                    ans += int(translator(CaesarForJson(p)))
                if p[0] == "V":
                    ans += int(translator(VigenereForJson(p)))
            if tp == "math":
                ans += int(MathBot3(p))
            if tp == "determinant":
                ans += int(determinant(parse_matrix(p), 1))
            if tp == "string-number":
                ans+= int(translator(p))
        else:
            x = 0
            for j in range(len(a[i])):
                if a[i][j].isdigit() or a[i][j] == '-':
                    x+=1
            if x == len(a[i]) and a[i] != "":
                ans += int(a[i])
    return ans

