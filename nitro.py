import os
import time

import colorama
from colorama import Fore

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

choice = input(f"{purple}choice: ")

#  nitro gen dont be a fag and skid it
if choice == '1':
    setTitle("Nitro Generator")
    print("made by sevenv1 , took this from upincoming discord tool lmao join the discord to know when it comes out | https://discord.gg/3j83VKCknY")
	
    webhooklink = str(input(f"\n(\x1b[31m$\x1b[95m\x1b[37m) Webhook URL: "))
    
    count = 0

    webhook = "WEBHOOK_URL""".replace("WEBHOOK_URL", webhooklink)

    while True:
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
        except:
            print(f"{purple}ERROR!")
            break
