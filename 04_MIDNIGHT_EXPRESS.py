import time
import sys
import subprocess

# for i in ..:
#     print(i,end="",flush=True)
    
#     if i == " ":
#         time.sleep(0.02)
#     else:
#         time.sleep(0.05)

while True:
    name = str(input("Enter the Manager Name ").strip())
    if name:
        break
    print("you can't leave this empty.")
    
tname = str(input("Enter the Train Name "))
TNumber = int(input("Enter the Train Number "))
while True:

        numberC = int(input("Enter the Number of Coaches "))
        if numberC>0:
            break
        else:
            print("error: The value must be greater than zero.")
while True:
    Passenger = int(input("Enter the Passenger Capacity "))
    if Passenger>numberC:
        break
    else:
        print("Capacity cannot be less than coaches.")
        

        
Journey_ID = print(f"Journey ID :{tname.upper()[0:3]}{TNumber}")
subprocess.run("cls", shell=True )

def Journey():
    distance = 0
    j = 50
    fuel = 900
    speed = 200
    print("Journey starts")
    fuel -= 8
    distance += j
    e = int(input("enter the code for events:"))

    match(e):
        case 1 :
            print("Heavy Rain")
            distance += 50
            speed -=30
            print(f"speed is reduced to {speed} due to Heavy Rain ")
    
     

m = int(input("enter a code:"))
match(m):
    case 1:
        Journey()
    case 2:
        Passengers()
    case 3:
        Tickets()
    case 4:
        Fuel()
    case 5:
        Garage()
    case 6:
        Cargo()
    case 7:
        Emergency()
    case 8:
        Finance()
    case 9:
        Crew()
    case 10:
        status()
    case 11:
        Report()
    case 12:
        Exit()
    default:
        print(" ")
        
        
            
        