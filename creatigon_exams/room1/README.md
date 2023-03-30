# Creatigon Basic Pentest Exam (1)

- March 30, 2022, 11:50 pm
- Singha

---

## Enumeration

### Nmap

```
PORT      STATE SERVICE       VERSION
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
2221/tcp  open  rockwell-csp1 syn-ack
5040/tcp  open  unknown       syn-ack
49664/tcp open  unknown       syn-ack
49665/tcp open  unknown       syn-ack
49666/tcp open  unknown       syn-ack
49667/tcp open  unknown       syn-ack
```
- WINDOWS version
```
OS details: Microsoft Windows 10 1709 - 1909
```
```
PORT      STATE SERVICE VERSION
2221/tcp  open  ftp     Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
```

## User Access


## System Access