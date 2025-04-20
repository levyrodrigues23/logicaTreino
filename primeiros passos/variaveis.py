nota1 = nota2 = nota3 = nota4 = media = 0
aluno = "jose levy"

print(aluno)

nota1 = 9
print(nota1)

aluno = input("digite o nome do aluno:")
nota1 = input("digite a nota 1")
nota2 = input("digite a nota 2 ")
nota3 = input("digite a nota 3")
nota4 = input("digite a nota 4")

media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4
print("aluno:", aluno)
print("sua média é:", media)
