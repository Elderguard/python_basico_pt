lista = [1,2,3,4,5,22]
print(len(lista)) #imprime o tamanho (nro elementos) da lista

lista.insert(2,22) #insere na posição 2 o elemento 22
lista.append(33) #insere o 33 no final da lista
print(lista)
print(len(lista))

#remove elemento na posição 4 da lista

del lista[4]
print(lista)
print(len(lista))

#remove o elemento 22 da lista. Apenas o primeiro valor 22 encontrado será removido
lista.remove(22)
#lista.remove(66) -> remover elemento que não existe dá erro
print(lista)
print(len(lista))
