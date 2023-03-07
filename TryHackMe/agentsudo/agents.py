import requests 
import string

out_file = ""

s = requests.Session()
for char in string.ascii_uppercase:
    url = 'http://10.10.218.47/index.php'
    header = {
        "User-Agent": char
    }
    r = s.get(url, headers=header)
    out_file += char + '\n' + '======' + '\n' + r.text + '\n'

with open('agent_find.txt', 'w') as f:
    f.write(out_file)

print('Done')
