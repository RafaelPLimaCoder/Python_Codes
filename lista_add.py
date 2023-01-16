import os

lista = []

while True:
    
    acao = input('Selecione a opção:\n[i]nserir [a]pagar [l]istar (ou "sair"): ').lower()

    if acao == 'sair':
        break

    if acao == 'clear':
        os.system('clear')

    if acao == 'i':
        os.system('clear')
        print('Lista:')
        for indice, item in enumerate(lista):
            print(indice, item)

        lista.append(input('Digite o ítem para acrescentar: '))        

    elif acao == 'a':
        os.system('clear')
        print('Lista:')
        
        if len(lista) == 0:
            print('Lista está vazia.')

        for indice, item in enumerate(lista):
            print(indice, item)
        try:
            lista.remove(lista[int(input('Digite o ítem para apagar: '))])
        except ValueError:
            print('Digite apenas numeros inteiros.')
        except IndexError:
            print('Digite apenas índices presentes na lista.')
        # except: -> The Zen of Python: evite 'except(s) Exception(s)'
        #     print('Vocẽ digitou algo que não é nem inteiro nem esta na lista.')                  
            
    elif acao == 'l':
        os.system('clear')
        print('Lista:')
        
        if len(lista) == 0:
            print('Lista está vazia.')

        for indice, item in enumerate(lista):
            print(indice, item)
    
    else:
        print("Por favor, digite: 'i', 'a' ou 'l'.")
        print()
        
    
print('Você saiu do programa.')
    