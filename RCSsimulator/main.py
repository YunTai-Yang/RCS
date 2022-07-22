from Visualization import Visualizer
from environment import Environment
from rocketStatus import RocketStatus
from rcsThruster import RCS
from rocket import Rocket

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

from transformer import Transformer


if __name__ == '__main__':

  rocketStatus = RocketStatus()
  rcs_thruster = RCS()
  rocket = Rocket(rocketStatus, rcs_thruster)

  # Simulation Time (sec)
  simTime = 20
  timestep = 0.001

  # Simulation
  rocket.launch(environment = Environment(),timestep = timestep, simTime = simTime)

  # Visualization
  # which = ['Vx','Vy','Vz','V','Ax','Ay','Az','A','roll','pitch','yaw','','Wx','Wy','Wz','','Mass','Thrust','Drag']
  which = ['Vz','Az','yaw','Wz']
  # which = '3d'
  Visualizer(rocket,simTime,timestep,which)

  '''
    witch :

     3d

     or

     Vx  Vy  Vz  V
     Ax  Ay  Az  A

     roll pitch yaw
     Wx   Wy   Wz

     Mass Thrust Drag

     (Everything you choose)

     '''