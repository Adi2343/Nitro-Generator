import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
print("Nitro Generator made by Adi ✞#9566")
while 1:
    password_len = 16
    password_count = int(input("Ile kodów wygenerować: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password = password + password_char
        print("https://discord.gift/" + password)
    break