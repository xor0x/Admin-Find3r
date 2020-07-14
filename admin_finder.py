import argparse
import requests
from fake_headers import Headers
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

print("""
  ___      _           _            ______ _           _  _____      
 / _ \    | |         (_)           |  ___(_)         | ||____ |     
/ /_\ \ __| |_ __ ___  _ _ __ ______| |_   _ _ __   __| |    / /_ __ 
|  _  |/ _` | '_ ` _ \| | '_ \______|  _| | | '_ \ / _` |    \ \ '__|
| | | | (_| | | | | | | | | | |     | |   | | | | | (_| |.___/ / |   
\_| |_/\__,_|_| |_| |_|_|_| |_|     \_|   |_|_| |_|\__,_|\____/|_|   
                                                                     
                            By Xor0x                      
""")
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help="Web site without http/https and www")
parser.add_argument('-w', '--workers', default=5, type=int, help="Number of workers to use")
args = parser.parse_args()
url = args.url
url = url.replace('https://', '')
url = url.replace('https://www.', '')
url = url.replace('http://', '')
url = url.replace('http://www.', '')

protocols = ["http://", "https://"]

header = Headers(
        # generate any browser & os headers
        headers=False  # don`t generate misc headers
    )


def _headers():
    tmp_headers = {
        "User-Agent":
            header.generate()['User-Agent']
    }
    return tmp_headers


def fetch(f, target=url):
    for protocol in protocols:
        response = requests.get(url=f"{protocol}{target}/{f}", headers=_headers())
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] Admin Page Found: --> {protocol}{target}/{f}")
            break
        print(f"{Fore.RED}[-] Admin Not Found: --> {target}/{f}")


def run():
    with open("admin.txt", "r")as file:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            for f in file:
                executor.submit(fetch, f)


if __name__ == '__main__':
    run()
