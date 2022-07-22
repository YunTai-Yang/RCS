import numpy as np

class Transformer:
  def __init___(self):
      pass
  
  # Make transform matrix M = yaw@pitch@roll
  def body_to_earth(self, bodyAngle):

      roll   = bodyAngle[0]
      pitch  = bodyAngle[1]
      yaw    = bodyAngle[2]

      r = np.array([[1,           0,            0],
                    [0, np.cos(roll), -np.sin(roll)],
                    [0, np.sin(roll),  np.cos(roll)]])


      p= np.array([[ np.cos(pitch), 0, np.sin(pitch)],
                    [             0, 1,             0],
                    [-np.sin(pitch), 0, np.cos(pitch)]])


      y = np.array([[np.cos(yaw), -np.sin(yaw), 0],       
                    [np.sin(yaw),  np.cos(yaw), 0],
                    [          0,            0, 1]])




            
      transformation_mtx = p@r@y

                  
      return transformation_mtx