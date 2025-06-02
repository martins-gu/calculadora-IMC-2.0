nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)
print (f"nome: {nome} \nImc: ")

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <=24.9:
    print("Peso Nornmal")
elif imc >=25.0 and imc <29.9:
    print("Sobrepeso")
elif imc >=30 and imc <= 34.9:
    print("Obesidade Grau I")
elif imc >=35 and imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("obesidade Grau III")