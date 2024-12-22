import random
aryanpass = int(input("Please enter the length of the password to be generated: "))
newvar = "abcdefghijklmnopqrstuvwxyaABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?"
password = "".join(random.sample(newvar, aryanpass))
print(password)