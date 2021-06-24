#Faça uma função que, dado uma lista de strings, retorne uma lista com as 
#strings ordenadas, exceto as strings que iniciam com ‘x’, as quais devem 
#vir no início da lista retornada. Por exemplo: ['milho', 'xyz', 'amora', 'xicara', 'abacaxi'] 
#resulta em: ['xicara', 'xyz', 'abacaxi', 'amora', 'milho']
#Dica: crie duas listas, uma para palavras que iniciam com ‘x’ e outra não). 
#Para cada palavra armazene na lista correspondente. Ao final, ordene cada lista e junte uma à outra. 

def ordenaLista(lista):
    
    listaX=list(sorted(filter(lambda k: "x" in k,lista)))
    
    listaRestante=list(sorted(filter(lambda k: "x" not in k,lista)))
    
    print("Lista de X ordenada ->",listaX)
    
    print("Lista Restante ordenada ->",listaRestante)

    print("Lista Final ->",listaX+listaRestante)
   

lista = ['milho', 'xyz', 'amora', 'xicara', 'abacaxi']
ordenaLista(lista)