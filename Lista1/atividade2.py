#Faça uma função que, dado uma lista de strings, retorne uma lista com as 
#strings ordenadas, exceto as strings que iniciam com ‘x’, as quais devem 
#vir no início da lista retornada. Por exemplo: ['milho', 'xyz', 'amora', 'xicara', 'abacaxi'] 
#resulta em: ['xicara', 'xyz', 'abacaxi', 'amora', 'milho']
#Dica: crie duas listas, uma para palavras que iniciam com ‘x’ e outra não). 
#Para cada palavra armazene na lista correspondente. Ao final, ordene cada lista e junte uma à outra. 

def ordenarString(vetor):
    list=vetor
    list2 = []

    list.sort()

    # percorre lista procurando elementos que comecem com 'x'
    for itens in list:
        if itens[0] == 'x':
            list2.append(itens)

    # ordena os elementos da list2  
    list2.sort()

    # inclui os elementos que não são x na nova lista
    for itens in list:
        if itens[0] != 'x':
            list2.append(itens)
            
    list
    print(list)

    # mata a primeira lista
    list = []
    print(list2)



vetor=['milho' , 'xyz', 'amora', 'xicara', 'abacaxi']
ordenarString(vetor)