#from euler_orbit import planets, plt
from rk2_orbit import planets, plt

for i in planets:
  plt.plot(i.xhist,i.yhist)

plt.gca().set_aspect('equal')

plt.show()
