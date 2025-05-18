#!/usr/bin/env python3

import os
import sys
import subprocess
from datetime import datetime
from termcolor import cprint, colored

# Banner
def banner():
    os.system("clear")
    cprint("╔═╗╦  ╦╔╦╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╔═╗╔═╗", "red")
    cprint("╠═╝║  ║ ║ ║╣ ╠═╣╠╦╝  ║  ╠═╣╠═╝╠═╣", "yellow")
    cprint("╩  ╩═╝╩ ╩ ╚═╝╩ ╩╩╚═  ╚═╝╩ ╩╩  ╩ ╩", "green")
    cprint("     Vampire Squad - Auto SQL Scanner", "cyan")
    print(colored("     Coded by: Muhammad Shourov (VAMPIRE)\n", "magenta"))

# Dependency check
def check_deps():
    try:
        import requests, termcolor
    except:
        print("[*] Installing required Python modules...")
        os.system("pip install requests termcolor")

# Run ParamSpider
def run_paramspider(target):
    cprint(f"\n[+] Running ParamSpider on: {target}", "cyan")
    out_file = f"output/{target.replace('https://', '').replace('http://', '').replace('/', '_')}_params.txt"
    os.system(f"paramspider --domain {target} --quiet > {out_file}")
    return out_file

# Run SQLMAP
def run_sqlmap(param_file):
    cprint(f"\n[+] Running SQLMap on extracted parameters...", "cyan")
    with open(param_file, "r") as f:
        urls = f.readlines()

    for url in urls:
        url = url.strip()
        if "?" in url:
            cprint(f"\n[*] Testing: {url}", "yellow")
            cmd = f"python3 sqlmap/sqlmap.py -u \"{url}\" --batch --random-agent --level=5 --risk=3 --threads=5"
            os.system(cmd)

# Main Logic
def main():
    banner()
    check_deps()

    if len(sys.argv) != 2:
        print("Usage: python3 vampire-autosql.py <target-site>")
        sys.exit(1)

    target = sys.argv[1]
    if not target.startswith("http"):
        target = "https://" + target

    if not os.path.exists("output"):
        os.makedirs("output")

    params_file = run_paramspider(target)
    run_sqlmap(params_file)
    cprint("\n[✓] Scanning complete. Stay Vampire!", "green")

if __name__ == "__main__":
    main()
