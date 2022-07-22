from environment import Environment
from rocketStatus import RocketStatus
from rcsThruster import RCS
from rocket import Rocket

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
# https://jehyunlee.github.io/2021/07/10/Python-DS-80-mpl3d2/

if __name__ == '__main__':
  rocketStatus = RocketStatus()
  rcs_thruster = RCS()
  rocket = Rocket(rocketStatus, rcs_thruster)
  simTime = 20
  rocket.launch(environment = Environment(),timestep = 0.01, simTime = simTime)
  print(rocket.positionlist)
  
  fig = plt.figure()
  ax = fig.add_subplot(331)       # Trajectory
  ax2 = fig.add_subplot(332)      # Mass
  ax3 = fig.add_subplot(333)      # Roll
  ax4 = fig.add_subplot(334)      # Pitch
  ax5 = fig.add_subplot(335)      # Yaw
 
  ax.plot(rocket.positionlist[:,0],rocket.positionlist[:,2])
  ax5.plot(rocket.timeList,rocket.anglelist[:,1])
  # ax.plot(rocket.positionlist[:,0],rocket.positionlist[:,2])
  # ax2.plot(rocket.timeList,rocket.masslist)

  ax.set_xlim(0,500)
  ax.set_ylim(0,500)
  # ax.set_zlim(0,300)

  # ax2.set_xlim(0,simTime)
  # ax2.set_ylim(rocket.masslist[-1]-1,rocket.masslist[0]+1)

  plt.show()