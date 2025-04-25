from datetime import datetime
v_age = ""
while not(v_age.isnumeric()):
    v_age = input("Enter your year of birth: ")
v_loyalty = input("Loyalty member (y/n)? ")
v_day = datetime.now().weekday
print(f"{v_day}")