linha = 0

while linha < 3:
    coluna = 0
    while coluna < 3:
        print(linha, coluna)
        coluna += 1
    linha += 1

"""
ele verifica se coluna é menor que 3, depois que sair do loop, ele roda linha novamente
ate linha se tornar menor q 3

"""

#----------------------------------------------------------------------------------------

print("\n")

numeroInicial = 1
numeroFinal = int(input("digite um numero maior que 1"))

while numeroInicial <= numeroFinal:
    print(numeroInicial)
    numeroInicial += 1

    print("\n")

numero = 1
numeroPar = int(input("digite um numero maior que 1: "))

while numero <= numeroPar:
    if numero % 2 == 0:
        print(numero, end=" ")
    numero += 1

