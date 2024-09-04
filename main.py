print(" 🌟 Current Leader 🌟 ")
print()
f = open("high.score", "r")
scores = f.read().split("\n")
f.close()
max_score = [None, 0]
for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > max_score[1]:
      max_score = [data[0], int(data[1])]
print("Analyzing high scores......")
print()
print(f"Current leader is {max_score[0]} with a score of {max_score[1]}")
print()
print(f"The max score currently is {max_score[1]}")
