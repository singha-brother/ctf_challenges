# Brainpan 1

- https://tryhackme.com/room/brainpan
- March 10, 2023
- hard

---

## Enumeration

### Nmap

```
PORT      STATE SERVICE          REASON
9999/tcp  open  abyss            syn-ack
10000/tcp open  snet-sensor-mgmt syn-ack
```

- `nc $IP 9999` -> need to enter password
- 10000 -> SimpleHTTPServer 0.6 (Python 2.7.3)


## User Access


## Root Access

