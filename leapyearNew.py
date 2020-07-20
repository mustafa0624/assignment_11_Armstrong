def leapyear():
    a = int(input("Please enter a digit Number :"))
    if a % 4 == 0 and a % 400 == 0:
        print(f"{a} is a leap year")
    elif a % 100 == 0:
        print(f"{a} is not a leap year")
    else:
        print(f"{a} is not a leap year")    

leapyear()