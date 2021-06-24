#Desenvolva uma função em Python que retorne o número de palavras de uma 
#string recebida como argumento. Para tanto, explore a função split().
#Adicionais: carregue um texto de um arquivo para passar como parâmetro para a função do usuário. 

def numPalavras(arquivo):
    linhas = arquivo.readlines()
    
    for linha in linhas:
        valores = linha.split()
        print("String Geral->",valores)
        
        for valor in valores:
         
            print("String -> [" + str(valor) + "] -> Quantidade:",len(valor))
               
arquivo = open("texto.txt")
numPalavras(arquivo)

