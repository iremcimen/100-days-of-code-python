def greet():
    print("a")
    print("b")
    print("c")

greet()


def greet_with_name(name): #name= parametre
    print(f"Hello {name}!")
    print(f"How do you do {name}?")

greet_with_name("İrem") #İrem= argument


def life_in_weeks(current_age):
    years_left = 90 - current_age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)