#importações de lib
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("Lista 2/Dados.csv", names=['time','x','y','z','index'])

#legendas
titulo="Acelerometro"
eixotempo="Tempo"
eixox="Eixo X"

#legendas
plt.title(titulo)
plt.ylabel(eixotempo)
plt.xlabel(eixox)

#Plotagem
plt.plot(df['time'],df['x'],label="Amostra de X")
plt.legend()
plt.show()

