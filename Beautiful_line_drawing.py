#!/usr/bin/env python
# coding: utf-8

# In[1]:


import drawSvg as draw
d = draw.Drawing(2000, 2000, origin='center', displayInline=False)
R=0
x1a = -200
y1a = 0
x2a = -400
y2a = 500
x1b = 0
x2b = 500
y1b = 0
y2b = 500
d.append(draw.Line(x1a,y1a,x2a,y2a,stroke= "red", stroke_width=2))
d.append(draw.Line(x1b,y1b,x2b,y2b,stroke= "red", stroke_width=2))
n=36
for i in range (0,n):
    x1a = x1a + i*(x2a-x1a)/n
    y1a = y1a + i*(y2a-y1a)/n
    x2b = x2b - i*(x2b-x1b)/n
    y2b = y2b - i*(y2b-y1b)/n
    if i > n/5:
        B = 0
        G=255
    else:
        B = 255
        G = 0
    color = '#%02x%02x%02x' % (R,B,G)
    d.append(draw.Line(x1a,y1a,x2b,y2b,stroke= color, stroke_width=2))
    
d


# In[ ]:




