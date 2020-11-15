import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"


password_len = int(input("What length would you like your password to be : "))
password_count = int(input("How many passwords would you like : "))
for x in range(0,password_count):
    password = ""
    for x in range(0,password_len):
        password_char = random.choice(chars)
        password = password+password_char
    print("Here is your password : ", password)
