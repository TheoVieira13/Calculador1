def somar(y, x):
    return y + x

def subtrair(y, x):
    return y - x

def multiplicacao(y, x):
    return y * x

def divisao(y, x):
    if x != 0:
        return y / x
    else:
        return 'Erro não e possivel dividir por 0'
while True:
    try:    
        escolha = int(input("""1. Somar
2. Subtrair
3. Multiplicar
4. Dividir 
Digite sua escolha: """))
        if escolha in [1, 2, 3, 4]:
            break
        else:
            print('Erro opção invalida escolha novamente.')
    except ValueError:
        print('Erro digite um numero valido.')

num = float(input('Digite seu primeiro numero: '))
num2 = float(input('Digite seu segundo numero: '))

if escolha == 1:
    print(f'{num} + {num2} = {somar(num, num2)}')
elif escolha == 2:
    print(f'{num} - {num2} = {subtrair(num, num2)}')
elif escolha == 3:
    print(f'{num} X {num2} = {multiplicacao(num, num2)}')
elif escolha == 4:
    print(f'{num} / {num2} = {divisao(num, num2)}')
