def ordenaLista(lista):
    
    listaX=list((sorted(filter(lambda k: "x" in k,lista))))
    

    print("Lista de X ordenada ->",listaX)
    
   
   

lista = ['milho', 'xyz', 'amora', 'xicara', 'abacaxi']
ordenaLista(lista)