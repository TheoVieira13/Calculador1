def calculadora():
    while True:
        num_1 = input('Digite o primeiro numero: ')
        num_2 = input('Digite o segundo numero numero: ')
        operador = input('Digite o operador (+-/*): ')

        numeros_validos = None

        num_1_float = 0
        num_2_float = 0

        try:
            num_1_float = float(num_1)
            num_2_float = float(num_2)
            numeros_validos = True
        except:
            numeros_validos = None

        if numeros_validos is None:
            print('Um ou ambos os numeros digitados são invalidos. ')
            continue

        operadores_validos = '+-/*'

        if operador not in operadores_validos:
            print('Operador invalido.')
            continue

        if len(operador) > 1:
            print('Digite apenas um operador.')
            continue

        if operador == '+':
            print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
        elif operador == '-':
            print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
        elif operador == '/':
            if num_2_float == 0:
                print('Não e possivel dividir por 0.')
            else:
                print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
        else:
            print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
            
        sair = input('Deseja sair? [S]im ').lower().startswith('s')

        if sair:
            print('Finalizando!')
            break
calculadora()
