import numpy as np

class RocketStatus:
  def __init__(self):
    self.position     = np.array([0,0,0])         # m
    self.velocity     = np.array([0,0,0])         # m/s
    self.acceleration = np.array([0,0,0])         # m/s^2

    self.angle               = np.array([0,0,3])*np.pi/180  # ras
    self.angulerVelocity     = np.array([0,0,0])*np.pi/180  # rad / s
    self.angulerAcceleration = np.array([0,0,0])*np.pi/180  # rad / s^2

    self.thrust   = np.array([0,0,100])                           # N
    self.burnTime = 3                             # sec

    self.structureMass  = 3                       # kg
    self.propellantMass = 0.4                     # kg
    self.burnratio      = self.propellantMass/self.burnTime


    self.massCenter = 0.7                         # m from bottom
    self.aeroCenter = 0.45                        # m from bottom

    self.length   = 1.5                           # m
    self.diameter = 0.11                          # m

    self.dragCoeff  = 0.3