"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite seu idade: ')

print(30 * '-')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Sua idade é: {idade}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome POSSUI espaco(s).')
    else:
        print('Seu nome NAO possui espaco(s).')

    print(f'Seu nome tem: {len(nome)} caracteres.')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print()
    print('Desculpe, você deixou campos vazios.')





# if nome and idade:
#     print(f'Seu nome é: {nome}')
#     print(f'Sua idade é: {idade}')
#     print(f'Seu nome invertido é: {nome[::-1]}')
#     print(f'A primeira letra do seu nome é: {nome[0]}')
#     print(f'A última letra do seu nome é: {nome[-1]}')
#     print()
# else:
#     print()
#     print('Desculpe, você deixou campos vazios.')

# if ' ' in nome:
#     print('Seu nome possui espaco(s).')
# elif ' ' not in nome:
#     print('Seu nome nao possui espaco(s).')




# elif ' ' in nome:
#     print(f"Seu nome: {nome}, tem espacos.")
# elif ' ' not in nome:
#     print(f"Seu nome: {nome}, NÃO tem espacos.")
# else:
#     print( f'SAIU NO ELSE')


