def pesquisa_binaria(lista,item): 
    baixo = 0
    alto = len(lista) - 1
    contador = 0
    while baixo <=alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        print("meio: ", meio)
        
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else: 
            baixo = meio + 1 
    
    return None

minha_lista =[1,3,5,7,9 ]
print ("Resultado da pesquisa: ",pesquisa_binaria(minha_lista,3))
print ("Resultado da pesquisa: ",pesquisa_binaria(minha_lista,-1))