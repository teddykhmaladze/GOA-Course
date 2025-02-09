# day 22

# დაასრულეთ საკლასო დავალება: 
# 1) შექმენით for loop რომელიც სამჯერ შეეკითხება მომხმარებელს პაროლს, თუ მომხმარებელმა პაროლი სწორად შეიყვანა დაიბეჭდება "correct" თუ სამ ცდას გადააჭარგბა და პაროლი ვერ გამოიცნო კოდი გამოირთვება და დაიბეჭდება "out of trys"


correct_password = "1234" 

for _ in range(3):
    user_input = input("შეიყვანეთ პაროლი: ")
    if user_input == correct_password:
        print("correct")
        break
else:
    print("out of trys")


