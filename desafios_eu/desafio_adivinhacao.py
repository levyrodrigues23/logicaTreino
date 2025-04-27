import string # comando para poder manipular as strings...nesse caso, usamos para remover as pontuações para nao afetar a procura
from collections import Counter # ajuda a contar a frequencia que cada palavra aparece

# Passo 1: Abrir o arquivo
with open('texto', 'r') as arquivo:
    texto = arquivo.read() # aqui da pra ler o arquivo

# Passo 2: Preparar o texto (minúsculas e remover pontuação)
texto_limpo = texto.lower()  # Converte todo o texto para minúsculas
texto_limpo = texto_limpo.translate(str.maketrans('', '', string.punctuation))  # Remove pontuação

# Passo 3: Dividir o texto em palavras
palavras = texto_limpo.split()  # Divide o texto em uma lista de palavras

# Passo 4: Contar a frequência das palavras
contador = Counter(palavras)  # Conta quantas vezes cada palavra aparece

# Passo 5: Imprimir as palavras em ordem decrescente de frequência
for palavra, frequencia in contador.most_common():  # 'most_common()' retorna as palavras mais comuns
    print(f"{palavra}: {frequencia}")  # Imprime a palavra e sua contagem
