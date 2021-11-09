'''Digite um nome, calcule e retorne quantas letras tem esse nome.'''

'''Forma01'''
txt = input("Digite um nome: ")
print(len(txt) - txt.count(" "))

'''Forma02'''
print(len(txt.replace(' ', '')))

'''Forma03'''
aux = txt.split()
print(len(''.join(aux)))