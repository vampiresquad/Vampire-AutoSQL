#!/usr/bin/env python3
import os
import sys
import time
import subprocess
from termcolor import cprint, colored
from urllib.parse import urlparse
import getpass

PASSWORD = "SH404"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

def banner():
    os.system("clear")
    cprint("\n╔═╗╦  ╦╔╦╗╔═╗╔═╗╦═╗  ╔═╗╔═╗╔═╗╔═╗", "red")
    cprint("╠═╝║  ║ ║ ║╣ ╠═╣╠╦╝  ║  ╠═╣╠═╝╠═╣", "yellow")
    cprint("╩  ╩═╝╩ ╩ ╚═╝╩ ╩╩╚═  ╚═╝╩ ╩╩  ╩ ╩\n", "green")
    cprint("     Vampire Squad - Auto SQL Scanner", "cyan")
    print(colored("     Coded by: Muhammad Shourov (VAMPIRE)", "magenta"))
    print(colored("     Status: Fully Automatic | Fully Secure | Fully Advanced\n", "light_green"))

def slow_type(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def disclaimer():
    slow_type("\n[!] Disclaimer: This tool is for educational purposes only. Use it legally.", 0.05)

def check_password():
    try:
        inp = getpass.getpass("\nEnter Tool Password: ")
        if inp != PASSWORD:
            print("\n[!] Incorrect password.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Exiting.")
        sys.exit(1)

def run_paramspider(target):
    print(colored("\n[*] Scanning for parameters using ParamSpider...", "cyan"))
    output_file = f"{output_dir}/params.txt"
    os.system(f"paramspider -d {target} --level high -o {output_file} > /dev/null 2>&1")
    print(colored(f"[+] Parameters saved to {output_file}", "green"))
    return output_file

def run_sqlmap(url_file):
    log_file = f"{output_dir}/sqlmap_log.txt"
    html_report = f"{output_dir}/report.html"
    with open(url_file, 'r') as f:
        urls = f.readlines()

    slow_type("\n[!] Starting SQL Injection scan...\n")
    for url in urls:
        url = url.strip()
        if not url:
            continue
        slow_type(f"\n[*] Testing: {url}", 0.01)
        cmd = f"sqlmap -u \"{url}\" --batch --random-agent --level=3 --risk=3 --output-dir={output_dir} --flush-session --html-reports"
        with open(log_file, "a") as lf:
            subprocess.run(cmd, shell=True, stdout=lf, stderr=lf)

    print(colored(f"\n[+] SQLi scan complete. Logs saved to: {log_file}", "green"))
    print(colored(f"[+] HTML report (if any vulnerabilities found): {html_report}\n", "cyan"))

if __name__ == '__main__':
    banner()
    disclaimer()
    check_password()

    if len(sys.argv) != 2:
        print("\nUsage: python3 vampire-autosql.py <website>")
        sys.exit(1)

    target = urlparse(sys.argv[1]).netloc
    if not target:
        print("\n[!] Invalid URL.")
        sys.exit(1)

    param_file = run_paramspider(target)
    run_sqlmap(param_file)

    print(colored("\n[✔] All tasks complete.", "light_green"))
