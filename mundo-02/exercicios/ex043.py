# Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule o seu IMC.

while True:
    try:
        peso = int(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = peso / (altura**2)
        print(f'Seu IMC é de {imc:.2f}')
        if imc < 18.5:
            print("Abaixo do peso.")
        elif 18.5 < imc < 25:
            print("Peso ideal. Parabéns!")
        elif 25 < imc <= 30:
            print("Sobrepeso! Faça uma dieta.")
        elif 30 < imc <= 40:
            print("Obeso.")
        elif imc > 40:
            print("\U0001F480")
        break
    except:
        print("Digite o peso e a altura corretamente seguindo\n os exemplos: 80 - 1.75")