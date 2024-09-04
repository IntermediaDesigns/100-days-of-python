print("List Generator")
print()
start = (int(input("List a starting number: ")))
end = (int(input("List an ending number: ")))
increment = (int(input("List an increment between values: ")))
print()

print("\nHere is your list: ")
for i in range(start, end, increment):
  print(i)

