try:
    nome_do_paciente = input("Digite seu nome: ").strip()
    if not nome_do_paciente:
        raise ValueError("Erro: Nome não pode ser vazio.")

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    if peso <= 0:
        raise ValueError("Erro: Peso deve ser um valor positivo.")
    if altura <= 0:
        raise ValueError("Erro: Altura deve ser um valor positivo.")

    if altura > 2.5 or peso > 300:
        raise ValueError("Erro: Os valores de altura ou peso parecem irreais.")

    imc = peso / (altura * altura)
    print(f"Nome: {nome_do_paciente} \nIMC: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso Normal")
    elif 25.0 <= imc < 29.9:
        print("Sobrepeso")
    elif 30 <= imc <= 34.9:
        print("Obesidade Grau I")
    elif 35 <= imc <= 39.9:
        print("Obesidade Grau II")
    else:
        print("Obesidade Grau III")

except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")

with open("cadastro_imc_lista.txt" , "a")  as arquivo:
    arquivo.write(f"\nNome: {nome_do_paciente}\nPeso: {peso}\nAltura: {altura}\nIMC: {imc}\n")
    
    if imc < 18.5:
        arquivo.write("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        arquivo.write("Peso Normal")
    elif 25.0 <= imc < 29.9:
        arquivo.write("Sobrepeso")
    elif 30 <= imc <= 34.9:
        arquivo.write("Obesidade Grau I")
    elif 35 <= imc <= 39.9:
        arquivo.write("Obesidade Grau II")
    else:
        print("Obesidade Grau III")
    arquivo.write("\n----------------------------------------------------------------------\n")