
import numpy as np
def rotacionarvetor(x, theta)
theta_rad = np.radians(theta)

R = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
              [np.sin(theta_rad), np.cos(theta_rad)]])

X = np.array(X)
V = R @ X

return V