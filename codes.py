"""
1. Usando index() função

Uma solução simples é iterar pela lista com índices usando compreensão de lista e verificar outra ocorrência de cada elemento encontrado usando o index() função. A complexidade de tempo dessa solução seria quadrática e o código não lida com elementos repetidos na saída.

if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    dup = [x for i, x in enumerate(nums) if i != nums.index(x)]
    print(dup)  # [1, 5, 1]
 

Download  Executar código
2. Usando o operador In

Alternativamente, você pode usar o fatiamento com o in operador para pesquisar na parte já visitada da lista. A complexidade de tempo da solução permanece quadrática e permite elementos repetidos na saída.

if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    dup = [x for i, x in enumerate(nums) if x in nums[:i]]
    print(dup)  # [1, 5, 1]
 

Download  Executar código
3. Usando o Conjunto (Eficiente)

Para melhorar o desempenho e fazer o trabalho em tempo linear, você pode usar o set estrutura de dados.

if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    visited = set()
    dup = [x for x in nums if x in visited or (visited.add(x) or False)]
 
    print(dup)  # [1, 5, 1]
 

Download  Executar código

 
Para obter cada duplicata apenas uma vez, você pode usar a compreensão do conjunto, conforme mostrado abaixo:

if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    visited = set()
    dup = {x for x in nums if x in visited or (visited.add(x) or False)}
 
    print(dup)  # {1, 5}
 

Download  Executar código
4. Usando count() função

Aqui está uma solução alternativa usando o count() função, que fornece uma maneira simples e limpa de identificar duplicatas em uma lista. Isso não é recomendado para listas grandes, pois a complexidade de tempo é quadrática.

if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    dup = {x for x in nums if nums.count(x) > 1}
    print(dup)  # {1, 5}
 

Download  Executar código
5. Usando iteration_utilities módulo

finalmente, o iteration_utilities módulo oferece a duplicates função, que produz elementos duplicados. Você pode usar isso como:

from iteration_utilities import duplicates
 
if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    dup = list(duplicates(nums))
    print(dup)        # [1, 5, 1]
 

 
Para obter cada duplicata apenas uma vez, combine-a com unique_everseen():

from iteration_utilities import unique_everseen
 
if __name__ == '__main__':
 
    nums = [1, 5, 2, 1, 4, 5, 1]
 
    dup = unique_everseen(duplicates(nums))
    print(dup)        # [1, 5]
 

Isso é tudo sobre encontrar os itens duplicados em uma lista em Python. 
"""

salario = float(input("Digite o salário para calculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salário: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}")

