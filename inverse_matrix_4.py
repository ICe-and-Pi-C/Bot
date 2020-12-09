
# coding: utf-8

# In[ ]:


# Инверсия матрицы - inverse-matrix

def inverse(a):
    if (abs(np.linalg.det(a)) < 0.000001):
        return "unsolvable"
    x = np.linalg.inv(a)
    if (x == a).all():
        return "unsolvable"
    out = ''
    for i in x:
        for j in i:
            out += str(j) + ' ' + '& '
        out = out[:len(out)-1]
        out = out[:len(out)-1]
        out += "\\\\ "
    out = out[:len(out)-1]
    out = out[:len(out)-1]
    out = out[:len(out)-1]
    out = out[:len(out)-1]
    return out

