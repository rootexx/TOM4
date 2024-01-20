import random
import string
import os

def banner():
    print("\033[0;31m")
    print(" _____  ___   __  __     _    ")
    print("|_   _|/ _ \\ |  \\/  |   / \\   ")
    print("  | | | | | || |\\/| |  / _ \\  ")
    print("  | | | |_| || |  | | / ___ \\ ")
    print("  |_|  \\___/ |_|  |_|/_/   \\_\\ \033[0;31m[\033[0;32mCoded By K4HINz <3\033[0;31m]\033")
    print("\033[0m")
    print("\033[0;31m[\033[0;32mInstagram:@t4lha.js\033[0;31m]\033")
    print("\033[0;31mUYARI:\033[0;32mYapılan islemler sorumlulugumda degildir!!!")

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

while True:
    os.system("")
    banner()
    try:
        length = int(input("Şifre uzunluğunu girin: "))
        password = generate_password(length)
        print("Oluşturulan Şifre:", password)
        break
    except ValueError:
        print("Geçersiz uzunluk. Lütfen bir tam sayı girin.")
