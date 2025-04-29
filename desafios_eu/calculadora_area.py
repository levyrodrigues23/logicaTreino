import math

print("===============\nCalculadora de Área\n===============")

formas = int(input( "Escolha uma forma:\n"
    "1) Triângulo\n"
    "2) Retângulo\n"
    "3) Quadrado\n"
    "4) Círculo\n"
    "5) Sair\n"))

if formas == 1:
    base = int(input("base: "))
    altura = int(input("altura: "))
    area_triangulo = (base * altura) / 2
    print(f"A área do seguinte triângulo equivale a {int(area_triangulo)}")

elif formas == 2:
    base = int(input("base: "))
    altura = int(input("altura: "))
    area_retangulo = int(base * altura)
    print(f"o valor desta area é {int(area_retangulo)}")
elif formas == 3:
    lado = int(input("digite o valor do lado do quadrado: "))
    area_quadrado = lado * 2
    print(f"o valor desta area é {int(area_quadrado)}")
elif formas == 4:
    raio = int(input("digite para mim o valor do raio: "))
    area_circulo = math.pi * raio
    print(f"o valor desta area é {float(area_circulo)}")
elif formas == 5:
    print("obrigado por nada :) ")


