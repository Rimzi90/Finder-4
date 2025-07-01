#!/usr/bin/env python3
import os, re, time, random
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# Colors
RED, GREEN, YELLOW, BLUE, CYAN, RESET = ("\033[91m","\033[92m","\033[93m","\033[94m","\033[96m","\033[0m")

def show_banner():
    os.system("clear")
    print(f"""{RED}
██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     ███████╗██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██║██║╚██╗██║██║  ██║██╔══╝  ╚═══╝
███████╗██║██║ ╚████║██║  ██╗    ███████║██║██║ ╚████║██████╔╝███████╗██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝
{CYAN}        LINK FINDER - WhatsApp & Telegram Group Finder by RIMZI{RESET}
""")

descs = ["🔥 Active Group", "💬 Chat & Discussion", "🔔 24/7 Members", "🌐 Open to All", "✅ Verified Group"]

def fetch_links(topic, site, regex, limit=15):
    q = f"site:{site} {topic}"
    seen = set()
    for url in search(q, num_results=limit*2, unique=True):
        match = re.search(regex, url)
        if match:
            link = match.group(0)
            if link not in seen:
                seen.add(link)
        if len(seen) >= limit:
            break
    return list(seen)

def find_whatsapp(topic):
    print(f"\n{CYAN}Searching WhatsApp for:{RESET} {topic}\n")
    ws = fetch_links(topic, "chat.whatsapp.com", r"https://chat\.whatsapp\.com/\S+")
    if not ws:
        print(f"{RED}❌ No WhatsApp links found!{RESET}")
    else:
        for link in ws[:10]:
            print(f"{YELLOW}╭──[ ✅ WHATSAPP ]──╮")
            print(f"{GREEN}Link: {link}")
            print(f"{YELLOW}Description: {random.choice(descs)}{RESET}\n")

def find_telegram(topic):
    print(f"\n{CYAN}Searching Telegram for:{RESET} {topic}\n")
    tg = fetch_links(topic, "t.me", r"https://t\.me/\S+")
    if not tg:
        print(f"{RED}❌ No Telegram links found!{RESET}")
    else:
        for link in tg[:10]:
            name = link.split("/")[-1].replace("-", " ").title()
            print(f"{YELLOW}╭──[ ✅ TELEGRAM ]──╮")
            print(f"{GREEN}Group: {name}")
            print(f"{YELLOW}Link: {link}{RESET}\n")

def main():
    while True:
        show_banner()
        print(f"{GREEN}[1]{RESET} WhatsApp  {GREEN}[2]{RESET} Telegram  {GREEN}[0]{RESET} Exit")
        ch = input(f"\n{BLUE}>> {RESET}").strip()
        if ch=="1": find_whatsapp(input("Topic: ").strip())
        elif ch=="2": find_telegram(input("Topic: ").strip())
        elif ch=="0": break
        else: print(f"{RED}Invalid{RESET}")
        input(f"\n{CYAN}Press Enter to return to menu...{RESET}")

if __name__=="__main__":
    main()
