import random
from datetime import datetime

print("\nSalary and rent task")
print("--------------------\n")
v_rent = int(input("Please enter your monthly rent:"))
v_salary = int(input("Please enter your monthly salary:"))
if v_salary-v_rent > 1000:
  print("Both rent and savings are possible this month!")
elif v_salary-v_rent < 0:
  print("Salary is not enough this month.")
else:
    print("Only rent will be paid this month.")

print("\nShipping calculator")
print("-------------------\n")
v_price = random.randint(0,500)
print(f"The product price is: {v_price}")
v_quantity = int(input("Please enter number of same item:"))
v_fee = 100
if v_price*v_quantity > 200:
   v_cost = v_price*v_quantity
   if v_cost > 500:
      if v_cost*0.1 > v_fee:
        print(f"Total cost is {v_cost*0.9:.2f}. Discount was given, delivery is for free.")
      else:
         print(f"Total cost is {v_cost*0.9:.2f}. Discount was given, delivery fee was charged.")
      v_cost *= v_cost*0.9
   else:
      print(f"Total cost is {v_cost:.2f}. No discount was given, delivery is for free.")
else:
   v_cost = v_price*v_quantity + v_fee
   print(f"Total cost is {v_cost:.2f}. No discount was given, delivery fee was charged.")

print("\nGuard duty")
print("----------\n")
v_age = int(input("Please enter your year of birth: "))
v_age = int(datetime.now().year)-v_age
v_pass = bool(int(datetime.now().second)%2)
v_name = input("Please enter your royal name: ")
if v_age < 18:
   print("Young ages not allowed - back home, nighty night!")
else:
   if v_name in ["Camila", "Elisabeth", "McBeth", "Charles"]:
      print("You are blacklisted - to the gallows!!!")
   else:
         if v_pass == True or v_name in ["Anne", "Diana", "George", "Duncan", "Cholomondeley", "Stuart"]:
            print("Honorable guest, please come in!")
         else:
            print(f"Since your name, {v_name}, is not royal, and you could not provide us a Gold pass, unfortunately you will not be let in tonight. Apologize!")

print("\nCar insurance quote")
print("-------------------\n")
v_accident_cnt = random.randint(0, 10)
if v_age < 25:
   v_premium = 3000
else:
   v_premium = 2000
v_premium += 500*v_accident_cnt
if v_premium > 5000:
   print(f"This policy is in High risk status, at premium cost of {v_premium}. No. of accidents reported is {v_accident_cnt}.")
else:
   print(f"This policy is in Standard status, at premium cost of {v_premium}. No. of accidents reported is {v_accident_cnt}.")

print("\nLab safety checklist")
print("--------------------\n")
v_temperature = random.randint(0, 100)
v_voltage = random.randint(0, 280)
v_pressure = random.randint(0, 100)
print(f"Current lab conditions are temperature at {v_temperature}, voltage of {v_voltage} and pressure at {v_pressure}.")
if (v_temperature >= 20 and v_temperature <= 80) and v_pressure < 60:
   if v_voltage > 190 and v_voltage < 240:
      print("All conditions are ok, safe to proceed!!!")
   else:
      if v_voltage > 190:
         print("While temperature and pressure are fine, voltage is too low to proceed. Please fix.")
      else:
         print("Voltage is too high! Evacuate immediately!")
else:
   if v_pressure >= 60:
      print("Pressure became too high! Panic and run for your life!!!")
   else:
      if v_temperature > 80:
         print("Lab became hot and all contents will catch catastrophic fire!!! Run away!!!")
      else:
         print("Lab became too chill. Please carefully check temperature control.")

print("\nWiazrds exam analysis")
print("---------------------\n")
v_spell = random.randint(0, 100)
v_accuracy = random.randint(0, 100)
v_control = random.randint(0, 100)
v_mark = (v_spell+v_accuracy+v_control)/3
if v_spell < 40 or v_accuracy < 40 or v_control < 40 or v_mark < 60:
   print("Fail.")
else:
   if v_mark < 74:
      print("Apprentice. Nice.")
   else:
      if v_mark < 89:
         print("Mage. Good luck.")
      else:
         print("Archmage. I bow to thee!")
