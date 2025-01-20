try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))
    res = n1/n2
    print("The result is ", res )

except ZeroDivisionError :
    print("Zero is not used to divide ")
except ValueError :
    print("Enter a valid number")
except NameError as ex :
    print("Exception:",ex)
except:
    print("Some error occured")
finally:
    print("I will happen no matter what")