#!/bin/usr/python

from time import sleep
import os
import sys
from Modules.core import *

menu = '''
\033[1;36m What's New On Version2.5*

\033[1;32m∆\033[1;33m Change Name From D.L.B To W.o.F
\033[1;32m∆\033[1;33m Added Btc AutoClaim
\033[1;32m∆\033[1;33m Added ZCash Auto Claim
\033[1;32m∆\033[1;33m Bch/Doge All In One Script
\033[1;32m∆\033[1;33m Ltc/Zcash All In One Script
\033[1;32m∆\033[1;33m Still No Captcha Bypass...

\033[1;34m[\033[1;32m1\033[1;34m]\033[1;36m BTC Click Bot V2.5 ✔️
\033[1;34m[\033[1;32m2\033[1;34m]\033[1;36m BCH/DOGE Click Bot V2.5 ✔️
\033[1;34m[\033[1;32m3\033[1;34m]\033[1;36m LTC/ZCASH Click Bot V2.5 ✔️


\033[1;34m[\033[1;32m0\033[1;34m]\033[1;36m Exit ❌
'''

def main():
    banner()
    sleep(1)
    print ('\033[1;96mChoose Your Auto Claim Bot Senpai 😍😍😘')
    print (menu)
    pil = input('\033[1;95mWoF\033[1;0m >>\033[1;92m ')
    if pil == '1' or pil == '01':
       BTC()
    elif pil == '2' or pil == '02':
       BCD()
    elif pil == '3' or pil == '03':
       LTZ()
    elif pil == '0' or pil == '00':
       sys.exit()

    else:
       print ('\033[1;91mERROR \033[1;32m: \033[1;33mWrong Input Senpai 😉!')
       sleep(2)
       restart()

if __name__ == "__main__":
       main()


