import os
import sys

def find_admin_panel():
    try:
        os.system("python admin/admin.py")
    except FileNotFoundError:
        print("admin/admin.py dosyası bulunamadı.")

def run_sherlock():
    try:
        user = input("Kullanıcı adını girin:")
        os.system(f"python sherlock/sherlock/sherlock.py {user}")
    except FileNotFoundError:
        print("Sherlock Bakımda")
        

def run_zphisher():
    try:
        os.system("bash zpisher/zphisher.sh")
    except FileNotFoundError:
        print("zphisher bulunamadı")    

def run_infoga():
    try:
        domain = input("Hedef Domaini Girin: ")
        os.system(f"python ınf/infoga.py -d {domain}")
    except FileNotFoundError:
        print("infoga bulunamadı!")

def send_sms():
    try:
        os.system("python sms.py")
    except FileNotFoundError:
        print("sms.py dosyası bulunamadı.")

def generate_password():
    try:
        os.system("python şifre.py")
    except FileNotFoundError:
        print("şifre.py dosyası bulunamadı.")

def ddos_attack():
    try:
        os.system("python ddos/hammer.py")
    except FileNotFoundError:
        print("Ddos bakımda")

def run_sql_injection():
    os.system("python sqlmap/sqlmap.py")

def banner():
   print("\033[91m")
   print(" _____  ___   __  __     _    ")
   print("|_   _|/ _ \\ |  \\/  |   / \\   ")
   print("  | | | | | || |\\/| |  / _ \\  ")
   print("  | | | |_| || |  | | / ___ \\ ")
   print("  |_|  \\___/ |_|  |_|/_/   \\_\\ \033[0;31m[\033[0;32mCoded By K4HINz <3\033[0;31m]\033")
   print("\033[0;31m[\033[0;32mInstagram:@t4lha.js\033[0;31m]\033")
   print("\033[0;31mUYARI:\033[0;32mYapılan islemler sorumlulugumda degildir!!!")
   print()
   print()




while True:
    os.system("")
    banner()

    print("\033[0;31m[\033[0;32m1\033[0;31m]\033[0m Admin panel          \033[0;31m[\033[0;32m2\033[0;31m]\033[0m SMS Bomb")  
    print("\033[0;31m[\033[0;32m3\033[0;31m]\033[0m Random Pass          \033[0;31m[\033[0;32m4\033[0;31m]\033[0m Ddos*")
    print("\033[0;31m[\033[0;32m5\033[0;31m]\033[0m NULL                 \033[0;31m[\033[0;32m6\033[0;31m]\033[0m NULL")
    print("\033[0;31m[\033[0;32m7\033[0;31m]\033[0m Phishing             \033[0;31m[\033[0;32m8\033[0;31m]\033[0m Kullanıcı Bulma")
    print("\033[0;31m[Q]\033[0m Çıkış")

    choice = input("Seçim yapın: ")

    if choice == "1":
        find_admin_panel()
        sys.exit(0)  # İşlem yapıldıktan sonra programı sonlandır
    elif choice == "2":
        send_sms()
        sys.exit(0)
    elif choice == "3":
        generate_password()
        sys.exit(0)
    elif choice == "4":
        ddos_attack()
        sys.exit(0)
    elif choice == "5":
        run_sql_injection()
        sys.exit(0)
    elif choice == "6":
        run_infoga()
        sys.exit(0)
    elif choice == "7":
        run_zphisher()
        sys.exit(0)
    elif choice == "8":
        run_sherlock()
        sys.exit(0)
    elif choice.lower() == "q":
        sys.exit(0)
    else:
        print("\033[0;31mGeçersiz bir seçim yaptınız. Tekrar deneyin.\033[0m")
