def login(username, password):
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Invalid Username or Password.")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSlelct():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculate():
    userSelected = menuSlelct()

    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2

    if userSelected == 1:
        return vatCalculate(totalPrice)

    elif userSelected == 2:
        return totalPrice

login("admin", "1234")
print(priceCalculate())