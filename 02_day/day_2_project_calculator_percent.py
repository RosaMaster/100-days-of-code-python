# Calculator Porcentagem

print("Welcome to the tip calculator.")
custo = input("What was the total bill? $ ")
pessoas = input("How many people to split the bill?\n")
percent = input("What percentage tip would you like to give? 10, 12, or 15?\n")
if (percent = 10) {
    total = (custo + custo*0.1)/pessoas
    }
elif (percent = 12) {
    total = (custo + custo*0.12)/pessoas
    }
elif (percent = 15) {
    total = (custo + custo*0.15)/pessoas
    }
else {
    print("Digite um valor valido!")
    return(percent)
    }
print(total)