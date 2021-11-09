'''Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.'''

nomeCompleto = input("Digite seu nome completo: ")
nomeCompleto = nomeCompleto.lower()
vogais = "a","e","i","o","u"
for i in range(0, len(vogais)):
  nomeSemVogais = nomeCompleto = nomeCompleto.replace(vogais[i],"")
print(nomeSemVogais)