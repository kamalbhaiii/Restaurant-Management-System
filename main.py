from customer import *
from admin import *

role = int(input("Welcome to Our Restaurant!!!\nLogin as:\n1. As Customer\n2. As Admin\nEnter your Choice:\t"));

if role == 1:
    customerOnboarding();
elif role == 2:
    adminOnboarding();
else:
    print("Invalid Input")