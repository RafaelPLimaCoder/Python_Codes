"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# import os

print()
print('### Preparando o Jogo ###')
palavra = input('Escolha a palavra: ')
palavra = palavra.lower()

print()
print('***Adivinhe a palavra***')
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    letra_digitada = letra_digitada.lower()
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
           palavra_formada += '*'
    print('palavra_formada: ', palavra_formada)

    if palavra_formada == palavra:
        #os.system('clear')
        print()
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra)
        print('Tentativas:', numero_tentativas)

        letras_acertadas = ''
        numero_tentativas = 0
        print()
        print('###Preparando o Jogo###')
        palavra = input('Escolha a palavra: ')
        palavra = palavra.lower()
        print()
        print('***Adivinhe a palavra***')
        letras_acertadas = ''
        numero_tentativas = 0
        
    