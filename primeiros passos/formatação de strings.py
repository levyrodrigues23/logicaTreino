nome = "cintia alves moreira"
print(nome)

print(len(nome))
print(nome[0])
print(nome[0:6])
print(nome[7:12])
print(nome[13:20])

"""
se eu colocar apenas os dois pontos, ele pega todo o resto da lista

"""
print(nome.upper())
"""
upper retorna as letras todas maiusculas
"""
print(nome.lower())

"""
lower retorna todas as letras minusculas
"""

notaProva = "tirei nota cinco na prova"
print(notaProva.replace("cinco", "dez "))

cpf = "123.123.123-45"

cpfPartes = cpf.split(".")

print(cpfPartes)

cpfPartes2 = cpfPartes[2].split("-")
print(cpfPartes2[0])
