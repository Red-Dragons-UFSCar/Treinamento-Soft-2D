import numpy as np

class Vision:
    
    # retorna as coordenadas do robô
    def getPoseRobot(self):
        x = np.random.uniform(0, 150)
        y = np.random.uniform(0, 130)
        theta = np.random.uniform(-np.pi, np.pi)
        
        return (x, y, theta)
    
    # retorna as coordenadas da bola  
    def getPoseBall(self):
        x = np.random.uniform(0, 150)
        y = np.random.uniform(0, 130)
        
        return (x, y)