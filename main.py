birth_year = int(input("What year were you born? "))

if 1925 <= birth_year <= 1946:
    print("You are part of the Traditionalists generation. 🧓")
elif 1947 <= birth_year <= 1964:
    print("You are part of the Baby Boomers generation. 👶")
elif 1965 <= birth_year <= 1981:
    print("You are part of the Generation X. 🚶")
elif 1982 <= birth_year <= 1995:
    print("You are part of the Millennials generation. 🙋")
elif 1996 <= birth_year <= 2015:
    print("You are part of the Generation Z. 👼")
else:
    print("You are part of a generation not listed here.")