
def challenge():
    while True:
        action = int(input("Type a number: "))
        if action % 2 == 0:
            print("Even")
        else:
            print("Odd")

challenge()
