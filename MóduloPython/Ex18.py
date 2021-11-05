'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

import math
tamArquivo = float(input("Qual o tamanho do arquivo para download (em MB)? "))
velLink = int(input("Qual a velocidade do link de internet (em Mbps)? "))
velLink = velLink * 0.125
tempoDownload = math.ceil(tamArquivo / velLink)
minutos = tempoDownload // 60
segundos = tempoDownload % 60

print(f"O tempo aproximado de download será de {minutos} minutos e {segundos} segundos.")