def multiplica(*args):
    total = 1
    for num in args:
        total *= num
    return total

multiplicacao = multiplica(10, 1, 3)

print(multiplicacao)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

saida = par_impar(4)
print(saida)
