#Encontre em um texto os nomes próprios e os retorne em uma lista.
#Utilize o Regex (‘import re’) e a função findall(). 
#Na versão básica, retorne todas as palavras que iniciam com maiúscula.

import re

texto='Victor rangel,Gabriel maia'
padrao=[]

padrao = re.findall(r'[A-Z][a-z]+',texto)

if padrao:
    print(padrao)
else:
    print("Não existe nomes próprios")
    
