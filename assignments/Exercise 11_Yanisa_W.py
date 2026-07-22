inputFloor = int(input("Enter Floor: "))

for x in range(inputFloor):
    print(" " * (inputFloor-(x+1))+"*"*((x+1)+x))
