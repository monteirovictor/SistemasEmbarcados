list = ['milho' , 'xyz', 'amora', 'xicara', 'abacaxi']
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