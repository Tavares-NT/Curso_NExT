'''Faça um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuario. Serão considerados letras maiúsculas e minúsculas '''

string = input("Digite uma string: ")
l1 = input("Primeira letra: ")
l2 = input("Segunda letra: ")
print(string.replace(l1,l2))