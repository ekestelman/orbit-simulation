import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['figure.figsize'] = [10, 10]

gconst = 1

class Planet:
    def __init__(self, name, mass, pos, vel):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.xhist = [pos[0]]
        self.yhist = [pos[1]]
        
def distcalc(a, b):
    return ( (a.pos[0]-b.pos[0])*(a.pos[0]-b.pos[0]) + (a.pos[1]-b.pos[1])*(a.pos[1]-b.pos[1]) )**.5

def accelcalc(a, b):
    dist = distcalc(a, b)
    return -( gconst * b.mass / (dist*dist*dist) * (a.pos - b.pos) )

nplanets = 5                 # Number of planets

sun = Planet('sun', 100, [0., 0.], [0.2, -0.5])
pluto = Planet('pluto', 1, [1., 0.], [0., 9.])
moon = Planet('moon', 1, [2., 0.], [0., 9.])
galadriel = Planet('galadriel', 1, [3., 0.], [0., 6.])
chungus = Planet('chungus', 200, [-10., 0.], [0., -1.5])

planets = [sun, pluto, moon, galadriel, chungus]
#planets.remove(moon)                                  # Easier way to remove unwanted planets?
#planets.remove(galadriel)

del planets[nplanets:]

momentum = [0,0]

for i in planets:
    if i != sun:
        momentum[0] += i.vel[0] * i.mass
        momentum[1] += i.vel[1] * i.mass
        
sun.vel = -np.array(momentum) / sun.mass             # Sets Sun's vel for stationary CoM. Can comment out.

time = 0

mindist = 100              # Closest approach between objects
collision = 0

dt = .0001

# make an attribute dist, an array with an element for dist to each other planet. Append through loop.

# Euler

#for i in planets:
#    i.xhist.append(i.pos)

#while time < 40000*dt:
while time < 4:
    
    for i in planets:
        
        temppos = i.pos + i.vel * dt
        i.xhist.append(temppos[0])
        i.yhist.append(temppos[1])
        
        accel = 0                                # Initialize accel, then add each component
        
        for j in planets:
            if j != i:
                accel += accelcalc(i,j)            # Need to store accel components then add up for 3+ bodies
                                                   # Try calculating force for fewer, then accel for each
        i.vel += accel * dt

    for i in planets:                                    # Done finding accelsa and vels, can finally
        i.pos = np.array([i.xhist[-1],i.yhist[-1]])
    
    for i in planets:
        for j in planets:
            if j != i:
                collision = distcalc(i,j)
                if collision < mindist:
                    mindist = collision
            else:
                break
                
    if mindist < .005:
        break                      # Should shrink time increments during close encounters
                    
    time += dt                                   # Include a collision test. Based on dist or on x and y flip

print(time, time/dt)

#plt.rcParams['figure.figsize'] = [10, 10]
    
#for i in planets:                           # Make another file for this
#    plt.plot(i.xhist,i.yhist)
    #print(i.xhist,i.yhist)
    
#plt.gca().set_aspect('equal')
#plt.xlim(-12, 4)
#plt.ylim(-8, 8)

#plt.show()                                   # Not necessary in notebook?

#with open('trajectory.py', 'w') as f:               # Something doesn't work here
#  f.write('planets = [')
#  i = 0
#  while i < nplanets-1:
#    f.write(str(planets[i]) + ', ')
#    i += 1
#  f.write(str(planets[i]) + ']')
    #f.write(i.name + 'x = ' + str(i.xhist))
    #f.write(i.name + 'y = ' + str(i.yhist))

