# Blog (THM)

- https://tryhackme.com/room/blog
- March 21, 2023
- medium

---

## Enumeration

### Nmap

```
PORT     STATE    SERVICE     REASON      VERSION
22/tcp   open     ssh         syn-ack     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open     http        syn-ack     Apache httpd 2.4.29 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
139/tcp  open     netbios-ssn syn-ack     Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open     netbios-ssn syn-ack     Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
1021/tcp filtered exp1        no-response
```

- need to add `IP -> blog.thm` in /etc/hosts

### Samba

```
[+] IP: 10.10.148.143:445	Name: blog.thm  Status: Guest session   
    Disk      Permissions	Comment
	----      -----------	-------
	print$    NO ACCESS	Printer Drivers
	BillySMB  READ, WRITE	Billy's local SMB Share
	IPC$      NO ACCESS	IPC Service (blog server (Samba, Ubuntu))
```

- RW access at BillySMB

```sh
$ smbclient //$IP/BillySMB
Password for [WORKGROUP\hope]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Mar 21 22:14:23 2023
  ..                                  D        0  Wed May 27 00:28:23 2020
  Alice-White-Rabbit.jpg              N    33378  Wed May 27 00:47:01 2020
  tswift.mp4                          N  1236733  Wed May 27 00:43:45 2020
  check-this.png                      N     3082  Wed May 27 00:43:43 2020
```
- get image and `check-this.png` is qr code and redirect to youtube `Billy Joel - We Didn't Start the Fire`


### HTTP

- home page -> error establishing database connection
- directory brute forcing with ffuf

```
wp-admin
wp-content
wp-includes
```
- subdomain brute forcing with ffuf 
- `wp-admin` -> database error (I think it is actual error for this room and can't go further)


## User Access

## Root Access
