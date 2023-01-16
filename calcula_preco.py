# Valor_Custo = Valor do Produto + Frete
# Se Valor_Custo <= 100,00  | porcentagem = 90%
# Se 100 < Valor_Custo <= 200,00  | porcentagem = 60%
# Se Valor_Custo > 200,00  | porcentagem = 40%
# Valor_Hora = Numero de Imagens x R$40.00
# Valor_Venda = Valor_Custo + Valor_Porcentagem_l (Lucro)
# Orcamento = Valor_Custo + Valor_Porcentagem_l + Valor_Hora


valor_custo = float(input('Digite o Valor do Custo: '))
valor_porcentagem = float(input("Digite a Porcentagem: "))
horas = float(input("Digite as horas gastas ('1hr = 1 imagem'): "))
print(15 * '-')

valor_porcentagem_l = valor_porcentagem / 100.00
valor_lucro = (valor_porcentagem_l * valor_custo)
valor_venda = valor_lucro + valor_custo
valor_horas = horas * 40.00
valor_final = valor_venda + valor_horas
valor_lucro_final = valor_horas + valor_lucro

orcamento = valor_venda + valor_horas

print(f'Valor Venda: R$ {valor_venda:.2f}')
print(f'Valor Lucro (sobre a venda): R$ {valor_lucro:.2f}')
print(f'Valor Horas/Trabalho: R$ {valor_horas:.2f}')
print(f'Valor Final (Orçamento): R$ {orcamento:.2f}')





    