'''
# In[8]:


# Test of max movement in one time increment for checking appropriate proximity limits.

leap = 0

for i in planets:
    for j in range(len(i.xhist)-1):
        jump = ( (i.xhist[j]-i.xhist[j+1]) * (i.xhist[j]-i.xhist[j+1]) +                 (i.yhist[j]-i.yhist[j+1]) * (i.yhist[j]-i.yhist[j+1]) ) ** .5
        if jump > leap:
            leap = jump
            
print(leap)


# In[132]:


#%%time

# Trying more planets (animation)

def init():
    line.set_data([], [])
    line2.set_data([], [])
    return line,

def run(orbit):
    x, y = orbit
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

def get_data():
    for i in range(len(sun.xhist)):
        yield sun.xhist[i], sun.yhist[i], pluto.xhist[i], pluto.yhist[i]                 # [i] for blank, full list for full drawing
    #return sun.xhist, sun.yhist
    
def animate(i):
    sunx.append(sun.xhist[i*50])
    suny.append(sun.yhist[i*50])
    plutox.append(pluto.xhist[i*50])
    plutoy.append(pluto.yhist[i*50])
    #xdata.append(x)
    #ydata.append(y)
    line.set_data(sunx,suny)
    line2.set_data(plutox,plutoy)
    return line,

fig, ax = plt.subplots()
#ax.set_xlim(-10, 2)
#ax.set_ylim(-4, 6)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
line, = ax.plot([], [], lw=2)
sunx, suny = [], []
line2, = ax.plot([], [], lw=2)
plutox, plutoy = [], []

#ani = animation.FuncAnimation(fig, run, get_data, interval=10, init_func=init)
ani = animation.FuncAnimation(fig, animate, frames=400, interval=5, init_func=init)
# Interval adjusts animation speed (higher is faster)

plt.show()

ani


# In[123]:


#%%time

# Sun only animation

def init():
    line.set_data([], [])
    return line,

def run(orbit):
    x, y = orbit
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

def get_data():
    for i in range(len(sun.xhist)):
        yield sun.xhist[i], sun.yhist[i]                 # [i] for blank, full list for full drawing
    #return sun.xhist, sun.yhist
    
def animate(i):
    x = sun.xhist[i*100]
    y = sun.yhist[i*100]
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata,ydata)
    return line,

fig, ax = plt.subplots()
ax.set_xlim(-10, 2)
ax.set_ylim(-4, 6)
line, = ax.plot([], [], lw=2)
xdata, ydata = [], []

#ani = animation.FuncAnimation(fig, run, get_data, interval=10, init_func=init)
ani = animation.FuncAnimation(fig, animate, frames=200, interval=10, init_func=init)

plt.show()

ani


# In[48]:


import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_gen():
    for i in range(len)
    yield sun.xhist, sun.yhist


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    #if t >= xmax:
    #    ax.set_xlim(xmin, 2*xmax)
    #    ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, interval=10, init_func=init)
plt.show()

ani


# In[9]:


#%%time

nplanets = 2                 # Number of planets

sun = Planet('Sun', 100, [0., 0.], [0.2, -0.5])
pluto = Planet('Pluto', 1, [1., 0.], [0., 9.])
moon = Planet('Moon', 1, [2., 0.], [0., 9.])
galadriel = Planet('Galadriel', 1, [3., 0.], [0., 6.])
chungus = Planet('Chungus', 200, [-10., 0.], [0., -1.5])

planets = [sun, pluto, moon, galadriel, chungus]
#planets.remove()                                  # Easier way to remove unwanted planets?

del planets[nplanets:]

momentum = [0,0]                                   # Change this to make system move wrt viewer

for i in planets:
    if i != sun:
        momentum[0] += i.vel[0] * i.mass
        momentum[1] += i.vel[1] * i.mass
        
sun.vel = -np.array(momentum) / sun.mass             # Sets Sun's vel for stationary CoM. Can comment out.

time = 0

mindist = 100              # Closest approach between objects
collision = 0

dt = .0002

# make an attribute dist, an array with an element for dist to each other planet. Append through loop.

# RK4

#for i in planets:
#    i.xhist.append(i.pos)

while time < 20000*dt:
    
    for i in planets:
        
        posk1 = i.pos + i.vel * dt * .5
        #i.xhist.append(temppos[0])
        #i.yhist.append(temppos[1])
        
        accel = 0                                # Initialize accel, then add each component
        
        for j in planets:
            
            if j != i:
                accel += accelcalc(i,j)            # Need to store accel components then add up for 3+ bodies
                                                   # Try calculating force for fewer, then accel for each
                #temppos = i.pos + i.vel * dt     #doesn't need to be here
                #i.vel += accel * dt               # accel for other planets depends on pos, not vel
                #i.xhist.append(temppos[0])
                #i.yhist.append(temppos[1])
                
#            else:
#                pass                        #does nothing here
            
        i.vel += accel * dt
        #i.pos = temppos                         #can't change pos yet, fudges things
        #accel = accel
        #tpos = pos + vel * dt
    for i in planets:
        i.pos = np.array([i.xhist[-1],i.yhist[-1]])
    
    for i in planets:
        for j in planets:
            if j != i:
                collision = distcalc(i,j)
                if collision < mindist:
                    mindist = collision
            else:
                break
                
    if mindist < .005:
        break                      # Should shrink time increments during close encounters
                    
    time += dt                                   # Include a collision test. Based on dist or on x and y flip

print(time, mindist)

plt.rcParams['figure.figsize'] = [10, 10]
    
for i in planets:
    plt.plot(i.xhist,i.yhist)
    #print(i.xhist,i.yhist)
    
plt.gca().set_aspect('equal')
plt.show()


# In[10]:


#%%time

#obsolete

nplanets = 2                 # Number of planets

sun = Planet('Sun', 10, [0.,0.], [0.,-.35])

pluto = Planet('Pluto', 1, [1.,0.], [0.,3.5])

planets = [sun, pluto]

time = 0

dt = .0001

# make an attribute dist, an array with an element for dist to each other planet. Append through loop.

# RK4

#for i in planets:
#    i.xhist.append(i.pos)

while time < 40000*dt:
    
    for i in planets:
        
        for j in planets:
            
            if j != i:
                accel = accelcalc(i,j)
                temppos = i.pos + i.vel * dt
                i.vel += accel * dt               # accel for other planets depends on pos, not vel
                i.xhist.append(temppos[0])
                i.yhist.append(temppos[1])
                
            else: pass
        #accel = accel
        #tpos = pos + vel * dt
    for i in planets:
        i.pos = np.array([i.xhist[-1],i.yhist[-1]])
    
    time += dt                                   # Include a collision test. Based on dist or on x and y flip
    
for i in planets:
    plt.plot(i.xhist,i.yhist)
    #print(i.xhist,i.yhist)
    
plt.rcParams['figure.figsize'] = [8, 8]
plt.show()


# In[11]:


# Initial parameters
    
pos = [1, 0]

dist = ( pos[0]*pos[0] + pos[1]*pos[1] ) ** .5

vel = [0, np.pi]             # Yields period of 2

speed = ( vel[0]*vel[0] + vel[1]*vel[1] ) ** .5   # Total speed (vel components combined, no direction)
                                                  # Used for setting mass

#gconst = 6.6743e-11     # Gravitational constant
gconst = 1               # Fictional gravitational constant

mass = speed * speed * dist / gconst   # From centripetal and gravitational force eqns

time = 0

pos = np.array(pos)
vel = np.array(vel)

#accel = -( gconst * mass / (dist*dist*dist) * pos )
print(accel)


# In[12]:


get_ipython().run_cell_magic('time', '', '# Euler method\n\nposhist = []\nposhist.append(pos)\nxhist = []\nyhist = []\nxhist.append(pos[0])\nyhist.append(pos[1])\n\ndt = 0.02                          # Time increment\n\nwhile time < 2:\n    dist = ( pos[0]*pos[0] + pos[1]*pos[1] ) ** .5\n    accel = -( gconst * mass / (dist*dist*dist) * pos )\n    temppos = pos + vel * dt\n    tempvel = vel + accel * dt\n    pos = temppos\n    #dist = ( pos[0]*pos[0] + pos[1]*pos[1] ) ** .5               # Back order Euler?\n    #accel = -( gconst * mass / (dist*dist*dist) * pos )\n    #tempvel = vel + accel * dt\n    vel = tempvel\n    time += dt\n    xhist.append(pos[0])\n    yhist.append(pos[1])')


# In[13]:


plt.plot(xhist,yhist)
#fig = plt.figure(figsize=(5,10))
plt.rcParams['figure.figsize'] = [8, 8]
plt.show()


# In[14]:


#%%time
# 4th Order Runge-Kutta

poshist = []
poshist.append(pos)
xhist = []
yhist = []
xhist.append(pos[0])
yhist.append(pos[1])

dt = 0.02                          # Time increment

while time < 2:
    accel = -( gconst * mass / (dist*dist*dist) * pos )
    #temppos = pos + vel * dt
    #tempvel = vel + accel * dt
    k1 = vel
    temppos = pos + k1 * 0.5 * dt
    tempdist = ( temppos[0]*temppos[0] + temppos[1]*temppos[1] ) ** .5
    a1 = -( gconst * mass / (tempdist*tempdist*tempdist) * temppos)
    k2 = vel + a1 * 0.5 * dt
    temppos = pos + k2 * 0.5 * dt
    tempdist = ( temppos[0]*temppos[0] + temppos[1]*temppos[1] ) ** .5
    a2 = -( gconst * mass / (tempdist*tempdist*tempdist) * temppos)
    k3 = vel + a2 * 0.5 * dt
    temppos = pos + k3 * dt
    tempdist = ( temppos[0]*temppos[0] + temppos[1]*temppos[1] ) ** .5
    a3 = -( gconst * mass / (tempdist*tempdist*tempdist) * temppos)
    k4 = vel + a3 * dt
    #tempvel = vel + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
    temppos = pos + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
    pos = temppos
    dist = ( pos[0]*pos[0] + pos[1]*pos[1] ) ** .5
    #accel = -( gconst * mass / (dist*dist*dist) * pos)
    vel += dt / 6 * (accel + 2*a1 + 2*a2 + a3)
    time += dt
    xhist.append(pos[0])
    yhist.append(pos[1])


# In[15]:


# 4th Order Runge-Kutta (bad)

poshist = []
poshist.append(pos)
xhist = []
yhist = []
xhist.append(pos[0])
yhist.append(pos[1])

dt = 0.02                          # Time increment

while time < 2:
    #accel = -( gconst * mass / (dist*dist*dist) * pos )
    #temppos = pos + vel * dt
    #tempvel = vel + accel * dt
    k1 = vel
    temppos = pos + k1 * 0.5 * dt
    dist = 
    tempaccel = -( gconst * mass / (dist*dist*dist) * temppos)
    vel2 = vel + accel1 * 0.5 * dt
    pos2 = pos + vel2 * 0.5 * dt
    accel2 = -( gconst * mass / (dist*dist*dist) * pos2)
    vel3 = vel + accel2 * 0.5 * dt
    pos3 = pos + vel3 * dt
    accel3 = -( gconst * mass / (dist*dist*dist) * pos3)
    k4 = vel + tempaccel * dt
    #tempvel = vel + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
    temppos = pos + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
    pos = temppos
    accel = -( gconst * mass / (dist*dist*dist) * pos)
    vel += dt * accel
    time += dt
    xhist.append(pos[0])
    yhist.append(pos[1])


# In[ ]:



try:
    print('this is a try clause')
    int('')
    print('still trying')
except ValueError:
    print('this is an error clause')
    
print('eof')
'''
