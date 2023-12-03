altura = float(input("Digite sua altura em metros: "))
print("A sua altura é: ", altura)

peso = float(input("Digite seu peso em Quilogramas (Kg): "))
print("O seu peso é: ", peso)

imc = peso/(altura**2)

print("Seu IMC é igual a: %.2f" % imc)

if imc < 22:
    print("Você está magro")
elif 22<=imc<=26:
    print("Você está normal")
elif 26<imc<=30:
    print("Você está acima do peso")
else:
    print("Você está obeso")