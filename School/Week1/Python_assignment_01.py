# First assignment for the AD_SD

# Objective 1, Welcome!
print("*** Responsible alcohol use calculator ***\n")


# Objective 2, Who's this?
name = input("What's your name? ")

# Error handling
if name == "":  # noqa: PLC1901
    name = "Anon"

print("Hi", name, "!\n")


# Objective 3, Gender?
gender = input("Whats your gender? [Male/Female] ").lower()

if gender == "male":
    print("Men are strong!\n")
    drinking_norm = 21

elif gender == "female":
    drinking_norm = 14
    print("Women are smart!\n")

# Error handling
else:
    gender = "None"
    drinking_norm = 17
    print("You are one of a kind\n")


# Objective 4, Drinks?
drinks = float(input("How many alcoholic beverage do you drink on average per week? "))

try:
    print("That's", drinks*52, "per year!\n")

# Error handling
except ValueError:
    print("Invalid number error\nExiting code...")
    exit()


# Objective 5, A word of advice
# if int(drinks) <= 0:
#     print("Healthy choice,", name)
# elif int(drinks) <= 7:
#     print("You'll probably be okay,", name)
# else:
#     print("Drinking less would be a healthier choice,", name)


# Objective 6, Gender-specific advice
if drinks <= 0:
    print("Healthy choice,", name)

elif drinks <= 7:
    print("You'll probably be okay,", name)


elif drinks <= drinking_norm: # type: ignore
    print("Drinking less would be a healthier choice,", name)

elif drinks <= drinking_norm*2: # type: ignore
    print("You're an excessive drinker,", name, ". That's not healthy..")

else:
    print("You're a really heavy drinker,", name, ". That's very unhealthy. Change your ways!")

# Objective 7, Error handling
# Ob 1,
# Ob 2, Made the user 'Anon' if they do not fill in a name.
# Ob 3, Made a 3rd gender called 'none' with the print 'You are special'.
#       Also made their drinking norm 17 cause thats the average.
# Ob 4, Made a try and except for the first 'float()' function
#       so if that one fails the code shuts down, Instead of throwing
#       more errors.
# Ob 5, Is incorporated in Ob 6.
# Ob 6, Further handling is that the input gender is set to lowercase
#       for better recognition.
