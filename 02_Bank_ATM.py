
    
name = str(input("enter your name:"))
acc = int(input("enter your account number:"))
Mno = int(input("enter your mobile number:"))
currB = int(input("enter the current balance here:"))
accct = str(acc)
print(f"{name.title().strip():<13}")
print(f"{acc:>13}")
print(f"{Mno:>13}")
print(f"{currB:>20}")
print(f"Customer ID : {name.upper()[0:3]}{accct[-4:]}")
Deposit = int(input("enter the amount you want to deposit:"))
print(Deposit)
ww = int(input("enter the amount you want to withdraw:"))
print(ww)
check_balance = currB + Deposit - ww
print(f"balance present in your account: {check_balance}")
print("exit")

amm = float(input(f"now the submitting amount : "))
if(amm<=0):
    print("INVALID AMOUNT")
else:
    check_balance += amm
    
ammountt = float(input(f"now the withdrawing amount : "))
if(ammountt<=0):
    print("INVALID ")
elif(ammountt >check_balance):
    print("Insufficient amount in your amount for this withdrawal!")
else:
    print("withdrawing ....")
    check_balance = check_balance - ammountt
    
print(f"the updated amount: Rs. {check_balance:.2f}")


for i in range(0,34):
    print("=",sep="",end="")
print("\n \t Bank ATM ")
for i in range(0,34):
    print("=",sep="",end="")
print(f"\n {'Name :':>13} {name.title().strip()}")
print(f"{'Account No.':>13}{acc}")
print(f"{'Mobile No.':>13} {Mno}")

print(f"{'Customer ID :':>13} {name.upper()[0:3]}{accct[-4:]}")
print(f"{'FINAL BALANCE:':>13}Rs. {check_balance:.2f}")

print(f"{'status :':>13} ACTIVE")

from datetime import date
today = date.today()
print(f"DATE:{today} \n")

for i in range(0,34):
    print("=",sep="",end="")
print(f"\n thank you for using the bank ATM")

    
    