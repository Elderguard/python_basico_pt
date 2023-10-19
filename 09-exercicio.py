peso = float(input("Informe seu peso em Quilogramas (Kg): "))
altura = float(input("Informe sua altura em metros (m): "))

iMC = peso/(altura**2)

print("IMC: ", iMC)
print("IMC2: %.2f " % iMC) #formatado com 2 casas decimais %.2f
print(f"IMC3: {iMC}")
