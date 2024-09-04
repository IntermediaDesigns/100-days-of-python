print("Let's check your grade on your test!")
print()

test_name = input("Enter the name of the test: ")
max_score = 100
score = int(input("Enter your score: "))
percentage = round((score / max_score) * 100, 2)

if percentage >= 90:
  grade = 'A+'
  emoji = '🎉'
elif percentage >= 80:
  grade = 'A'
  emoji = '👍'
elif percentage >= 70:
  grade = 'B'
  emoji = '😊'
elif percentage >= 60:
  grade = 'C'
  emoji = '😐'
elif percentage >= 50:
  grade = 'D'
  emoji = '😕'
else:
  grade = 'U'
  emoji = '😢'


print(f"\nFor the {test_name} test:")
print(f"You scored {score} out of {max_score}.")
print(f"That's a percentage of {percentage}%.")
print(f"Your grade is {grade}. {emoji}")