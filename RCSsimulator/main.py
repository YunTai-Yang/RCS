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
  simTime = 10
  rocket.launch(environment = Environment(),timestep = 0.01, simTime = simTime)
#   print(rocket.positionlist)
  
  fig = plt.figure()
  ax = fig.add_subplot(221,projection='3d')
  ax2 = fig.add_subplot(222)
  ax.plot(rocket.positionlist[:,0],rocket.positionlist[:,1],rocket.positionlist[:,2])

  ax2.plot(rocket.timeList,rocket.masslist)

  ax.set_xlim(-300,300)
  ax.set_ylim(-300,300)
  ax.set_zlim(0,300)

  ax2.set_xlim(0,simTime)
  ax2.set_ylim(rocket.masslist[-1]-1,rocket.masslist[0]+1)

  plt.show()