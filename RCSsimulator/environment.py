import numpy as np
from transformer import Transformer

class Environment:
  def __init__ (self):
    # gravity
    self.g     = np.array([9.81,0,0])                # m / s^2
    self.wind  = np.array([0,0,0])

  # Kinematics
  def free_fall(self,rocket,dt):

        ''' Set Parameters'''
        # Thrust
        T = rocket.status.thrust
        # position and velocity
        p_v = np.append(rocket.status.position,rocket.status.velocity)
        # anguler and angulerVelocity
        a_w = np.append(rocket.status.angle,rocket.status.angulerVelocity)
        # mass
        m = rocket.status.structureMass + rocket.status.propellantMass

        # inertia
        I = 0.5*m*rocket.status.length**2
        # mass center to aero center
        mc2ac = np.array([rocket.status.aeroCenter - rocket.status.massCenter,0,0])
        # mass center to rocket bottom
        mc2bottom = np.array([-rocket.status.massCenter,0,0])
        # drag coefficient
        Cd = rocket.status.dragCoeff
        # cross section
        S = np.pi*rocket.status.diameter**2/4
        # rho
        if p_v[2] <= 35000:
            rho = 1.225*(1-1.8e-5*p_v[2])**5.656                                  ## calculate atmospheric density
        else :
            rho = 0.001

        # Kinematics / X = A@X + B@U / Kinetics / X = A@X + B@U
        ''' |x |      |1, 0, 0, dt ,0 ,0||x |     |0.5*dt**2, 0,           0|
            |y |      |0, 1, 0, 0, dt ,0||y |     |0,         0.5*dt**2,   0||ax|
            |z |  =   |0, 0, 1, 0, 0, dt||z |  +  |0,         0,   0.5*dt**2||ay|
            |Vx|      |0, 0, 0, 1 ,0 ,0 ||Vx|     |dt,        0,           0||az|
            |Vy|      |0, 0, 0, 0, 1 ,0 ||Vy|     |0,         dt,          0|
            |Vz|      |0, 0, 0, 0, 0, 1 ||Vz|     |0,         0,          dt|                                 
            p_v = A@p_v + B@a

            |roll  |      |1, 0, 0, dt ,0 ,0||roll  |     |0.5*dt**2, 0,           0|
            |pitch |      |0, 1, 0, 0, dt ,0||pitch |     |0,         0.5*dt**2,   0||Wax|
            |yaw   |  =   |0, 0, 1, 0, 0, dt||yaw   |  +  |0,         0,   0.5*dt**2||Way|
            |Wx    |      |0, 0, 0, 1 ,0 ,0 ||Wx    |     |dt,        0,           0||Waz|
            |Wy    |      |0, 0, 0, 0, 1 ,0 ||Wy    |     |0,         dt,          0|
            |Wz    |      |0, 0, 0, 0, 0, 1 ||Wz    |     |0,         0,          dt|
            a_w = A@a_w + B2@wa                                                               '''

        A = np.array([[1, 0, 0, dt ,0 ,0],
                      [0, 1, 0, 0, dt ,0],
                      [0, 0, 1, 0, 0, dt],
                      [0, 0, 0, 1 ,0 ,0],
                      [0, 0, 0, 0, 1 ,0],
                      [0, 0, 0, 0, 0, 1]])

        A2 = np.array([[1, 0, 0, dt ,0 ,0],
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

        B2 = np.array([[0.5*dt**2,         0, 0],
                       [0,         0.5*dt**2, 0],
                       [0,         0, 0.5*dt**2],
                       [dt,        0,         0],
                       [0,         dt,        0],
                       [0,         0,         dt]])

        # Calculate thrust and transform thrust
        M = Transformer().body_to_earth(a_w[0:3])
        N = np.array([0,10,0])
        T = T
        T = np.array(M@T)        
        torqe_T = np.around(np.cross(M@mc2bottom,T),10)
        # Calculate drag and transform drag
        D = -0.5*rho*S*Cd*np.linalg.norm(p_v[3:6])*np.array(p_v[3:6])

        
        torqe_D = np.cross(M@mc2ac,D)


        # Calculate total acceleration
        total_accel = (T+D)/m -self.g
        p_v = A@p_v + B@total_accel

        # Calculate total moment 
        total_anguler_accel = (torqe_T+torqe_D)/I

        a_w = A2@a_w + B2@total_anguler_accel


        if rocket.timeFlow <= 3:
            rocket.status.propellantMass  -= rocket.status.burnratio*dt

        # Update status
        rocket.status.position         = p_v[0:3]
        rocket.status.velocity         = p_v[3:6]
        rocket.status.acceleration     = total_accel

        rocket.status.angle            = a_w[0:3]
        rocket.status.angulerVelocity  = a_w[3:6]

        rocket.totalDrag        = D


        


