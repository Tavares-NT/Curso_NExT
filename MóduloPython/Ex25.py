'''Construa uma pequena chave dicotômica para identificar uma determinada planta como membro de um dos principais grupos: Bryophyta, Pteridophyta, Gymnospermae ou Angiospermae. A identificação se dá com base na presença (1) ou ausência (0) de três caracteres: vascularização, sementes e flores. Utilize a tabela abaixo como referência.'''

vasc = 1
sem = 1
flor = 1

if vasc == 0 and sem == 0 and flor == 0:
  print("Pertence ao grupo Bryophyta.")
elif vasc == 1 and sem == 0 and flor == 0:
  print("Pertence ao grupo Pteridophyta.")
elif vasc == 1 and sem == 1 and flor == 0:
  print("Pertence ao grupo Gymnospermae.")
elif vasc == 1 and sem == 1 and flor == 1:
  print("Pertence ao grupo Angiospermae.")
else:
  print("Não pertece a nenhum dos grupos.")