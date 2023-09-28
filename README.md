# N-Body Orbit Simulation

Orbit simulation code using RK2

## Basic Usage:

```
python plot_orbit.py
```

Runs the simulation and outputs a still image of the planets' trajectories.

```
python nbody_ani.py
```

Runs the simulation and outputs an animation of the planets' trajectories.

The other files are modules for running the simulation.

## Screenshots

Below is a screenshot of the the orbit simulation, showing the trajectory of 8 bodies. This simulation features a large central mass (blue) and other smaller bodies orbiting it. While the blue body exhibits some motion, the center of mass of the system is fixed at $(0, 0)$.

<!-- ![orbits](https://github.com/ekestelman/orbit-simulation/blob/master/Orbit%20Images/still_frame.png?raw=true) -->
<img src="https://github.com/ekestelman/orbit-simulation/blob/master/Orbit%20Images/still_frame.png?raw=true" width="50%" height="auto">

The plot below shows the distance of each body to its closest neighbor, as well as each body's velocity and acceleration, plotted against time.

<!-- ![plot](https://github.com/ekestelman/orbit-simulation/blob/master/Orbit%20Images/plot.png?raw=true) -->
<img src="https://github.com/ekestelman/orbit-simulation/blob/master/Orbit%20Images/plot.png?raw=true" width="90%">

Each extrema on the velocity plot and the acceleration plot are aligned. The maxima for the red body and blue body's velocities/accelerations are aligned because the red body is closest to the blue, giving it the greatest gravitational force (though this may not be the case if there were a sufficiently massive farther body). Despite always being the closest body to the blue, the red is not always the fastest moving.

## Requirements

Python 3.6.7

matplotlib 2.1.1

numpy 1.16.2
