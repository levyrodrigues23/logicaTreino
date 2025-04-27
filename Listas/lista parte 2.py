listaMinMax = [1, 2, 3, 4, 5]

print(min(listaMinMax))
print(max(listaMinMax))
listaNumerosDe1ate10 = [posicao for posicao in range(101) if posicao <= 10 ]
print(listaNumerosDe1ate10) #ele percorre o numero ate oq foi declarado no for

listaDoisEmDois = list(range(0, 100, 2)) # imprime a sequencia do start, stop e step
print(listaDoisEmDois)

listaVeiculos = ["carros", "motos", "bikes", "aviões"]
listaCopiada = listaVeiculos.copy() #metodo para copiar a lista
print(listaCopiada)
print("\n")


listaJoi = listaMinMax + listaVeiculos
print(listaJoi)
"""
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

for item in l2:
    l1.append(item) #append incluiu valores no final, podendo juntar as listas

print(l1)
"""
lista1 = ["levy"]
lista2 = ["levy2"]

for item in lista1:
    lista2.append(item) # adiciona ao final da lista o item dps que o proprio percorre

print(lista2)
