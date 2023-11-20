# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela o seguinte:
# O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, são valores iguais.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
elif numero2 > numero1:
    print(f'{numero2} é maior que {numero1}')
else:
        print(f'{numero1} e {numero2} são números iguais')

