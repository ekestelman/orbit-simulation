import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
#from euler_orbit import planets
from rk2_orbit import planets

nplanets = len(planets)
#nplanets = 1, lessplanets = True
sample = 5                                    # only use i*(sample)th elements. Need more (lower) for rk
frames = 2 * int(len(planets[0].xhist) / sample)   # *2 to get out of range
print(len(planets[0].xhist), frames)
xmin = 0
xmax = 0
ymin = 0
ymax = 0

#for i in planets:                              # Still good if want big picture but only nplanets
#  if min(i.xhist) < xmin:
#    xmin = min(i.xhist)
#  if max(i.xhist) > xmax:
#    xmax = max(i.xhist)
#  if min(i.yhist) < ymin:
#    ymin = min(i.yhist)
#  if max(i.yhist) > ymax:
#    ymax = max(i.yhist)
for i in range(nplanets):                       # Better for custom nplanets
  if min(planets[i].xhist) < xmin:
    xmin = min(planets[i].xhist)
  if max(planets[i].xhist) > xmax:
    xmax = max(planets[i].xhist)
  if min(planets[i].yhist) < ymin:
    ymin = min(planets[i].yhist)
  if max(planets[i].yhist) > ymax:
    ymax = max(planets[i].yhist)

xmax += 0.5
ymax += 0.5
ymin -= 0.5
xmin -= 0.5

xinit = []
yinit = []
for i in range(nplanets):
  xinit.append(planets[i].xhist[0])
  yinit.append(planets[i].yhist[0])

xmin = min(xinit) - 0.5
xmax = max(xinit) + 0.5
ymin = min(yinit) - 0.5
ymax = max(yinit) + 0.5

goodplanets = [i for i in planets]

def init():
    line[0].set_data([], [])
    #line1.set_data([],[])
    return line,

#def run(orbit):
#    x, y = orbit
#    xdata.append(x)
#    ydata.append(y)
#    line.set_data(xdata, ydata)
#    return line,
#
#def get_data():
#    for i in range(len(sun.xhist)):
#        yield sun.xhist[i], sun.yhist[i]                 # [i] for blank, full list for full drawing
#    #return sun.xhist, sun.yhist
    
def animate(i):
    for j in range(nplanets):
      xdata[j].append(planets[j].xhist[i*sample])
      ydata[j].append(planets[j].yhist[i*sample])
      #xdata1.append(planets[1].xhist[i*sample])
      #ydata1.append(planets[1].yhist[i*sample])
      line[j].set_data(xdata[j],ydata[j])
      #line1.set_data(xdata1,ydata1)
      xmin,xmax = ax.get_xlim()
      ymin,ymax = ax.get_ylim()
      newlim = False
      for k in goodplanets:
        if xdata[j][i] + 0.5 > xmax:
          xmax = xdata[j][i] + 0.5
          newlim = True
        elif xdata[j][i] - 0.5 < xmin:
          xmin = xdata[j][i] - 0.5
          newlim = True
        if ydata[j][i] + 0.5 > ymax:
          ymax = ydata[j][i] + 0.5
          newlim = True
        elif ydata[j][i] - 0.5 < ymin:
          ymin = ydata[j][i] - 0.5
          newlim = True
      if newlim:
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin,ymax)
    #if i == frames:                                      # Doesn't work
    #  for j in range(nplanets):
    #    del xdata[j][:]
    #    del ydata[j][:]
    #    line[j].set_data(xdata[j], ydata[j])
    return line[0],

fig, ax = plt.subplots()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
#line, = ax.plot([], [], lw=2)
#line1, = ax.plot([], [], lw=2)
xdata, ydata = [[] for i in range(nplanets)], [[] for i in range(nplanets)]
#xdata1, ydata1 = [], []

line = [None for i in range(nplanets)]

for i in range(nplanets):
  line[i], = ax.plot([], [], lw=planets[i].mass**0.2)   # log or root?

#ani = animation.FuncAnimation(fig, run, get_data, interval=10, init_func=init)
# Smaller interval for faster animation??
ani = animation.FuncAnimation(fig, animate, frames, interval=1, init_func=init)
# blit=False by default, return in animate and init do nothing. Doesn't work with blit=True.
plt.gca().set_aspect('equal')
plt.show()

