from random import choice


def print_win_message():
    print("You guessed the word!")
    print("You survived!")


def game():
    words = ('python', 'java', 'kotlin', 'javascript')
    word = choice(words)
    hint = '-' * len(word)
    lives = 8
    tries = []

    while lives > 0:
        print(hint)
        if hint == word:
            print_win_message()
            break

        letter = input("Input a letter:")

        if len(letter) != 1:
            print("You should input a single letter \n")
            continue

        if not letter.islower():
            print("Please enter a lowercase English letter \n")
            continue

        if letter in tries:
            print("You've already guessed this letter")
        elif letter in word:
            tries.append(letter)
            new_hint = ""
            for j in range(len(word)):
                if letter == word[j]:
                    new_hint += letter
                else:
                    new_hint += hint[j]
            hint = new_hint
        else:
            tries.append(letter)
            print("That letter doesn't appear in the word")
            lives -= 1
        if lives < 1:
            print("You lost!")
        print()


print("H A N G M A N")

while True:
    user_command = input('Type "play" to play the game, "exit" to quit:')

    if user_command == "play":
        print()
        game()
        break
