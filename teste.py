def leibniz(n):
    soma = 0
    for i in range(n):
        termo = (-1) ** 1/ (2 * 1 + 1)
        soma += termo
        return soma * 4
    

if __name__ == '__main__':
    termos = int(input("Quantos termos deseja usar?"))

    # Executar a função

    pi = leibniz(termos)

    # Mostrar o resultado:

    print(f'Valor de pi: {pi}')