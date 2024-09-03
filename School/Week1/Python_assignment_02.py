# Second assignment for the AD_SD.

print("*** Welcome to Santa's Workshop ***")

# Function for the while loop
keep_going = "yes"

# The while loop that keeps running with all the rest of the code as long that 'keep_going' is yes.
while keep_going == "yes":
    print("\nLets draw a tree!")
    
    while True: # While loop for asking the height
        try: # Try for catching an invalid height
            height = int(input("How tall would you like it to be? "))
            break
        except ValueError:
            print("Invalid number error")
    
    # The if else tree for deciding what shape has to be displayed. If an incorrect shape has been given the code starts again at
    # 'Lets draw a tree!'.
    shape = input("What shape should it have? [right/left/normal] ").lower()
    
    if shape == "right": # Code for displaying the right side tree.
        for i in range(height):
            for _j in range(i + 1):
                print("* ", end="")
            print()
    elif shape == "left":     # Code for displaying the left side tree.
        for i in range(1, height + 1):
            print(" " * (height - i) + "*" * i)
    elif shape == "normal":     # Code for displaying the normal tree.
        k = 0
        for i in range(1, height + 1):
            for _space in range(1, (height - i) + 1):
                print(end="  ")
            while k != (2 * i - 1):
                print("* ", end="")
                k += 1
            k = 0
            print()
    else:
        # If an incorrect shape has been given the code starts at 'Lets draw a tree!' again.
        print("No such shape")
        continue
    
    while True:
        # Code for asking the user if they want to make another tree. If not 'Yes' or 'No' the code keeps asking again.
        keep_going = input("Would you like to see another tree? [yes/no] ").lower()
        if keep_going == "yes" or keep_going == "no":
            break
        else:
            print("Invalid choice!")
