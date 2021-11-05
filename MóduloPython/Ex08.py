'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

pag = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalhou no mês? "))
salario = pag * horas
print(f"O salário esse mês será R${salario}")