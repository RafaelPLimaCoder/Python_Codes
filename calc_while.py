while True:
    print("CALCULADORA BÁSICA - (Para sair digite: 'S')")    
    
    numero_1 = input('Digite um número: ').lower()
    if numero_1 == 's':
        print('Você saiu.')
        break 
    operador = input('Digite o operador [+] [-] [/] [*]: ').lower()
    if operador == 's':
        print('Você saiu.')
        break 
    numero_2 = input('Digite outro número: ').lower()
    if numero_2 == 's':
        print('Você saiu.')
        break

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True     
    except:
        numeros_validos = None
        operador = None
    
    if numeros_validos is None:
        print('Número(s) digitados inválidos.')
        continue
    elif operador not in ['+', '-', '/', '*']:
        print('Operador inválido.')
        continue
    
    print((10*'-'),'Resultado',(10*'-'))

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    else:
        print('Se você ver isso algo deu errado.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break