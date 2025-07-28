from requests import *
asciiart = """
 █    ██   ██████ ▓█████  ██▀███      ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒   ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄     ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░     ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░    ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
   ░           ░     ░  ░   ░        ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                                     ░                       ░                               
                                       made by @pieprzydev 
"""
print(asciiart)
usernames = input('[?]: Usernames dictionary: ')
accesstoken = input('[?]: Token (used to send requests): ')
with open(f"{usernames}", "r", encoding="utf-8") as f:
    users = f.read().splitlines()
for n in users:
   user = post(url='https://discord.com/api/v9/users/@me/pomelo-attempt',json={"username": n}, headers={"content-type": "application/json", "authorization": accesstoken})
   if user.status_code == 200:
       if user.json().get("taken") == True:
        print(f"[-]: USERNAME TAKEN: {n}")
       else:
        print(f"[+]: USERNAME AVAILABLE: {n}")
        with open(".\\validusers.txt", "a", encoding="utf-8") as g:
           g.write(f"{n}\n")
   elif user.status_code == 401:
      print("[!]: ERROR: No access.")
      input()
   else:
       print("[!] ERROR: Unknown error")
input("[!]: All username checked, press ENTER to exit.")