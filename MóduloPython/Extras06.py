'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
quantos espaços em branco existem na frase. quantas vezes aparecem as vogais a, e, i, o, u.'''

frase = input("Digite uma frase: ")
contador = {' ': 0, 'a': 0, 'e':0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
  if letra in contador.keys():
    contador[letra] += 1
  
print(f"A letra \'a\' aparece {contador['a']} vezes")