#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import drawSvg as draw
from random import uniform
import math
from itertools import combinations

window_x = 400
window_y = 400
r = 10 #radius of these balls
timestep = 1
X=[]
Y=[]
vx=[]
vy=[]
n=15 #number of balls

for i in range (0,n):
    x = uniform(- window_x/2+r,window_x/2-r)
    y = uniform(- window_y/2+r,window_y/2-r)
    X.append(x)
    Y.append(y)
    vx.append(uniform(5,5))
    vy.append(uniform(5,5))

ball=[]
for i in range (0,n):
    ball.append([X[i],Y[i],vx[i],vy[i]])


def update_position(i):
    X[i] += timestep * vx[i]
    Y[i] += timestep * vy[i]

    if X[i] - r < - window_x/2:
        X[i] = -window_x/2 + r
        vx[i] = -vx[i]
        
    if X[i] + r > window_x/2:
        X[i] = window_x/2 - r
        vx[i] = -vx[i]
        
    if Y[i] - r < - window_x/2:
        Y[i] = -window_y/2 + r
        vy[i] = -vy[i]
        
    if Y[i] +r > window_y/2:
        Y[i] = window_y/2 - r
        vy[i] = -vy[i]
    
        
def coll():
    two_balls=combinations(range(n),2)
    for i,j in two_balls:
        distance = math.sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
        if distance <= 2 * r:
            vx[i],vx[j], vy[i],vy[j] = vx[j],vx[i], vy[j],vy[i]
            
            
def draw_ball (i):
    d.append(draw.Circle(X[i],Y[i],r,fill="red"))
    return d



def draw_frame ():
    for i in range(0,n):
        
        update_position(i)
        draw_ball(i)
        coll()
    return d


with draw.animate_jupyter(draw_frame, delay=0.05) as anim:
    while( True ):
        d = draw.Drawing(window_x, window_y, origin='center' )
        d.append(draw.Rectangle(-window_x/2,-window_y/2,window_x,window_y, fill='black'))
        anim.draw_frame()
        
d


# In[ ]:




