produto1 = ["Água", 4, 2.50]
produto2 = ["Suco", 3, 5.00]
produto3 = ["café", 2, 4.50]

total1 = produto1[1]*produto1[2]
print("Total " + produto1[0], "= R$ %.2f" % total1)

total2 = produto2[1]*produto2[2]
print("Total " + produto2[0], "= R$ %.2f" % total2)

total3 = produto3[1]*produto3[2]
print("Total " + produto3[0], "= R$ %.2f" % total3)

total= total1+total2+total3
print("Total Geral ", "= R$ %.2f" % total)