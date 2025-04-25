letras = ["a", "b", "c", "d", "e"]

for posicao in letras:
    print(posicao)

print("\n")

for i, letra in enumerate(letras):
    print(i, letra)


for i in "levy":
    print(i)

listaCores = ["azul", "amarelo", "verde", "cinza"]

for i in listaCores:
    if i == "laranja":
        print("Cor laranja encontrada com sucesso!")
        break #interromper do for, interrompe

        # a diferença do for para o while é que no while vc precisa acrescentar 1 no bloco de codigo
        # ja no for ele ja entende que vai fazer tal ação ate que aquilo seja interrompido
