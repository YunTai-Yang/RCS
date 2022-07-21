import numpy as np
from transformer import Transformer
class Environment:
  def __init__ (self):
    self.g = np.array([0,0,9.81])                # m / s^2
    self.wind    = np.array([0,0,0])

  def free_fall(self,rocket,dt):
        T = rocket.status.thrust

        p_v = np.append(rocket.status.position,rocket.status.velocity)
        a_w = np.append(rocket.status.angle,rocket.status.angulerVelocity)

        m = rocket.status.structureMass + rocket.status.propellantMass

        A = np.array([[1, 0, 0, dt ,0 ,0],
                      [0, 1, 0, 0, dt ,0],
                      [0, 0, 1, 0, 0, dt],
                      [0, 0, 0, 1 ,0 ,0],
                      [0, 0, 0, 0, 1 ,0],
                      [0, 0, 0, 0, 0, 1]])

        B = np.array([[0.5*dt**2, 0,         0],
                      [0,         0.5*dt**2, 0],
                      [0,         0,         0.5*dt**2],
                      [dt,        0,         0],
                      [0,         dt,        0],
                      [0,         0,         dt]])

        con_vec = Transformer().body_to_earth(a_w[0:3])
        T = np.array(con_vec@T)

        a = T/m -self.g
        p_v = A@p_v + B@a

        rocket.status.position         = p_v[0:3]
        rocket.status.velocity         = p_v[3:6]
        rocket.status.angle            = a_w[0:3]
        rocket.status.anglulerVelocity = a_w[3:6]
        print(T)
        if not np.array_equal(T,np.array([0,0,0])):
            rocket.status.propellantMass  -= rocket.status.burnratio*dt
        # print(p_v)


        


