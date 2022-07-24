from Visualization import Visualizer
from environment import Environment
from rocketStatus import RocketStatus
from rcsThruster import RCS
from rocket import Rocket


if __name__ == '__main__':

  rocketStatus = RocketStatus()
  rcs_thruster = RCS()
  rocket       = Rocket(rocketStatus, rcs_thruster)

  # Simulation Time (sec)
  simTime  = 30
  timestep = 0.001

  # Simulation
  rocket.launch(environment = Environment(),timestep = timestep, simTime = simTime)

  # Visualization
  # which = ['Vx','Vy','Vz','V','Ax','Ay','Az','A','roll','pitch','yaw','','Wx','Wy','Wz','','Mass','Thrust','Drag']
  # which = ['roll','pitch','yaw','Dragx','Dragy','Dragz']
  which = '3d'
  Visualizer(rocket,simTime,timestep,which)

  '''
    which :

     3d

     or

     Vx  Vy  Vz  V
     Ax  Ay  Az  A

     roll pitch yaw
     Wx   Wy   Wz

     Mass Thrust Drag

     (Everything you choose)

     '''
