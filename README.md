<h1 align="center">Vampire-AutoSQL</h1>
<p align="center">
  <b>A Fully Automatic & Powerful SQL Injection Scanner</b><br>
  <i>by Muhammad Shourov (VAMPIRE), Founder - Vampire Squad</i>
</p>

---

## :zap: Overview

**Vampire-AutoSQL** is a powerful and fully automated SQL injection vulnerability scanner designed to identify weak parameters from a given URL and test them using the industry-standard `sqlmap` engine.

This tool is specifically crafted for:

- Cybersecurity professionals
- Bug bounty hunters
- Ethical hackers
- Red teamers

---

## :rocket: Key Features

- **Parameter Discovery:** Auto-discovers all injectable GET/POST parameters from any target using ParamSpider.
- **SQL Injection Scanner:** Automatically performs SQLi tests on each parameter using `sqlmap`.
- **Auto Save Reports:** Saves results and logs in organized folders.
- **Live Vulnerability Logging:** Displays vulnerable parameters in real-time.
- **Exportable HTML Report:** Beautiful, shareable reports of SQLi findings.
- **Password Protected Access:** Secured with terminal password login (hidden input).
- **Legal Disclaimer Display:** Shows a slow-typing legal warning before tool runs.
- **Full Automation:** Just give a URL — it does the rest.

---

## :package: Installation

```bash
git clone https://github.com/vampiresquad/Vampire-AutoSQL.git
cd Vampire-AutoSQL
chmod +x install.sh
./install.sh
