import matplotlib.pyplot as plt
import numpy as np

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

del planets[nplanets:]                                 # This is the easier way!

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

