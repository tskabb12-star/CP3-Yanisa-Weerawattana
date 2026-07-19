userName = input("Enter your UserName: ")
password = input("Enter your Password: ")

if userName == "user" and password == "123":
    print("""
    ====================================
             HARDWARE SHOP
    ====================================
    1. Hammer             250 THB
    2. Screwdriver         80 THB
    3. Electric Drill   1,990 THB
    4. Paint Brush         60 THB
    5. Wrench Set         450 THB
    6. Measuring Tape     120 THB
    ====================================
    """)
    userSelect = int(input("Enter your Selection: "))
    if userSelect == 1:
        item = "Hammer"
        price = 250
    elif userSelect == 2:
        item = "Screwdriver"
        price = 80
    elif userSelect == 3:
        item = "Electric Drill"
        price = 1990
    elif userSelect == 4:
        item = "Paint Brush"
        price = 60
    elif userSelect == 5:
        item = "Wrench Set"
        price = 450
    elif userSelect == 6:
        item = "Measuring Tape"
        price = 120
    else:
        print("Invalid selection")
        exit()

    quantity = int(input("Enter quantity: "))


    print("====================================")
    print("Item :   ", item)
    print("Price:   ", price, "THB")
    print("Quantity:", quantity)
    print("Total:   ", price * quantity, "THB")
    print("====================================")
    print("Thank you for shopping!")
    print("====================================")
else:
    print("Invalid Username or Password.")