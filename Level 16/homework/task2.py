GOA_BEST = input("რეგისტრაცია")
num = input("გთხოვთ შეიყვანოთ პაროლი!    Password:")
while num != GOA_BEST:
    
    print("Error: პაროლები არასწორია, გთხოვთ შეიყვანოთ სწორად!")
    num = input("Password:")
    
    print("თქვენ ხართ რეგისტრილებული! 🎉")
    break