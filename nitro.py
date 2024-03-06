import ctypes
import os
import time
import random
import string
import requests
from colorama import Fore, init

init(autoreset=True)

def validateWebhook(hook):
    if not "api/webhooks" in hook:
        print(f"\n{Fore.RED}Invalid Webhook!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    try:
        responce = requests.get(hook)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        print(f"\n{Fore.RED}Invalid Webhook!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    try:
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    print(f"{Fore.GREEN}Valid webhook! ({j})")

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | made by sevenv1")
    elif system == 'posix':
        sys.stdout.write(f"{Fore.LIGHTMAGENTA_EX} | made by sevenv1")
    else:
        pass

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

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
print(f"{purple}[$] made by sevenv1 | my discord server (gonna release a discord tool soon) : https://discord.gg/3j83VKCknY")

choice = input(f"{purple} Press 'Enter' to start the nitro generator: ")

if choice == '':
    setTitle("Nitro Gen ")

    print("join the discord im gonna release a discord tool soon | https://discord.gg/3j83VKCknY")

    webhooklink = str(input(f"{purple} Webhook URL: "))
    validateWebhook(webhooklink)

    count = 0 
    max_count = 9999999

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
            print(f"{purple}Generated Nitro | [{count}] .gg/render")
            s = requests.post(webhook, json=post, headers=head)
        except Exception as e:
            print(f"{purple}ERROR!")
            break
