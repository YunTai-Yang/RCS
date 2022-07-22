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
        I = (1/12)*m*rocket.status.length**2

        mc2ac = np.array([0,0,rocket.status.aeroCenter - rocket.status.massCenter])
        mc2bottom = np.array([0,0,-rocket.status.massCenter])
        Cd = rocket.status.dragCoeff
        S = np.pi*rocket.status.diameter**2/4

        if p_v[2] <= 35000:
            rho = 1.225*(1-1.8e-5*p_v[2])**5.656                                  ## calculate atmospheric density
        else :
            rho = 0.001

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

        B2 = np.array([[0.5*dt**2, 0,         0],
                       [0,         0.5*dt**2, 0],
                       [0,         0,         0.5*dt**2],
                       [dt,        0,         0],
                       [0,         dt,        0],
                       [0,         0,         dt]])

        M = Transformer().body_to_earth(a_w[0:3])
        torqe_T = np.cross(mc2bottom,T)
        T = np.array(M@T)
        

        D = -0.5*rho*S*Cd*np.linalg.norm(p_v[3:6])*np.array(p_v[3:6])
        torqe_D = np.cross(mc2ac,D)
        D = np.array(M@D)
        

        total_accel = (T+D)/m -self.g
        p_v = A@p_v + B@total_accel

        total_anguler_accel = (torqe_T+torqe_D)/I
        a_w = A@a_w + B2@total_anguler_accel

        rocket.status.position         = p_v[0:3]
        rocket.status.velocity         = p_v[3:6]
        rocket.status.angle            = a_w[0:3]
        rocket.status.anglulerVelocity = a_w[3:6]
        print(T, D)
        if not np.array_equal(T,np.array([0,0,0])):
            rocket.status.propellantMass  -= rocket.status.burnratio*dt
        # print(p_v)


        


