def calulator():
    while True:
        try:
            width = float(input("width:"))
            if width <= 0:
                print("width must be bigger than 0")
                continue
            length = float(input("length: "))
            if length <= 0: 
                print("length must be bigger than 0")
                continue
            cost_per_m =float(input("cost per meter"))
            if cost_per_m <= 0:
                print("Cost per meter must be bigger than 0")
                continue

            perimeter = 2*(width+length)
            cost = perimeter*cost_per_m
            print(f"the cost to fence your {perimeter}m perimeter rectangular area is ${cost}")

            another = (input("would you like to calculate another? (Enter = yes, any charactor to quit)"))
            if another != '':
                print("thank you for using the calculator.")
                break

        except ValueError:
            print("invalid input, try again.")

calulator()
 