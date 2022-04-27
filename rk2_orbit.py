import matplotlib.pyplot as plt
import numpy as np
from planets_module import planets, import_planets
from time import time as timer

#import_planets = False                                 # Comment out to use random generated planets

rkstart = timer()

gconst = 1

class Planet:                                           # Necessary if not import_planets?
    def __init__(self, name, mass, pos, vel):
        self.name = name
        self.mass = mass
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.xhist = [pos[0]]
        self.yhist = [pos[1]]
        self.temppos = [None, None]
        self.tempvel = [None, None]
        
def distcalc(a, b, temp=False):
    if temp:
      return ( (a.temppos[0]-b.temppos[0])*(a.temppos[0]-b.temppos[0]) + \
               (a.temppos[1]-b.temppos[1])*(a.temppos[1]-b.temppos[1]) )**.5
    return ( (a.pos[0]-b.pos[0])*(a.pos[0]-b.pos[0]) + \
             (a.pos[1]-b.pos[1])*(a.pos[1]-b.pos[1]) )**.5

def accelcalc(a, b, temp=False):
    dist = distcalc(a, b, temp)
    if temp:
      return -( gconst * b.mass / (dist*dist*dist) * (a.temppos - b.temppos) )
    return -( gconst * b.mass / (dist*dist*dist) * (a.pos - b.pos) )

if not import_planets:         # If planets not iportanted, this gives error
  
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
  
planets[0] = Planet('sun', 100, [0.,0.], [0., 0.])

momentum = [0,0]

for i in planets:
    if i.name != 'sun':
        momentum[0] += i.vel[0] * i.mass
        momentum[1] += i.vel[1] * i.mass
        
#sun.vel = -np.array(momentum) / sun.mass             # Sets Sun's vel for stationary CoM. Can comment out.
planets[0].vel = -np.array(momentum) / planets[0].mass             # Sets Sun's vel for stationary CoM. Can comment out.

time = 0

mindist = 100              # Closest approach between objects
collision = 0

dt = .002

# make an attribute dist, an array with an element for dist to each other planet. Append through loop.

#for i in planets:
#    i.xhist.append(i.pos)

#while time < 10000*dt:
while time < 10:
  
  for i in planets:
    
    i.temppos = i.pos + i.vel * dt * .5
    #i.xhist.append(temppos[0])
    #i.yhist.append(temppos[1])
    
    accel = 0                                # Initialize accel, then add each component
    
    for j in planets:
      if j != i:
        accel += accelcalc(i,j)            # Need to store accel components then add up for 3+ bodies
                                               # Try calculating force for fewer, then accel for each
    i.tempvel = i.vel + accel * dt * .5

  for i in planets:
    
    i.pos += i.tempvel * dt
    i.xhist.append(i.pos[0])
    i.yhist.append(i.pos[1])

    accel = 0
    
    for j in planets:
      if j!= i:
        accel += accelcalc(i, j, temp=True)

    i.vel += accel * dt

#  for i in planets:                                    # Done finding accelsa and vels, can finally
#    i.pos = np.array([i.xhist[-1],i.yhist[-1]])
  
#  for i in planets:
#    for j in planets:
#      if j != i:
#        collision = distcalc(i,j)
#        if collision < mindist:
#          mindist = collision
#      else:
#        break
#
#  if mindist < .005:
#    break                      # Should shrink time increments during close encounters

  time += dt                                   # Include a collision test. Based on dist or on x and y flip

#print(time, mindist)

rkstop = timer()

print(time, time / dt)
print(rkstop-rkstart)

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


# In[8]:


# Test of max movement in one time increment for checking appropriate proximity limits.

#leap = 0
#
#for i in planets:
#    for j in range(len(i.xhist)-1):
#        jump = ( (i.xhist[j]-i.xhist[j+1]) * (i.xhist[j]-i.xhist[j+1]) +                 (i.yhist[j]-i.yhist[j+1]) * (i.yhist[j]-i.yhist[j+1]) ) ** .5
#        if jump > leap:
#            leap = jump
#            
#print(leap)
#
#
