text = input()
sub = 'old'

first = text.find(sub)
second = text.rfind(sub)

print(first if first > second else second)
