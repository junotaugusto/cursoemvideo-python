# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento. 

# À vista dinheiro / cheque - 10% desconto.
# À vista no cartão - 5% de desconto.
# Em até 2x no cartão - sem desconto.
# 3x ou mais no cartão - 20% de juros.
import time
import sys
while True:
    try:
        print("Digite o valor da sua compra.")
        compra = float(input("Quanto deu sua compra: "))
        print(f"Sua compra deu R${compra:.2f}")
        print("Digite uma das opções:\n[1]Dinheiro\n[2]Cheque\n[3]Cartão.")
        pagamento = int(input("Digite uma das opções:\n[1]Dinheiro - [2]Cheque - [3]Cartão."))
        if pagamento > 3:
            print('Digite novamente: ')
        else:
            digitar_mensagem('Obrigado. Estamos processando sua solicitação.\n')
            time.sleep(3)
            if pagamento == 1:
                digitar_mensagem("Você escolheu pagar em Dinheiro, à vista.\nPor isso, tem  desconto de 10%.\n")
                digitar_mensagem(f'Sua compra ficou em R${compra - (compra * (10 / 100)):.2f}\n')
            elif pagamento == 2:

                digitar_mensagem("Você escolheu pagar em cheque.\nAceitamos apenas cheques à vista com desconto de 10%.\n")

                digitar_mensagem(f'Sua compra deu R${compra - (compra * (10 / 100)):.2f}\n')    
            break
    except ValueError:
        digitar_mensagem('Digite as opções com números válidos para continuar.')

def digitar_mensagem(mensagem):
    for char in mensagem:
        sys.stdout.write(char)
        sys.stdout.flush()  # Força a saída imediata para exibir o caractere
        time.sleep(0.05)  # Ajuste o tempo de espera conforme desejado