notas = {"Maria" : 5.5, "Luiz" : 10.0, "Anonio" : 8.5, "Ana" : 3.7}
print ("Alunos e notas:")
print(notas)
print(notas["Luiz"])
valor_guardado = notas["Maria"]
print(valor_guardado)

nota_ana = notas.get("Ana")
print(nota_ana)