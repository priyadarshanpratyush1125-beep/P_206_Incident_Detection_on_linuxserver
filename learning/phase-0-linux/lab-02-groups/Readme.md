# Lab 02 — Linux Groups
## Objective

Understand how Linux groups organize users and how groups are related to permissions.

## Commands Used

```bash
groups
id
getent group | head -20
getent group | grep "$(whoami)"
```

## Terminal Output

### `groups`

```c
avatar@Avatargzb:~/HCLTech_Project$ groups
avatar adm cdrom sudo dip plugdev users lxd
```

### `id`

```c
avatar@Avatargzb:~/HCLTech_Project$ id
uid=1000(avatar) gid=1000(avatar) groups=1000(avatar),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),101(lxd)
```

### System Groups

```c
avatar@Avatargzb:~/HCLTech_Project$ getent group | head -20
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,avatar
tty:x:5:
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:avatar
floppy:x:25:
tape:x:26:
```

### My Groups

```c
avatar@Avatargzb:~/HCLTech_Project$ getent group | grep "$(whoami)"
adm:x:4:syslog,avatar
cdrom:x:24:avatar
sudo:x:27:avatar
dip:x:30:avatar
plugdev:x:46:avatar
users:x:100:avatar
lxd:x:101:avatar
avatar:x:1000:
```

## What I Learned

Linux groups are used to organize users and control access to resources.

A user can belong to multiple groups, and group membership becomes important when working with Linux permissions.

## Project Connection

In an incident detection system, user and group information can help identify **which user or group was associated with a particular activity**.
