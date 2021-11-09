'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

download = float(input('Digite o tamanho do arquivo: '))
velocidade = float(input('Digite a velocidade da NET: '))

print(f'O tempo aproximado de download deste aquivo de {download}MB é de {round(download/(velocidade/8)/60,1)} minutos')