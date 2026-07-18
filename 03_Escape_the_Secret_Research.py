name = str(input("enter the your name Agent:"))
id = str(input("enter your ID here:  "))
level = int(input("enter your security level here:  "))
age = int(input("enter your age here: "))
energy = 100
    
    
if(age<18):
    print("ACCESS DENIED")
    mission = "Fail"
elif level < 3 :
    print("ACCESS DENIED") 
    mission = "Fail" 
else:
    password = str(input("Enter Secret Password:"))
    j = 0
    if len(password) == 8 :
        a = any(char.isupper() for char in password)
        b = any(char.islower() for char in password)
        c = any(char.isdigit() for char in password)
        if a==True and b==True and c==True:
            print("ACCESS GRANTED ! \n WELCOME BACK, AGENT.")
        else:
            print("ALARM ACTIVATED")
            
    else:
        print("MISSION FAILED")
        
   
   
    if(energy>0):
        g = int(input("enter : \n 1  Unlock Main Door \n 2 Disable Cameras \n 3 Download Secret Files \n 4 Exit \n "))   
        match(g):
            case 1:
                print("DOOR UNLOCKED")
                energy -= 30
            case 2:
                print("Disabled Camera")
                energy -= 20
            case 3:
                print(" Files Downloaded ")  
                energy -= 40  
            case 4:
                print("exit")
    else:
        print("MISSION FAILED")
            
    attempt = 3
    while(attempt>0):
        real = "ACCESS-2040"
        catchca = str(input(f"for verification of you being a human \n enter ACCESS-2040:"))    
        attempt -=1   
        if(catchca == real):
            print("Door Opening...")
            mission = "Pass"
            break

for i in range(0,30):
    print("=",sep="",end="")
print("\n \n MISSION REPORT\n ")  
for i in range(0,30):
    print("=",sep="",end="")
    
print(f"\n {'Agent':<13}: {name}")
print(f"\n {'Agent Id':<13}:{id}")
print(f"\n {'Security Level':<13}:{level}")
print(f"\n {'Energy Left':<13}: {energy}")
print(f"\n {'Mission Status ':<13}: {mission}")
print(f"\n {'Generated Key ':<13}:{name[0:4]}{id[-2:]}{level} \n")
for i in range(0,30):
    print("=",sep="",end="")    
        
            
            
                

        
