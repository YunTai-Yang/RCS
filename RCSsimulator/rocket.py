import numpy as np
import time

class Rocket:
  def __init__(self,RocketStatus,RCS):
    self.status = RocketStatus
    self.rcs = RCS

    self.timeFlow = 0
    self.landingTime = 0
    self.totalDrag = np.array([0,0,0])

    # Saved datas (for Visualization)
    self.positionlist = np.array([self.status.position])
    self.velocitylist = np.array([self.status.velocity])
    self.accellist    = np.array([self.status.acceleration])
    self.anglelist    = np.array([self.status.angle])
    self.angulerVelocitylist = np.array([self.status.angulerVelocity])
    self.masslist            = np.array([self.status.structureMass + self.status.propellantMass])
    self.massCenterlist      = np.array([self.status.massCenter])
    self.thrustlist          = np.array([self.status.thrust])
    self.totalDraglist       = np.array([self.totalDrag])
    self.timeFlowList            = np.array([0])

  # rocket launcher (in environment)
  def launch(self,environment,timestep = 0.001, simTime = 20):

    print('======start simulation======')
    time.sleep(1)

    while self.timeFlow <= simTime:
      # in burnning
      if self.timeFlow <= self.status.burnTime:
        environment.free_fall(self,timestep)

      # finish burnning
      else :
        self.status.thrust = np.array([0,0,0])

        # finish burnning but still fying
        if self.status.position[0] > 0:
          environment.free_fall(self,timestep)

        # landing
        else :
          if self.landingTime == 0:
            self.landingTime = self.timeFlow
          self.status.velocity  = np.array([0,0,0])
          self.status.acceleration     = np.array([0,0,0])
          self.status.angulerVelocity  = np.array([0,0,0])
          self.totalDrag               = np.array([0,0,0])

      # Save datas for Visualization
      self.saveDatas()

      # Progress
      if self.timeFlow%2 == 0:
        print("Progress : %.1f%%"%(self.timeFlow/simTime*100))
      self.timeFlow += timestep
      self.timeFlow = np.around(self.timeFlow,5)

    print('======finish simulation======')

  def saveDatas(self):
    self.positionlist = np.append(self.positionlist,np.array([self.status.position]),axis=0)
    self.velocitylist = np.append(self.velocitylist,np.array([self.status.velocity]),axis=0)
    self.accellist    = np.append(self.accellist,np.array([self.status.acceleration]),axis=0)
    self.anglelist    = np.append(self.anglelist,np.array([self.status.angle]),axis=0)
    self.angulerVelocitylist = np.append(self.angulerVelocitylist,np.array([self.status.angulerVelocity]),axis=0)
    self.masslist            = np.append(self.masslist,np.array([self.status.structureMass + self.status.propellantMass]),axis=0)
    self.massCenterlist      = np.append(self.massCenterlist,np.array([self.status.massCenter]),axis=0)
    self.thrustlist          = np.append(self.thrustlist,np.array([self.status.thrust]),axis=0)
    self.totalDraglist       = np.append(self.totalDraglist,np.array([self.totalDrag]),axis = 0)
    self.timeFlowList        = np.append(self.timeFlowList,np.array([self.timeFlow]),axis=0)