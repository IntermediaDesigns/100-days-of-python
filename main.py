first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
maiden_name = input("Enter your mother's maiden name: ")
city_name = input("Enter the city you were born in: ")
print()
# Slice the first 3 characters of the first and last names
star_wars_first_name = first_name[:3] + last_name[:3]

# Combine the first two letters of the maiden name with the last 3 letters of the city
star_wars_last_name = maiden_name[:2] + city_name[-3:]

# Generate Star Wars name
print(f"Your Star Wars name is {star_wars_first_name.title()} {star_wars_last_name.title()}")
