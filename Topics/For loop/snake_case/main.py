word = input()
translate = word[0]
delimiter = "_"

for char in word[1:]:
    if char.isupper():
        translate += delimiter
    translate += char
        
print(translate.lower())
