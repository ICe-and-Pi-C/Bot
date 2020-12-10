
# coding: utf-8

# In[ ]:


def dyslexia(s):
    a = s.split()
    f = open("text.txt", "r", encoding = "utf-8")
    r = f.read().split()
    for i in range(len(r) - len(a)):
        flag = 1
        for j in range(len(a)):
            if (sorted(a[j]) != sorted(r[i + j])):
                flag = 0
        if (flag == 1):
            ans = list()
            for j in range(len(a)):
                ans.append(r[i + j])
            return " ".join(ans)
    f.close()

def sypher(s):
    a = s.split("#")    
    if (a[0]=="dyslexia"):
        return dyslexia(a[1])
    return "exit"

