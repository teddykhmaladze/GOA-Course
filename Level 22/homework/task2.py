# 2) while loop ის გამოყენებით დაწერეთ კოდი რომელიც მომხმარებელს შეეკითხება რიცხვს და სანამ მომხმ
# არებელი არ გამოიცნობს იქამდე არ გაჩერდეს. (ვისაც ultimate ჩელენჯი გინდათ ისე ქენით 
# რომ ყოველი გამოცნობის მერე დაპრინტოს რიცხვი უფრო დიდია თუ პატარა გამოსაცნობთან შედარებით

import random

target = random.randint(1, 100)  # შემთხვევითი რიცხვი 1-დან 100-მდე
attempts = 0

while True:
    user_input = int(input("მოითხოვე რიცხვი: "))
    attempts += 1
    
    if user_input == target:
        print(f"გილოცავ! გამოიცანი {attempts} ცდაში.")
        break
    elif user_input < target:
        print("უფრო დიდი რიცხვი სცადე!")
    else:
        print("უფრო პატარა რიცხვი სცადე!")


