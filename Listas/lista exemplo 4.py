listaNomes = ["cristionel ronaldete","valentina","julia","levy"]

for i in listaNomes:
    print(i) #retorna cada item da lista

print("\n\n")

[print(item) for item in listaNomes] # imprime o item com o for numa linha só

i = 0  # Inicializa i antes do loop
while i < len(listaNomes):
    print(listaNomes[i])
    i += 1  # Forma mais compacta de fazer i = i + 1
