import numpy as np

class RCS:
  def __init__(self):

    self.left_thrust      = np.array([0, -0.5, 0])    # N
    self.right_thrust     = np.array([0,  0.5, 0])    # N
    self.forward_thrust   = np.array([0,  0,   0])    # N
    self.backward_thrust  = np.array([0,  0,   0])    # N

    self.useTime_left     = 0      # sec
    self.useTime_right    = 0      # sec
    self.useTime_forward  = 0      # sec
    self.useTime_backward = 0      # sec

    self.update_thrust()

  def update_thrust(self):
    self.thrust = self.left_thrust + self.right_thrust + self.forward_thrust + self.backward_thrust

  def left(self,t):
    self.useTime_left += t      # using time
    self.left_thrust  = 0.8 * self.left_thrust    # N
    self.update_thrust()

  def right(self,t):
    self.useTime_right += t     # using time
    self.right_thrust   = 0.8 * self.right_thrust    # N
    self.update_thrust()

  def forward(self,t):
    self.useTime_forward += t     # using time
    self.forward_thrust   = 0.8 * self.forward_thrust    # N
    self.update_thrust()

  def backward(self,t):
    self.useTime_backward += t     # using time
    self.backward_thrust   = 0.8 * self.backward_thrust    # N
    self.update_thrust()