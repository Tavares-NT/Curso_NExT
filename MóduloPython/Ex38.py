'''Crie uma lista de locais que você gostaria de conhecer no mundo, na ordem do local que você dá mais prioridade pra o local que você dá menos prioridade. Exiba a lista nas seguintes configurações:'''

viagem = ['Grecia', 'Tailandia', 'Italia', 'Escocia']

print(viagem)
print(sorted(viagem))
backup = viagem[:]
viagem.reverse()
print(viagem)
print(len(viagem))