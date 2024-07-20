import mod_func as mf

if __name__ == '__main__':
    mf.mensagem()

    num = int(input('Digite um número inteiro: '))

    print(f'\nCalcular fatorial do número: ')
    fat = mf.fatorial(num)
    print(f'Ofatorial é {fat}')

    print(f'\nCalcular sequencia de fibonacci do número: ')
    fat = mf.fibo(num)
    print(f'Ofatorial é {fat}')
  