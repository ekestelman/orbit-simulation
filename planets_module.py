# Random planet generator
import numpy as np
import random

import_planets = True

class Planet:
  def __init__(self, name, mass, pos, vel):
     self.name = name
     self.mass = mass
     self.pos = np.array(pos)
     self.vel = np.array(vel)
     self.xhist = [pos[0]]
     self.yhist = [pos[1]]
     self.temppos = [None, None]
     self.tempvel = [None, None]

def distcalc(a):                                     # To center (0,0)
  return ( (a.pos[0])**2 + (a.pos[1])**2 )**.5

nplanets = 9

planets = []

# Ideas for mass assignment:
# 3*random.betavariate(2,2)
# random.expovariate(.5)

for i in range(nplanets):
  planets.append( Planet(str(i), random.expovariate(.5), [random.gauss(0, 8), random.gauss(0, 8)],\
                 [random.gauss(0, 0), random.gauss(0, 4)]) )
  planets[i].vel = np.array([random.gauss(-planets[i].pos[1], distcalc(planets[i])/5),\
                             random.gauss(planets[i].pos[0], distcalc(planets[i])/5)])
  for j in range(2):
    planets[i].vel[j] *= ( 10 * ((planets[i].pos[0]**2 + planets[i].pos[1]**2)**(.5))**(-1.5) )
    #if planets[i].pos[j] > 0:
    #  #planets[i].vel[j] = 8 * planets[i].vel[j]**(-.5)
    #  planets[i].vel[j] = 10 * planets[i].pos[j]**(-.5)
    #else:
    #  planets[i].vel[j] = -8 * (-planets[i].vel[j])**(-.5)
  #    j ** .5
  #  else:
  #    j *= -1
  #    j ** .5
  #    j *= -1
  print(planets[i].name, planets[i].mass, planets[i].pos, planets[i].vel)
