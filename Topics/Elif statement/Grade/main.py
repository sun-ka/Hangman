score = int(input())
max_score = int(input())
score_percent = score * 100 // max_score
grade = 'A'

if score_percent < 60:
    print('F')
elif score_percent < 70:
    print('D')
elif score_percent < 80:
    print('C')
elif score_percent < 90:
    print('B')
else:
    print(grade)
