'''Escrever um programa em Python que leia um vetor V1 de n posições e gere um vetor V2 de tamanho n que é o vetor V1 invertido.'''

n = 5
v1 = list(range(0,n))
v2 = v1[:]
v2.reverse()
print(v2)