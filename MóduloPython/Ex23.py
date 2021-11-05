'''Crie um programa para um circo, no qual dada a idade de uma pessoa, seja indicado o valor do ingresso segundo as regras:
a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita;

b) a entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais;

c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais;

d) estudantes e professores pagam meia-entrada.'''

idade = int(input("Informe a idade: "))
if idade < 4 or idade > 60:
  print("A entrada será gratuita.")
elif idade >= 4 and idade < 18:
  entrada = 20
  categoria = input("Você é estudante ou professor (S / N): ")
  if categoria.upper() == "S":
    print(f"A entrada será R${entrada/2}")
  else:
    print(f"A entrada será R${entrada}.")
else:
  entrada = 30
  categoria = input("Você é estudante ou professor (S / N): ")
  if categoria.upper() == "S":
    print(f"A entrada será R${entrada/2}")
  else:
    print(f"A entrada será R${entrada}.")