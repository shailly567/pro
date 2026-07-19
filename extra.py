# MISSION 1 – WELCOME SCREEN
"""FASHION STORE"""
for i in range(1,42):
    print(f"=",end="")
    
print(f"\n \t FASHION STORE ")
for i in range(1,42):
    print(f"=",end="")
print(f"\n Quality Never Goes Out of Style")

print("Welcome!")

#MISSION 2 – CUSTOMER REGISTRATION
name = str(input("enter your name:"))
age = int(input("enter your age:"))
Mobile_Number = int(input("enter your age:"))
city = str(input("enter your city:"))
budget = float(input("enter your budget:"))


print(age)
print(Mobile_Number)
print(budget)

#MISSION 3 – SMART NAME FORMATTER
print(city)
print(f"length is {len(name)}")
# a[] = "name"
# print(a[0])

print(name.strip().title())
print(name.upper())
print(name.lower())
print(name.split().join().replace("_").lower())

# MISSION 4 – PRODUCT SELECTION
Product_Name = str(input("enetr name of the product:"))
Price = int(input("enetr its price"))
Quantity = int(input("Quantity"))

code = int(input("enter the code of the product you wanted"))

match code:
    case 1:
        print("T-shirts")
        
    case 2:
        print("trousers")
        
    case 3: 
        print("shoes")
    case 4 :
        print("jackets")
    case 5 :
        print("watch")
    case 6 :
        print("bag")
    case _:
        print("this product is out of stock .")
               
#🎯 MISSION 5 – DISCOUNT SYSTEM
            