vertical = int(input())
horizontal = int(input())
board = [1, 8]

if horizontal in board and vertical in board:
    print(3)
elif 1 < horizontal < 8 and 1 < vertical < 8:
    print(8)
else:
    print(5)
