# customers.py 
# Author: [Your Name]
# Module 11 lab : customer dictionary & look up

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "Alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--- Exercise 2 ---")
customer["phone"] = '555-5555' #Adding a new key-value pair to the dictionary
print(customer)
customer["tier"] = "platinum" #Updating the value of an existing key in the dictionary
print(customer)
del customer["Name"] #Removing a key-value pair from the dictionary
print(customer)

print(customer.get("ytd_spend", 0 )) #Using the get() method to retrieve a value from the dictionary, with a default value if the key is not found

print ("--- Exercise 3 ---")
print(customer.get("email", "Email not found")) #Using the get() method to retrieve a value from the dictionary, with a default value if the key is not found

# try: 
#     print(customer["email"]) #Using the square bracket notation to retrieve a value from the dictionary, which will raise a KeyError if the key is not found
# except KeyError as error: 
#     print("keyerror caught:" error) #Catching the KeyError and printing an error message
