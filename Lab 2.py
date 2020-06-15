#!/usr/bin/env python
# coding: utf-8

# Type Markdown and LaTex: $a^2$

# In[1]:


from resources306 import*


# In[2]:


def f(x,y):
    return x**2 - x**2 *y

y = 3
x = 0
xfinal = 5
n = 20
h = (xfinal - x) / n

xlist = [x]
ylist = [y]

for i in range(n):
    slope = f(x,y)
    y = y + h*slope
    x = x + h
    xlist.append(x)
    ylist.append(y)


# In[3]:


plt.figure(figsize=(8,8))
slopefieldplot(f,0,4,0,4,.1,lw=2)
plt.plot(xlist, ylist, 'mo-', lw=3, alpha=.6, label = 'Euler Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='center')


# In[4]:


def f(x,y):
    return x - y + 2

y = 5
x = 0
xfinal = 8
n = 16
h = (xfinal - x) / n

xlist = [x]
ylist = [y]

for i in range(n):
    slope = f(x,y)
    y = y + h*slope
    x = x + h
    xlist.append(x)
    ylist.append(y)


# In[5]:


plt.figure(figsize=(8,8))
slopefieldplot(f,0,4,2,7,.1,lw=2)
plt.plot(xlist, ylist, 'mo-', lw=3, alpha=.6, label = 'Euler Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='center')


# In[ ]:




