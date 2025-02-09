# 3) for loop ის გამოყენებით შექმენით კკოდი, მიუთითეთ ორი რიცხვი a და b და (a>b) და დაბეჭდეთ მათ შორის ყველა რიცხვი


a = int(input("შეიყვანე a: "))
b = int(input("შეიყვანე b: "))

if a > b:
    for i in range(b + 1, a):
        print(i)
else:
    print("a უნდა იყოს b-ზე დიდი!")
