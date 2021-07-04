#Apresente um plot de alguns segundos dos dados de acelerômetro do dataset:
#https://archive.ics.uci.edu/ml/datasets/Activity+Recognition+from+Single+Chest-Mounted+Accelerometer#
#Use a função read_csv() para abrir os arquivos

#importações de lib
import pandas as pd
import matplotlib.pyplot as plt

#import CSV
df= pd.read_csv("Lista 2/Dados.csv", names=['time','x','y','z','index'])

#legendas
titulo="Acelerometro"
eixotempo="Tempo"


#Plotagem
plt.title(titulo)
plt.ylabel(eixotempo)

plt.plot(df['time'],df['x'],label="Amostra de X")
plt.plot(df['time'],df['y'],label="Amostra de Y")
plt.plot(df['time'],df['z'],label="Amostra de Z")
plt.legend()
plt.show()

