#!/usr/bin/env python
# coding: utf-8

# In[1]:


import drawSvg as draw
from math import sqrt


# In[ ]:


class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b
    
    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep
    
    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep
    
    def draw(self, pixels_per_meter):
        #pixels = pixels_per_meter * meters
        x = self.x * pixels_per_meter
        y = self.y * pixels_per_meter
        return draw.Circle(x, y, self.pixel_radius, fill=f'rgb({self.r}, {self.g}, {self.b})')

class System:
    def __init__(self, body_list):
        self.body_list = body_list
    
    def update(self, timestep):
        for i, b in enumerate(self.body_list):
            ax, ay = self.compute_acceleration(i)
            b.update_velocity(ax, ay, timestep)
            b.update_position(timestep)
    
    def compute_acceleration(self, n):
        #For each body, loop over every body to compute and update all accelerations: a = (G*mass)/r^2
        
        G = 6.67384e-11
        this_body = self.body_list[n]
        those_bodies = [b for b in self.body_list if b != this_body]
        
        ax_total = 0
        ay_total = 0
        for that_body in those_bodies:
            r = sqrt((that_body.y - this_body.y)**2 + (that_body.x - this_body.x)**2)
            a = (G*that_body.mass) / r**2
            
            dx = that_body.x - this_body.x
            dy = that_body.y - this_body.y
            ax = a * dx/r
            ay = a * dy/r
            ax_total += ax
            ay_total += ay
            
        return ax_total, ay_total
    
    def draw(self, pixels_per_meter, D):
        for body in self.body_list:
            D.append(body.draw(pixels_per_meter))
            

AU = 1.49598e11 # number of meters per astronomical unit
EM = 5.9736e24  # mass of the Earth in kilograms
TIME_SCALE = 3.0e6              # how many real seconds for each second of simulation
PIXELS_PER_METER = 120. / AU    # distance scale for the simulation
FRAME_RATE = 30
TIMESTEP = 1.0 / FRAME_RATE     # time between drawing each frame
# Solar system data comes from
#   http://hyperphysics.phy-astr.gsu.edu/hbase/solar/soldata2.html
sun     = Body(1.98892e30, 0, 0, 0, 0, 15, 255, 255, 0)
mercury = Body(.06 * EM, -.3871 * AU, 0, 0, 47890, 3, 255, 102, 0)
venus   = Body(.82 * EM, -.7233 * AU, 0, 0, 35040, 6, 0, 153, 51)
earth   = Body(1.0 * EM, -1.0 * AU, 0, 0, 29790, 7, 0, 102, 255)
mars    = Body(.11 * EM, -1.524 * AU, 0, 0, 24140, 4, 204, 51, 0)
solar_system = System([sun, mercury, venus, earth, mars])

def draw_frame():
    solar_system.draw(PIXELS_PER_METER, D)
    solar_system.update(TIMESTEP * TIME_SCALE)
    return( D )

with draw.animate_jupyter(draw_frame, delay=0.05) as anim:
    while( True ):
        D = draw.Drawing(600, 600, origin='center') # clear canvas
        D.append( draw.Rectangle(-300,-300,600,600,fill='black')) # black background
        anim.draw_frame()


# In[ ]:




