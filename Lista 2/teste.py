
from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd

df= pd.read_csv("Lista 2/Dados.csv", names=['time','x','y','z','index'])



titulo="Graph Scatterplot"
eixox="Eixo X"
eixoy="Eixo y"


#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#rodar
plt.scatter(df['time'],df['x'],label="meus pontos",color="k",marker="^",s=100)
plt.legend()
plt.plot(df['time'],df['x'],color="k",linestyle="--")

plt.show()