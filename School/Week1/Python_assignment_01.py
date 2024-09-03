#First assignment for the AD_SD

#Objective 1, Welcome!
print("*** Responsible alcohol use calculator ***\n")

#Objective 2, Who's this?
name = input("What's your name? ")
if name == "":
    name = "Anon"
print("Hi", name,"!")

#Objective 3, Gender?
gender = input("Whats your gender? [Male/Female] ").lower()
if gender == "male":
    print("Men are awesome!")
    drinking_norm = 21
elif gender == "female":
    drinking_norm = 14
    print("Women are awesome!")
else:
    gender = "None"
    print("You are special")

#Objective 4, Drinks?
drinks = int(input("How many alcoholic beverage do you drink on average per week? "))
try:
    print("That's", drinks*52, "per year!")
except ValueError:
    print("Invalid number error\nExiting code...")
    exit()


#Objective 5, A word of advice
# if int(drinks) <= 0:
#     print("Healthy choice,", name)
# elif int(drinks) <= 7:
#     print("You'll probably be okay,", name)
# else:
#     print("Drinking less would be a healthier choice,", name)

#Objective 6, Gender-specific advice
if drinks <= 0:
    print("Healthy choice,", name)
elif drinks <= 7:
    print("You'll probably be okay,", name)
elif drinks <= drinking_norm:
    print("Drinking less would be a healthier choice,", name)
elif drinks <= drinking_norm*2 :
    print("You're an excessive drinker,",name,". That's not healthy..")
else:
    print("You're a really heavy drinker,",name,". That's very unhealthy. Change your ways!")

#Objective 7, Error handling
#Ob 1, 
#Ob 2, Made the user 'Anon' if they do not fill in a name.
#Ob 3, Made a 3rd gender called 'none' with the print 'You are special'.
#Ob 4, Made a try and except for the first 'int()' function 
#      so if that one fails the code shuts down, Instead of throwing 
#      more errors.
#Ob 5, Is incorporated in Ob 6.
#Ob 6, If gender is not male or female it doesn't give an advise.
#      Further handling is that the input gender is set to lowercase 
#      for better recognition.

