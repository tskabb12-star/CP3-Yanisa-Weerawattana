totalPrice = int(input("Enther total price: "))


def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print("grandTotal:",vatCalculate(totalPrice))


