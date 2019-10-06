#!/bin/usr/python

import os
import sys
from time import sleep

banner_WOF = '''
\033[1;35m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
\033[1;92m        <<<<<<\033[1;36mWelcome W.o.F Auto Claim Tools\033[1;32m>>>>>>
\033[1;35m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
\033[1;32m             ••••••••••[\033[1;33m∆\033[1;32m]\033[1;31mNOTE\033[1;32m[\033[1;33m∆\033[1;32m]••••••••••
\033[1;33m IF YOU GET A MESSAGE FROM BOT \033[1;32m: \033[1;31m[😭]FAILED
\033[1;32mJUST GO TO YOUR TELEGRAM ACCOUNT AND TAP THE SKIP BUTTON
\033[1;34m         DON'T FORGET TO SUBSCRIBE MY CHANNEL😉😉
\033[1;35m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
\033[1;33mCreated By \033[1;31m: \033[1;34m[\033[1;32mZetsU\033[1;34m]  \033[1;31mYouTube \033[1;33mChannel \033[1;31m: \033[1;34m[\033[1;32mZetsUHaxX\033[1;34m]
\033[1;33mVersion    \033[1;31m: \033[1;35m[\033[1;36mV2.0\033[1;35m]   \033[1;33mUpdated On      \033[1;31m: \033[1;35m[\033[1;36mMay 5,2019\033[1;35m]
\033[1;35m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

banner_BTC = '''
\033[1;36mGood Choice Senpai!😍😍😘

\033[1;33mEnter Your Number Senpai 😉

Don't Worry Senpai 😍 Just Only The Number Not Your
Information This Bot Is \033[1;32m100% Safe And Secure..


'''
banner_BCD = '''
\033[1;36mGood Choice Senpai!😍😍😘

\033[1;33mEnter Your Number Senpai 😉

Don't Worry Senpai 😍 Just Only The Number Not Your
Information This Bot Is \033[1;32m100% Safe And Secure..



'''

banner_LTZ = '''
\033[1;36mGood Choice Senpai!😍😍😘

\033[1;33mEnter Your Number Senpai 😉

Don't Worry Senpai 😍 Just Only The Number Not Your
Information This Bot Is \033[1;32m100% Safe And Secure..


'''

def restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()


def banner():
       print (banner_WOF)

def BTC():
       print (banner_BTC)
       sleep(1)
       print ('\033[1;95mExample : +63927**********\n')
       BTC = input('\033[1;36mEnter Your Number\033[1;0m :\033[1;32m ')
       os.system('cd Modules/.WOF && python one.py ' + BTC)

def BCD():
       print (banner_BCD)
       sleep(1)
       print ('\033[1;95mExample : +63927**********\n')
       BCD = input('\033[1;36mEnter Your Number\033[1;0m :\033[1;32m ')
       os.system('cd Modules/.WOF && python two.py ' + BCD)

def LTZ():
       print (banner_LTZ)
       sleep(1)
       print ('\033[1;95mExample : +63927**********\n')
       LTZ = input('\033[1;36mEnter Your Number\033[1;0m :\033[1;32m ')
       os.system('cd Modules/.WOF && python three.py ' + LTZ)


