import matplotlib.pyplot as plt
from PythonTreinamento import projPontoCircunferencia

def plotPonto(x, y):
    plt.plot(x, y, 'ro')  
    plt.axis('equal')  
    plt.show()


#x, y = 2, 3  
#r = 1  
#c1, c2 = 0, 0 
#x_proj, y_proj = projPontoCircunferencia(x, y, r, c1, c2)
#plotPonto(x_proj, y_proj)
