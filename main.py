import phonenumbers
import sys
import time
import datetime
import colorama
from colorama import Fore, Back, Style
from colorama import Style
colorama.init(autoreset=True)
print(Back.BLACK+Fore.RED+"""\033[94m
 ██▓     ▄████▄  ▄▄▄█████▓ ███▄    █ 
▓██▒    ▒██▀ ▀█  ▓  ██▒ ▓▒ ██ ▀█   █ 
▒██░    ▒▓█    ▄ ▒ ▓██░ ▒░▓██  ▀█ ██▒
▒██░    ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▓██▒  ▐▌██▒
░██████▒▒ ▓███▀ ░  ▒██▒ ░ ▒██░   ▓██░
░ ▒░▓  ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░   ▒ ▒ 
░ ░ ▒  ░  ░  ▒       ░    ░ ░░   ░ ▒░
  ░ ░   ░          ░         ░   ░ ░ 
    ░  ░░ ░                        ░ 
        ░""")
d = datetime.datetime.now()
print(d)
c ="""
HELLO I AM STARK *
        *
  THIS TOOL IS EDUCATION PURPOSE



CREATE BY STARK FROM AR

*** THANKS*** """


for i in c:
 time.sleep(0.1)
 sys.stdout.write(i)
 sys.stdout.flush()
from phonenumbers import timezone,geocoder,carrier
print(" ")
print(" ")
print(Back.BLACK+Fore.RED+"""
   USING FOR TOOL +910123456789
""")

print(" ")
print(" ")
number = input("enter the number with_+ ::")

phone = phonenumbers.parse(number)

time=timezone.time_zones_for_number(phone)

car = carrier.name_for_number(phone,"en")

reg = geocoder.description_for_number(phone,"en")
print("""\033[94m
   PHONE NUMBER IS []
""")
print(phone)
print(time)
print(number)
print(car)
print(reg)

