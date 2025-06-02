# if-else program to check if a number is positive, negative, or zero.
try:
    a=float(input("Enter any rational number: "))

    if a==0:
        print("Entered Number is 0")
    elif a>0:
        print("Entered Number is positive")
    elif a < 0:
        print("Entered Number is negative")

except ValueError:
    print("Please enter a valid rational number")

