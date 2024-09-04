loan = 1000
interest = 0.05
years = 10
for i in range(years):
  loan += (loan * interest)
print("Total amount owed after 10 years:", round(loan, 2))