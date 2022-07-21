import numpy as np

class Transformer:
  def __init___(self):
      pass
  
  def body_to_earth(self, bodyAngle):

      roll   = bodyAngle[0]
      pitch  = bodyAngle[1]
      yaw    = bodyAngle[2]
      
      r = np.array([[np.cos(roll), -np.sin(roll), 0],       
                    [np.sin(roll),  np.cos(roll), 0],
                    [          0,            0, 1]])

      p = np.array([[1,           0,            0],
                    [0, np.cos(pitch), -np.sin(pitch)],
                    [0, np.sin(pitch),  np.cos(pitch)]])

      y= np.array([[ np.cos(yaw), 0, np.sin(yaw)],
                    [             0, 1,             0],
                    [-np.sin(yaw), 0, np.cos(yaw)]])

            
      transformation_mtx = y@p@r

                  
      return transformation_mtx