
# o desafio é: faça um codigo na qual quando o numero for multiplo de 3 ou
# de 5, ele printe um texto especial
# caso nao obedeça nenhuma das instruções, permanece o numero e continua o outro

for i in range(1, 100):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

# achei facil e compreesivel