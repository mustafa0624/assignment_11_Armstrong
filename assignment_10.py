age = input("Are you a cigarette addict older than 75 years old?: (YES or NO) ".lower()) == "yes"
chronic = input("Do you have a severe chronic disease?: (YES or NO)".lower()) == "yes"
immune = input("Is your immune system too weak?: (YES or NO)".lower()) == "yes"
risk = age or chronic or immune
if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")
