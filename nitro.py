import subprocess

def install_packages():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Required packages installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install required packages.")

try:
    import requests
    import colorama
except ImportError:
    print("Required packages not found. Installing them...")
    install_packages()


import os
import time
import random
import string
import requests
from colorama import Fore, init

init(autoreset=True)

def cls():
    os.system('cls')

purple = Fore.LIGHTMAGENTA_EX

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
    setTitle("Nitro Gen | by sevenv1")
    print("made by sevenv1 , took this from upincoming discord tool lmao, join the discord to know when it comes out | https://discord.gg/3j83VKCknY")
    
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
