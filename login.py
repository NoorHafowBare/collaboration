# create the best login system ever
def login(username, password):
    # This is a placeholder for the best login system ever
    if username == "admin" and password == "password123":
        return "Login successful!"
    else:
        return "Login failed. Please try again."
# Example usage
print(login("admin", "password123"))    
print(login("user", "wrongpassword"))
print(login("admin", "password123"))
print(login("user", "wrongpassword"))
print(login("admin", "password123"))
print(login("user", "wrongpassword"))


# NEWWWWWWWWWWWWWWWWWWWWWWWWW
# create register forms
def register(username, password):
    # This is a placeholder for the best register system ever
    if len(username) < 5 or len(password) < 8:
        return "Registration failed. Username must be at least 5 characters and password at least 8 characters."
    else:
        return "Registration successful!"
# Example usage
print(register("newuser", "newpassword"))
print(register("usr", "pwd"))
print(register("newuser", "newpassword"))
print(register("usr", "pwd"))   
print(register("newuser", "newpassword"))
print(register("usr", "pwd"))   
print(register("newuser", "newpassword"))
