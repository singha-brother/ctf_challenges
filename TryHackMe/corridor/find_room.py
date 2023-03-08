import hashlib
import requests 

url = "http://10.10.50.100/"
s = requests.Session()

for i in range(0, 20):
    id_num = hashlib.md5(str(i).encode())
    id = id_num.hexdigest()
    r = s.get(url + id)
    print(f'[{i}] {r.url} -> {r.status_code} - {len(r.text)}')