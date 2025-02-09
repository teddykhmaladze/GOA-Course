

score = int(input("შეიყვანე შენი ქულა (0-10): "))

if score >= 9:
    print("A")
elif score >= 7:
    print("B")
elif score >= 5:
    print("C")
else:
    print("ვერ გადახვედი")


ნიშანი = int(input("შეიყვანე შენი ნიშანი: "))
if ნიშანი >= 100:
    print("ყოჩაღ, შენ მიიღე 10 ქულა")
elif 80 >= ნიშანი:
    print("ყოჩაღ, შენ მიიღე 8 ქულა")
elif 70 >= ნიშანი:
    print("შენ მიიღე 6 ქულა")
elif 60 >= ნიშანი:
    print("შენ მიიღე 4 ქულა")
else:
    print("სამწუხაროდ შენ მიიღე 02 ქულა")
