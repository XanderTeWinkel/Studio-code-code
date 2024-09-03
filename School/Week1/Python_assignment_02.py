# Second assignment for the AD_SD.

print("*** Welcome to Santa's Workshop ***")

# A string that if is 'yes' keeps the while loop running.
keep_going = "yes"

# The while loop that keeps running with all the rest of the code as long that 'keep_going' is yes.
while keep_going == "yes":
    print("\nLets draw a tree!")
    
    # A while loop that keeps asking the user for a integer from the user. If no integer is given the code keeps repeating itself.
    while True:
        try:
            size = int(input("How tall would you like it to be? "))
            break
        except ValueError:
            print("Invalid number error")
    
    # The if else tree for deciding what shape has to be displayed. If an incorrect shape has been given the code starts again at 
    # 'Lets draw a tree!'.
    shape = input("What shape should it have? [right/left/normal] ").lower()

    # Code for displaying the right side tree.
    if shape == "right":
        for i in range(size):
            for j in range(i+1):
                print("*", end="")
            print()

    # Code for displaying the left side tree.
    elif shape == "left":
        for i in range(1, size + 1):
            print(" " * (size - i) + "*" * i)

    # Code for displaying the normal tree.
    elif shape == "normal":
        k = 0
        for i in range(1, size+1):
            for space in range(1, (size-i)+1):
                print(end="  ")
            while k != (2*i-1):
                print("* ", end="")
                k += 1
            k = 0
            print()

    # If an incorrect shape has been given the code starts at 'Lets draw a tree!' again.
    else:
        print("No such shape")
        continue
    
    # Code for asking the user if they want to make another tree. If not 'Yes' or 'No' the code keeps asking again.
    while True:
        keep_going = input("Would you like to see another tree? [yes/no] ").lower()
        if keep_going == "yes" or keep_going == "no":
            break
        else:
            print("Invalid choice!")
