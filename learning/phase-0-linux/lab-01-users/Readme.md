# Lab 1 — Linux Users

## Objective

Understand how Linux identifies users using:

* Username
* UID
* GID
* Groups

## Commands Used

```bash
whoami
id
cat /etc/passwd | head -10
grep "^$(whoami):" /etc/passwd
```

## Terminal Output

### `whoami`

```c
avatar@Avatargzb:~/HCLTech_Project$ whoami
avatar
 
```

### `id`

```c
avatar@Avatargzb:~/HCLTech_Project$ id
uid=1000(avatar) gid=1000(avatar) groups=1000(avatar),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),101(lxd)
```

### `/etc/passwd`

```c
avatar@Avatargzb:~/HCLTech_Project$ cat /etc/passwd | head -10
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

### My User Entry

```c
avatar@Avatargzb:~/HCLTech_Project$ grep "^$(whoami):" /etc/passwd
avatar:x:1000:1000:avatar:/home/avatar:/bin/bash
```

## What I Learned

Linux uses a **username, UID, GID and groups** to identify and organize users.

## Project Connection

Later, the incident detector can use user information to understand **who performed an activity on the server**.
