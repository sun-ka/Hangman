string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0

for vowel in string:
    if vowel in vowels:
        counter += 1

print(counter)
