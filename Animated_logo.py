#!/usr/bin/env python
# coding: utf-8

# In[1]:


import drawSvg as draw


# In[ ]:





# In[2]:


#Excercise 1: draw logo with name
ann = draw.Drawing(300, 300, origin='center', displayInline=False)
ann.append(draw.Circle(50,50,30,fill="orange",origin='center'))
ann.append(draw.Circle(10,10,20,fill="orange"))
ann.append(draw.Circle(-20,-20,10,fill="orange"))
ann.append(draw.Text('An Tran',50,-50,10,fill='black'))
ann


# In[3]:


#Excercise 2: Favourite logo 
d = draw.Drawing(300, 300, origin='center', displayInline=False)

#1. Draw Arc
d.append(draw.ArcLine(0,0,30,45,150,
            stroke='red', stroke_width=10, fill='none', fill_opacity=0.6))
d.append(draw.ArcLine(0,0,30,150,210,
            stroke='yellow', stroke_width=10, fill='none', fill_opacity=0.6))
d.append(draw.ArcLine(0,0,30,210,300,
            stroke='green', stroke_width=10, fill='none', fill_opacity=0.6))
d.append(draw.ArcLine(0,0,30,300,360,
            stroke='blue', stroke_width=10, fill='none', fill_opacity=0.6))

#2. Draw Rectangle:
d.append(draw.Rectangle(4,-9,30,10,fill='blue',origin='center'))

#3. Draw Circle:
c = draw.Circle(0, 0, 10, fill='red')

#4. Draw animation:
c.appendAnim(draw.Animate('cy', '6s', '-80;80;-80',
                          repeatCount='indefinite'))
c.appendAnim(draw.Animate('cx', '6s', '0;80;0;-80;0',
                          repeatCount='indefinite'))
c.appendAnim(draw.Animate('fill', '6s', 'red;green;blue;yellow',
                          calcMode='discrete',
                          repeatCount='indefinite'))
d.append(c)

#5. Draw Text:
d.append(draw.Text('Google',20,-30,-60,fill='blue'))
d


# In[ ]:




