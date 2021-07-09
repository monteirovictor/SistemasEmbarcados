#importações de lib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#import CSV
df= pd.read_csv("Lista3/Dados.csv", names=['tempo','x','y','z','index'])

columX=np.array(df['x'])

#Estatística Descritiva

media=np.mean(columX)
mediana=np.median(columX)
variancia=np.var(columX)
desvio=np.std(columX)

print(media)
print("\n\n")
print(mediana)
print("\n\n")
print(variancia)
print("\n\n")
print(desvio)
