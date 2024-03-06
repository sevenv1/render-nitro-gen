import os
import time
import random
import string
import requests
from colorama import Fore, init

init(autoreset=True)

def cls():
    os.system('cls')

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | made by sevenv1")
    elif system == 'posix':
        sys.stdout.write(f"{_str} | made by sevenv1")
    else:
        pass

purple = Fore.LIGHTMAGENTA_EX

clearConsole()

watermark = """
    ██████╗  ██████╗     ██╗██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ 
   ██╔════╝ ██╔════╝    ██╔╝██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
   ██║  ███╗██║  ███╗  ██╔╝ ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
   ██║   ██║██║   ██║ ██╔╝  ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██╗╚██████╔╝╚██████╔╝██╔╝   ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝ ╚═════╝  ╚═════╝ ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

print(purple + watermark)
print(f"{purple}[+] made by sevenv1")

choice = input(f"{purple} Press 'Enter' to start the nitro generator: ")

if choice == '':
    setTitle("Nitro Gen ")
    print("join the discord im gonna release a discord tool soon | https://discord.gg/3j83VKCknY")
    
    webhooklink = str(input(f"{purple} Webhook URL: "))
    
    count = 0
    max_count = 10 

    webhook = "WEBHOOK_URL".replace("WEBHOOK_URL", webhooklink)

    while count < max_count:
        try:
            code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
            post = {"content":"https://discord.com/billing/promotions/"+code}
            head = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                'content-type' : 'application/json'
            }
            count += 1
            print(f"{purple}Generated Nitro | [{count}]")
            s = requests.post(webhook, json=post, headers=head)
        except Exception as e:
            print(f"{purple}ERROR! {e}")
            break
