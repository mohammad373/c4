# c4

#/wp-
import os
import sys
import time
import requests
from colorama import Fore

def __wordpress__():
    os.system("clear")
    try:
        time.sleep(2)
        print(Fore.YELLOW + "Hello . Welcome Back ;)")
        time.sleep(2)
        target = input(Fore.GREEN + "\n[!] ~ Enter Your Address Target ==>  ")
        time.sleep(2)
        if target == "" or None :
            try:
                time.sleep(2)
                print(Fore.RED + "\n[!] ~ Your Target Is Not Found ;(")
                time.sleep(2)
                sys.exit()
            except:
                pass
        else:
            pass
        print(Fore.YELLOW + "\nYour Target Is Testing ...")
        time.sleep(1)
        print(Fore.YELLOW + "\nPleass 5 Sec Latter ...")
        r = requests.get("http://" + target + "/wp-content/plugins/")
        if r.status_code == 404 or r.status_code == 500:


                print(Fore.RED + r + Fore.YELLOW + " > " + Fore.RED + "Not Found ;(")
                time.sleep(2)
                sys.exit()

        else:

                time.sleep(2)
                print(Fore.GREEN + r + Fore.YELLOW + " > " + Fore.GREEN + "Found ;)")
                time.sleep(2)
                sys.exit()

    except:
        pass
__wordpress__()
