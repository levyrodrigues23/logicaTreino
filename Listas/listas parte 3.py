lista1 = ["a", "c", "b"]
lista2 = ["d", "e", "f"]

lista1.extend(lista2) # com o extend, conseguiremos unir duas listas
print(lista1)

lista1.remove("a") #remove um item da lista
print(lista1)

lista1.pop(2) # removendo pelo indice do elemento
print(lista1)

lista1.pop() # remove o ultimo elemento
print(lista1)

del lista1[0] # remove atraves do del, pega o indice
print(lista1)

lista1.clear() # removendo todos os itens da lista
print(lista1)

lista1.append("Maça") #append adiciona items  na lista
print(lista1)

lista1.insert(1, "goiaba") # adiciona o item no indice passado
print(lista1)

lista1.insert(0, "tangerina")
print(lista1)

if "pera" in lista1:
    print("existe  na lista")
else:
    print("nn tem a fruta que vosmice citou :(")

lista1[2] = "Melancia"

print(lista1)

lista1[1:2] = ["a", "b"]
print(lista1)
















