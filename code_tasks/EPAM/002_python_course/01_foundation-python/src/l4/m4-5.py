# Visibility and Namespaces

Money = 2000

def AddMoney():
    # Uncomment to fix
    # global Money
    Money = Money + 1
    print (Money)

AddMoney()
print(Money)