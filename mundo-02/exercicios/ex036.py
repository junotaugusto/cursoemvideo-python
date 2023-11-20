# Escreva um programa para aprovar um empréstimo bancário para a compra de um imóvel.
# O programa vai perguntar o valor do imóvel, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário do comprador, ou o empréstimo será negado.

while True:
    valorImovel = input("Digite o valor do imóvel em R$: ")
    salario = input("Digite seu salário mensal em R$: ")
    financiamento = input("Digite em quantos anos deseja pagar: ")
    if valorImovel.isnumeric() and salario.isnumeric() and financiamento.isnumeric():
        valorImovel = int(valorImovel)
        salario = int(salario)
        financiamento = int(financiamento)
        break
    else:
        print('Digite apenas números inteiros nas opções. Não utilize pontos ou vírgulas.')

anos = financiamento * 12
prestacao = valorImovel / anos
if prestacao > salario * 30 / 100:
    print("Empréstimo NEGADO.")
    print(f'As parcelas ficaram R${prestacao:.2f} excedendo o valor de {salario * 30 / 100:.2f}')
else:
    print("Empréstimo APROVADO.")
