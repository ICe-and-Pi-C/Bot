
# coding: utf-8

# In[ ]:


#shape

import matplotlib.pyplot as plt
import random
points = input().split('|')[1].replace('(', '').replace(')', '').split()
p1 = []
p2 = []
print(len(points))
random.shuffle(points)
for i in range(min(len(points),500) ):
    points[i] = list(map(int, points[i].split(',')))
    p1.append(points[i][0])
    p2.append(points[i][1])
    plt.scatter(p1, p2, s = 2)
plt.show()

