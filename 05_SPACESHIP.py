import time
import subprocess

s = "start"
for i in s:
    print(i,end="",flush=True)
    
    if i == " ":
        time.sleep(0.08)
    else:
        time.sleep(0.09)
        
subprocess.run("cls",shell = True)
oname = str(input("Enter the officer name : "))
sname = str(input("Enter the spaceship name :"))
mpass = int(input("Maximum Passenger Capacity : "))
CPass = 0
Fuel = 60
Oxygen = 60
Food = 120 
Budget = 200000
subprocess.run("cls",shell = True)

for i in "="*24:
    print(i,end = "",flush=True)
print("\n"*2)
print("SPACE STATION CHECKPOINT")
print("\n"*2)
for i in "="*24:
    print(i,end = "",flush=True)
print("\n"*2)
aa = "1. Register Passengers  \n \n2. Manage Resources \n \n3. Mission Report \n \n4. Launch Mission \n \n5. Exit\n \n"
for i in aa:
    print(i,end="",flush=True)
    
    if i == " ":
        time.sleep(0.08)
    else:
        time.sleep(0.09)

for i in "="*24:
    print(i,end = "",flush=True)
print("\n"*2)



subprocess.run("cls",shell = True)

def register():
        while True:  
            a = int(input("How many passengers want to board?"))
            
            if a > mpass:
                print("Passenger count cannot exceed the maximum capacity.")
                continue
            elif a < 0:
                print("Passenger count cannot become negative.")
                continue
            else:
                break
        print(f"Current Passengers {CPass}")
        print(f"Capacity:{mpass}") 
         
        npass = CPass+ a
        print(f"New Passenger Count:{npass}")
        return 

def Manage_Resources():
    print("resource you want to update:\n 1. Fuel \n 2. Oxygen \n 3.food \n ")
    res = int(input("enter your choice here:"))
    def fuel(Fuel):
                 CurrentFuel = Fuel
                 print(f"Current Fuel ={CurrentFuel} %")
                 signn = input("enter sign + for add and - to subtract:")
                 if signn=="+":
                     if CurrentFuel==100:
                         print("not possible")
                     else:
                        print(f"New Fuel =  {CurrentFuel+20} %")
                        Fuel = CurrentFuel
                 elif signn == "-":
                     print(f"New Fuel =  {CurrentFuel-20} %")
                     Fuel = CurrentFuel
                     return Fuel
    def Foodd(Food):
                    CurrentFood = Food       
                    print(f"Current Food = {CurrentFood}Packs")
                    
                    while True:
                        usd = int(input("used number of packet:"))
                        if usd>CurrentFood :
                                print("we don't have enough food!")
                                break
                        else:
                            CurrentFood -= usd
                            print(f"Remaining Food = {CurrentFood} Packs") 
                            Food = CurrentFood
                        return Food
    match res:
        case 1:
            fuel(Fuel)
        case 2:
            print(Oxygen)
        case 3:
            Foodd(Food)
            
    return
def MissionReport():
    print(f"{'Officer Name':>14}:{oname}")
    print(f"{'Spaceship':>14}: {sname}")

    print(f"{'Mission Code'} {oname.upper()[0:2]}-204")
    print(f"{'Passengers':>14}:{CPass}/{mpass}")
    print(f"{'Fuel':>14}:{Fuel}%")
    print(f"{'Oxygen':>14}:{Oxygen}")
    print(f"{'Food':>14}:{Food}")
    print(f"{'Budget':>14}:{Budget}")
    return

def LaunchMission():
    print("Before launching, verifying conditions:")
    
    if Fuel<70 :
            print("Returning to Main Menu due to low Fuel...")
            return
    if Oxygen<70 :
            print("Returning to Main Menu due to low Oxygen...")
            return
    if Food <80:
            print("Returning to Main Menu due to less Food...")
            return
    print("Launching....")
    for i  in (0,6):
        print(i,"\n")
    print("MISSION SUCCESSFUL")
        
def exit():
    yy = str(input("enter y for yes and n for no- to exit:"))
    print(yy)
    if yy== "y":
        print("Thank you")
    elif yy== "n":
        return
        
       
while True: 
    a = int(input("Choose Option: ")) 
    match (a):
        case 1:
            register()
        case 2:
            Manage_Resources()
        case 3:
            MissionReport()
        case 4:
            LaunchMission()
        case 5:
            exit()
            break
        case _:
            print("invalid choice")
            
    

            