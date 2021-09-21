cafe_name = ""
cafe_visitors = "0"

while True:
    pet = input()

    if pet == "MEOW":
        print(cafe_name)
        break

    cafe_temp = pet.split(" ")

    if len(cafe_temp) > 1 and cafe_temp[1] > cafe_visitors:
        cafe_name = cafe_temp[0]
        cafe_visitors = cafe_temp[1]

