# Lab 03 — Linux Permissions
## Objective

Understand Linux file permissions:

* `r` → Read
* `w` → Write
* `x` → Execute
* Owner
* Group
* Others

## Experiment

I created a file and changed its permissions using `chmod`.

## Commands Used

```bash
touch test.txt
ls -l test.txt

chmod 600 test.txt
ls -l test.txt

chmod 644 test.txt
ls -l test.txt

chmod 755 test.txt
ls -l test.txt

stat -c "%A %a %U %G %n" test.txt
```

## Terminal Output

### Initial Permission

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-03-permissions$ ls -l test.txt
-rw-rw-r-- 1 avatar avatar 39 Sep 30 04:30 test.txt
```

### Permission 600

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-03-permissions$ chmod 600 test.txt
ls -l test.txt
```

### Permission 644

```C
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-03-permissions$ chmod 644 test.txt
ls -l test.txt
-rw-r--r-- 1 avatar avatar 39 Sep 30 04:30 test.txt
```

### Permission 755

```C
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-03-permissions$ chmod 755 test.txt
ls -l test.txt
-rwxr-xr-x 1 avatar avatar 39 Sep 30 04:30 test.txt
```

### `stat` Output

```C
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-03-permissions$ stat -c "%A %a %U %G %n" test.txt
-rwxr-xr-x 755 avatar avatar test.txt
```

## What I Observed

| Permission | Meaning     |
| ---------- | ----------- |
| `600`      | `rw-------` |
| `644`      | `rw-r--r--` |
| `755`      | `rwxr-xr-x` |

Linux permissions are divided into:

**Owner | Group | Others**

## What I Learned

`chmod` changes the permissions of a file.

The same file can have different access levels depending on its permission settings.

## Project Connection

File permissions are important for incident detection because unexpected permission changes can indicate suspicious or unauthorized activity.
