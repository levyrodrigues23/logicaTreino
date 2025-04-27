


"""
funcao any() retorna true ou false...basicamente voce pode fazer um any(letra.isupper for letra in senha)...elel ira percorrer tudo e verifiicar se tem alguma letra maiuscula
ele faz isso com todas as outras variaveis...exemplos
isupper: maiuscula
islower: minuscula
isdigit: numero
isalnum: caracteres especiais

logo dps cria um if, se tudo tiver true, retorna true, caso nn, é false. dps passa a senha pro input e dps passa
um if fora da funcao.. se validar senha passando o parametro senha for true...retorna uma mensagem, e vice versa
 
"""
#fazendo dps de explicado e compreendido

def validar_senha(senha):
    letra_maiuscula = any(letra.isupper() for letra in senha)
    letra_minuscula = any(letra.islower() for letra in senha)
    numero = any(letra.isdigit() for letra in senha)
    caractere_especial = any(not letra.isalnum() for letra in senha)

    if len(senha) >= 8 and letra_maiuscula and letra_minuscula and numero and caractere_especial:
        return True
    else:
        return False

senha = str(input("digite a senha:"))

if validar_senha(senha):
    print("sua senha esta bem feita")
else:
    print("vai ter que adicionar alguma coisa que esta faltando ai amiguinho :)")