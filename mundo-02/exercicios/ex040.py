# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida.
# Média abaixo de 5.0 = Reprovado. Média entre 5.0 e 6.9 = Recuperação. Média 7.0 ou superior = Aprovado.

while True:
    try:
        nota1 = float(input("Digite sua primeira nota. (Ex:7.3): "))
        nota2 = float(input("Digite sua segunda nota. (Ex:7.3): "))
        if nota1 > 10 or nota2 > 10:
            print("Você digitou uma das notas, ou ambas, maiores do que 10. As notas devem ser menores do que 10, utilizando um ponto para separá-la, conforme exemplo abaixo.")
        else:
            print(f"Sua primeira nota foi {nota1} e a segunda nota {nota2}.")
            media = (nota1 + nota2) / 2
            print(f"Sua média é {media:.1f}")
            if media < 5:
                print("Sua média é menor do que 5. Você está REPROVADO!")
            elif 5 <= media < 7:
                media_Rec = 7.0 - media
                menor_Nota = min(nota1, nota2)
                nota_Necessaria = menor_Nota + (media_Rec * 2) 
                print(f"RECUPERAÇÃO!!! Sua menor nota foi {menor_Nota}. Por isso, você precisa tirar {nota_Necessaria:.1f} na prova para atingir a média 7.0 e passar de ano.")
            else:
                print(f"Sua média foi {media}. Parabéns, você foi APROVADO!!!")
            break
    except:
        print("Erro! Digite uma nota válida.")