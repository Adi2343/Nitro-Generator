import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
print("Nitro Generator made by Adi ✞#9566")
while 1:
    nitro_len = 16
    nitro_count = int(input("Ile kodów wygenerować: "))
    for x in range(0, nitro_count):
        nitro = ""
        for x in range(0, nitro_len):
            nitro_char = random.choice(Chars)
            nitro = nitro + nitro_char
        print("https://discord.gift/" + nitro)
    break
