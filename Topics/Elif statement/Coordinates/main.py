horizontal = float(input())
vertical = float(input())

if horizontal == 0 and vertical == 0:
    print("It's the origin!")
elif horizontal == 0 or vertical == 0:
    print("One of the coordinates is equal to zero!")
elif horizontal > 0:
    print("I" if vertical > 0 else "IV")
elif horizontal < 0:
    print("II" if vertical > 0 else "III")
