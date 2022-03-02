#income project
#Julio Briceno

income = float(input("Enter the gross income: "))
dependants = int(input("Enter the number of dependants: "))

income_tax = (income - 10000 - dependants*(3000)) * 0.20

print("The income tax is:$ ", income_tax)

