# Anthem (THM)

- https://tryhackme.com/room/anthem
- March 18, 2023
- easy

---

## Enumeration

### Nmap

- add `-Pn` 

```
PORT     STATE SERVICE       REASON
80/tcp   open  http          syn-ack
3389/tcp open  ms-wbt-server syn-ack
```

### HTTP

- Flags

![](screenshots/2023-03-18-21-15-50.png)

![](screenshots/2023-03-18-21-17-14.png)

![](screenshots/2023-03-18-22-41-26.png)

- robots.txt

```
UmbracoIsTheBest!

# Use for all search robots
User-agent: *

# Define the directories not to crawl
Disallow: /bin/
Disallow: /config/
Disallow: /umbraco/
Disallow: /umbraco_client/
```
- CMS - Umbraco

- found login page

![](screenshots/2023-03-18-21-22-15.png)

- at one of the blog page, there is a poem

![](screenshots/2023-03-18-21-42-35.png)

- copy and search in google - 

![](screenshots/2023-03-18-21-43-26.png)

- Get username
- enter the login page with their email pattern (\*\*@\*\*\*\*\*\*.\*\*\*) and password from one of the potential we have already found

![](screenshots/2023-03-18-21-45-27.png)

- can access to admin dashboard

- in searchsploit found RCE and I used this script 

![](screenshots/2023-03-18-22-43-41.png)

![](screenshots/2023-03-18-22-05-00.png)


## User Access

- The RDP port is also open
- enter with above credential 
- username - only two capital letters

![](screenshots/2023-03-18-22-18-21.png)

- In `C:\` found backup directory
- in backup directory `restore.txt` file exists
- it has no read access, but can change

![](screenshots/2023-03-18-22-29-15.png)

- read the contents of restore.txt which may be a potential password


## Administrator Access

- enter cmd with administrator account with above password


![](screenshots/2023-03-18-22-32-24.png)

- flags are under `C:\Users\Administrator\Desktop\root.txt` and `C:\Users\usrname\Desktop\user.txt`