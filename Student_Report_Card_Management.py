# take input
Student_Name = str(input("\nenter name of the student :"))
Roll_No = int(input("enter rollno:"))
Class = int(input("enter class here:")) 
section = int(input("enter section here:"))
english = int(input("enter eng marks here:"))
maths = int(input("enter maths here:"))
sci = int(input("enter sci marks here:"))




# banner
for i in range(1,33): print("=",sep="",end="")
print("\n STUDENT REPORT CARD SYSTEM ")
for i in range(1,33): print("=",sep="",end="")

print(f"\n name of the student :{Student_Name.title().strip()}")
print(f"rollno:{Roll_No:>20}")
print(f"Class:{Class:>20}")
print(f"section:{section:>20}")
print(f"marks scored in english: {english:>35}")
print(f"marks scored in maths:{maths:>35}")
print(f"marks scored in sci:{sci:>35}")

if(english<0 or english>100):
    print("invalid marks of english")
    exit()
if(maths<0 or maths>100):
    print("invalid marks of maths")
    exit()
if(sci<0 or sci>100):
    print("invalid marks of science")
    exit()
    
total = english+ maths +sci
print(f"the total score is:{total}")
average = (total/3)
print(f"the total score is:{average:.2f} %")


a = average

match a:
    case val if val>90:
        print("A")
        print("outstanding")
    case val if 75<val<89:
        print("B")
        print("V.good")
    case val if 60<val<74:
        print("C")
        print("good")
    case val if 40<val<59:
        print("D")
        print("needs improvement")
    case val if 0<val<40:
        print("F")
        print("work hard")
    
        
        
b = average 
match b:
    case val if 33<val<100:
        print("Pass")
    case val if 0<val<33:
        print("fail,get ready for back paper")
rr = str(Roll_No)[-3:]
code = Student_Name.upper()[0:3] + rr
print(code)  
         
    
  


