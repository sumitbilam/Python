import random
import string

#This generate the password
def gen_password():
  temp1 = ""
  for i in range(1,3):
    k = random.choice(string.ascii_lowercase)
    temp1 += k
  temp2 = ""
  for i in range(0,2):
    x = str(random.randint(1,9))
    temp2 += x
  password = temp1+temp2
  print(password)
  return password

# this function display the inventory 
def display_inventory():
  print("Our Inventory:"+"\n"+"Honda"+"\n"+"Toyota"+"\n"+"kia")

 # this function display the car details
def car_detail(car):
  if car.lower() == "honda":
    print("You have selected: ", car.upper()) 
    print("Make: ", car.title(),"\n"+"model: Civic 2001"+"\n"+"Price: $2000.00")
  elif car.lower() == "toyota":
    print("You have selected: ", car.upper(),"\n") 
    print("Make: ", car.title(),"\n"+"model: Corola 2005"+"\n"+"Price: $2500.00")
  elif car.lower() == "kia":
    print("You have selected: ", car.upper(),"\n") 
    print("Make: ", car.title(),"\n"+"model: Optima 2017"+"\n"+"Price: $25000.00")
  else:
    print("We dont have this car")

#---------------------------------------------------------------------#
print("Welcome to ABC Cardealership \n")
display_inventory()
usercar = input("Enter car company:")

found = True

while found:
  if usercar.lower()=="honda" or usercar.lower()=="toyota" or usercar.lower()=="kia":
    print("Yes we have this company car. Please wait while we generate your password")
    print("Your password is: ")
    get_pass = gen_password()

    user_pass = input ("enter this password to access info of the car:")
    code = True
    while code:
      if user_pass == get_pass:
        car_detail(usercar)
        code = False
      else:
        user_pass = input("Please enter right password provided above:")
        code = True
    found = False
  else:
    print("Sorry we do not sale this company cars Please enter from below menu")
    display_inventory()
    usercar = input("Enter car company:")
    found = True

