
# Task 18 — Contact Book with Search (nested dict)
# Ek dictionary of dicts banao:

# contacts = {
#     "Asha":  {"phone": "98765", "city": "Mumbai"},
#     "Rahul": {"phone": "91234", "city": "Delhi"},
# }
# User se ek naam maango. .get() se safely dhoondho — mile toh phone + city print karo, na mile toh "Contact not found".

# Concepts: nested dict, .get(), input(), if/else
# Hint: contacts.get(name) pehle — agar None mila toh not found, warna andar ke fields access karo.


print("==========Contact Book with Search (nested dict)===========")

contacts = {
                "Asha":  {"phone": "98765", "city": "Mumbai"},
                "Rahul": {"phone": "91234", "city": "Delhi"},
            }

print(contacts)

user = input("Enter the key Asha/Rahul: ")

print(contacts.get("user"))

print(contacts.get("user", "contacts not found"))

# if user == contacts:
#     print(f"{user.items()}")
# else:
#     print("Contact Not Found")

# method 1
# print(contacts.get("Asha"))

# print(contacts.get("Rahul"))

# print(contacts.get("Arti"),"contact not found")

