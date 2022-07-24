import numpy as np

class RocketStatus:
  def __init__(self):
    # 로켓의 헤딩 방향  : x / roll
    # 로켓의 앞쪽      : y / pitch
    # 로켓의 오른쪽     : z / yaw

    # 아래의 변수는 (x,y,z) 또는 (roll, pitch, yaw) 순서.

    # 시각화시 x -> z   /   y -> x   /   z -> y   로 표현

    self.position     = np.array([0,0,0])         # m 
    self.velocity     = np.array([0,0,0])         # m/s
    self.acceleration = np.array([0,0,0])         # m/s^2

    self.angle               = np.array([0,0,10])*np.pi/180  # ras
    self.angulerVelocity     = np.array([0,0,0])*np.pi/180   # rad / s
    self.angulerAcceleration = np.array([0,0,0])*np.pi/180   # rad / s^2

    self.thrust   = np.array([50,0,0])            # x,y,z thrust in rocket inertia frame
    self.burnTime = 10                            # sec

    self.structureMass  = 3                       # kg
    self.propellantMass = 0.5                     # kg
    self.burnratio      = self.propellantMass/self.burnTime


    self.massCenter = 0.6                         # m from bottom
    self.aeroCenter = 0.45                        # m from bottom

    self.length   = 1.3                           # m
    self.diameter = 0.09                          # m

    self.dragCoeff  = 0.5