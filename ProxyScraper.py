#!usr/bin/env python3
import sys
import requests
import proxyscrape
import threading

banner = """
\33[38;5;214m██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
\33[38;5;214m██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
\33[38;5;208m██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
\33[38;5;208m██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
\33[38;5;202m██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
\33[38;5;202m╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                                     
"""
print(banner)


def downloadproxies():
    collector = proxyscrape.create_collector('my-collector', ['http', 'socks4', 'socks5'])
    proxies = collector.get_proxies()
    file = open("proxies.txt","w")
    file.write(str(proxies))
    file.close()
    print("                                 \33[38;5;214mSuccessfully saved proxies list!\n\033[0m")

if __name__ == "__main__":
    thread = threading.Thread(target=downloadproxies)
    thread.start()
