# Lista representa uma sequência de valores

# Sintaxe: nome_lista = [valores]

n1 = [5,7,6,8,9,]
n2 = [ 1, 6, 3, 0, 12, 4]



valores = n1 + n2

'''
valores[0] = 9

print(len(valores))
print(sorted(valores, reverse=True))
print(min(valores))
print(max(valores))
'''
'''

valores.append(13)
print(valores)
valores.pop()
print(valores)
valores.pop(3)
print(valores)
valores.insert(3,21)
print(valores)
print(12 in valores)

'''

planetas = ['Mercúrio', 'Vênus', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)
