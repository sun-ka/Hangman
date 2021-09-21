number = int(input())

if number < 1:
    print("no army")
elif number < 10:
    print("few")
elif number < 50:
    print("pack")
elif number < 500:
    print("horde")
elif number < 1000:
    print("swarm")
else:
    print("legion")
