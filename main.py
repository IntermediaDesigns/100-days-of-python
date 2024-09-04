name = input("What is your name? ")
print()
birthdate = input("What is your birthdate? ")
print()
phone = input("What is your phone number? (no spaces or dashes) ").strip()
print()
email = input("What is your email address? ").strip()
print()
address = input("What is your address? ")
print()

contact = {
    "name": name,
    "birthdate": birthdate,
    "phone": phone,
    "email": email,
    "address": address
}

print(
    f"Hi {contact['name']}. Our dictionary says that you were born on {contact['birthdate']}, "
    f"we can call you at {contact['phone']}, email you with {contact['email']}, or write to you at {contact['address']}."
)
