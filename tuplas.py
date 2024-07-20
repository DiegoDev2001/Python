#São imutáveis

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He','Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
#t1 = (5,2,6,8,4,5,6,4,0,12,22,3,4,5)
print(max(t1))

# Operações não disponíveis em tublas: .sort(), .append(), .reverse(), .pop()...

'''
for elementos in elementos:
    print(f'Elemento quimico: {elemento}')
'''

'''
grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)
'''

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

'''
#codigo de erro
print(sorted(alcalinos))
print(alcalinos.sort())
'''
