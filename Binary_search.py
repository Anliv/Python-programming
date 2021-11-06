#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Binary search
def binary_search(X,y):
    start,end = 0, (len(X)-1)
    while start <= end:
        n = (start+end)//2
        if X[n] == y:
            return True
        elif X[n] > y:
            return binary_search(X[0:n],y)
        else:
            return binary_search(X[n+1:],y)
    return False


# In[2]:


X = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
y1= 40
print(binary_search(X,y1))


# In[3]:


#2. Palindrome
def palindrome_check(X):
    if len(X) ==0 or len(X) ==1:
        return True
    elif X[0] != X[-1]:
        return False
    else:
        return palindrome_check(X[1:-1])

palindrome_check("nalsaslan")


# In[4]:


#3. Triangular numbers
def triangular(n):
    if n == 0:
        return 0
    else:
        return n + triangular(n-1)

K=[]
for i in range (0,21):
    K.append(triangular(i))
print(K)


# In[ ]:




