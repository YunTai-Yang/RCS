import numpy as np

class Rocket:
  def __init__(self,RocketStatus,RCS):
    self.status = RocketStatus
    self.rcs = RCS
    self.realTime = 0

    self.positionlist = np.array([self.status.position])
    self.velocitylist = np.array([self.status.velocity])
    self.accellist    = np.array([self.status.acceleration])
    self.anglelist    = np.array([self.status.angle])
    self.angulerVelocitylist = np.array([self.status.angulerVelocity])
    self.masslist            = np.array([self.status.structureMass + self.status.propellantMass])
    self.massCenterlist      = np.array([self.status.massCenter])
    self.timeList            = np.array([0])

  def launch(self,environment,timestep = 0.001, simTime = 20):


    while self.realTime <= simTime:
      if self.realTime <= self.status.burnTime:
        pass
      else :
        self.status.thrust = np.array([0,0,0])

      environment.free_fall(self,timestep)
      # print(realTime)
      
      self.saveDatas()
      self.realTime += timestep
      self.realTime = np.around(self.realTime,5)

  def saveDatas(self):
    self.positionlist = np.append(self.positionlist,np.array([self.status.position]),axis=0)
    self.velocitylist = np.append(self.velocitylist,np.array([self.status.velocity]),axis=0)
    self.accellist    = np.append(self.accellist,np.array([self.status.acceleration]),axis=0)
    self.anglelist    = np.append(self.anglelist,np.array([self.status.angle]),axis=0)
    self.angulerVelocitylist = np.append(self.angulerVelocitylist,np.array([self.status.angulerVelocity]),axis=0)
    self.masslist            = np.append(self.masslist,np.array([self.status.structureMass + self.status.propellantMass]),axis=0)
    self.massCenterlist      = np.append(self.massCenterlist,np.array([self.status.massCenter]),axis=0)
    self.timeList            = np.append(self.timeList,np.array([self.realTime]),axis=0)