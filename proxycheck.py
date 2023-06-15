import requests
import colorama
from colorama import Fore, Back, Style
import os

colorama.init()
logo = r"""
  _______ _    _ ______ ____  _______     __
 |__   __| |  | |  ____/ __ \|  __ \ \   / /
    | |  | |__| | |__ | |  | | |__) \ \_/ / 
    | |  |  __  |  __|| |  | |  _  / \   /  
    | |  | |  | | |___| |__| | | \ \  | |   
    |_|  |_|  |_|______\____/|_|  \_\ |_|   
                                            
                                                                                                                                                      
"""
url = "https://www.youtube.com/"
work_file = "work.txt"
not_work_file = "not_work.txt"
proxy_file = "proxy.txt"
os.system("cls||clear")
print(Fore.BLUE + logo + Fore.RESET)


def check_proxies(proxy_file, url, success_file, failure_file):
    work_proxies = []
    not_work_proxies = []

    if not os.path.exists(proxy_file):
        print(f"{proxy_file} bulunamadı.")
        return

    with open(proxy_file, "r") as f:
        proxies = f.read().splitlines()

    for proxy in proxies:
        proxy_dict = {
            "http": proxy,
            "https": proxy,
            "ftp": proxy,
            "socks4": proxy,
            "socks5": proxy
        }
        try:
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                print(f"{proxy} {Fore.GREEN}[+]{Style.RESET_ALL}")
                work_proxies.append(proxy)
            else:
                print(f"{proxy} {Fore.RED}[-]{Style.RESET_ALL}")
                not_work_proxies.append(proxy)
        except requests.exceptions.RequestException:
            print(f"{proxy} {Fore.RED}[-]{Style.RESET_ALL}")
            not_work_proxies.append(proxy)

    with open(success_file, "w") as f:
        for proxy in work_proxies:
            f.write(proxy + "\n")

    with open(failure_file, "w") as f:
        for proxy in not_work_proxies:
            f.write(proxy + "\n")

check_proxies(proxy_file, url, work_file, not_work_file)
os.system("cls||clear")
print(Fore.GREEN + logo + Fore.RESET)
