user = input("Are you leaving for work : ")

def shutdown(user):
    if user == "yes" or user =="Yes" or user =="YES":
        print("I am shutting down the house lights and electronics")
    else:
        print("Notify me while leaving")

shutdown(user)