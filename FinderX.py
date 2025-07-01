#!/usr/bin/env python3
import os, re, time, random
import requests
from bs4 import BeautifulSoup

# Terminal Colors
RED = "\033[91m"; GREEN = "\033[92m"; YELLOW = "\033[93m"
BLUE = "\033[94m"; CYAN = "\033[96m"; RESET = "\033[0m"

# Show Banner
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

descriptions = [
    "🔥 Active Group - Join Fast!", "💬 Daily Discussions & Fun",
    "🔔 24/7 Online Members", "🌐 Public Group Open to All",
    "✅ Verified & Active Group"
]

# Logic to scrape direct links (10+ real)
def get_minimum_links(query, regex, prefix, min_count=10, max_pages=5):
    headers = {'User-Agent': 'Mozilla/5.0'}
    collected = set()
    for page in range(max_pages):
        offset = page * 30
        url = f"https://html.duckduckgo.com/html/?q={query}&s={offset}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            for a in soup.find_all("a", href=True):
                found = re.findall(regex, a["href"])
                for link in found:
                    link = requests.utils.unquote(link)
                    if link.startswith(prefix):
                        collected.add(link)
                        if len(collected) >= min_count:
                            return list(collected)
        except:
            continue
    return list(collected)

def find_whatsapp(topic):
    print(f"\n{CYAN}Searching WhatsApp groups for:{RESET} {topic}\n")
    pattern = r"https://chat\.whatsapp\.com/\w+"
    links = get_minimum_links(f"site:chat.whatsapp.com {topic}", pattern, "https://chat.whatsapp.com/")
    if links:
        for link in links:
            print(f"{YELLOW}╭─────────────[ ✅ WHATSAPP ✅ ]─────────────╮")
            print(f"{GREEN} Group Name : {topic.title()} Group")
            print(f" Link       : {link}")
            print(f" Description: {random.choice(descriptions)}")
            print(f"{YELLOW}╰───────────────────────────────────────────╯{RESET}\n")
            time.sleep(0.2)
    else:
        print(f"{RED}❌ No WhatsApp groups found.{RESET}")

def find_telegram(topic):
    print(f"\n{CYAN}Searching Telegram groups for:{RESET} {topic}\n")
    pattern = r"https://t\.me/[\w\d_]+"
    links = get_minimum_links(f"site:t.me {topic}", pattern, "https://t.me/")
    if links:
        for link in links:
            name = link.split("/")[-1]
            print(f"{YELLOW}╭──────────────[ ✅ TELEGRAM ✅ ]──────────────╮")
            print(f"{GREEN} Group Name : {name.title()}")
            print(f" Link       : {link}")
            print(f" Description: {random.choice(descriptions)}")
            print(f"{YELLOW}╰─────────────────────────────────────────────╯{RESET}\n")
            time.sleep(0.2)
    else:
        print(f"{RED}❌ No Telegram groups found.{RESET}")

# Main menu loop
def main():
    while True:
        show_banner()
        print(f"{GREEN}[1]{RESET} WhatsApp Group Finder")
        print(f"{GREEN}[2]{RESET} Telegram Group Finder")
        print(f"{GREEN}[0]{RESET} Exit")
        choice = input(f"\n{BLUE}>> {RESET}").strip()
        if choice == "1":
            find_whatsapp(input("🔍 Topic: ").strip())
        elif choice == "2":
            find_telegram(input("🔍 Topic: ").strip())
        elif choice == "0":
            print(f"{YELLOW}Exiting... Bye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Try again.{RESET}")
        input(f"\n{CYAN}🔁 Press Enter to return to menu...{RESET}")

main()
