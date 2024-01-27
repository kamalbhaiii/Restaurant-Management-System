import json

# Admin onboarding function
def adminOnboarding():
    password = input("Enter the password for Admin portal:\t")
    defaultPass = "engineerscafe"

    while (password != "0" and password != "quit" and password != "q"):
        if (password == defaultPass):
            print("Hello Admin!!")
            break;
        else:
            password = input("Incorrect Password, try again.\nEnter the password for Admin portal else enter 'q' or 'quit' to exit:\t")
    else:
        print("Thank You for visiting. Bis Bald!!")