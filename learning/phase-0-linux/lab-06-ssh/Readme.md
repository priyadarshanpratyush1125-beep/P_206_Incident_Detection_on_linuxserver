# Lab 06 — SSH
## Objective

Understand SSH login sessions and the information Linux records about them.

## Commands Used

From my client machine:

```bash id="m8q2wp"
ssh username@SERVER_IP
```

On the Linux server:

```bash id="v5n9lc"
who
w
last
```

To close the SSH session:

```bash id="z1r6ht"
exit
```

## Terminal Output

### SSH Connection

```c
Microsoft Windows [Version 10.0.26100.6584]
(c) Microsoft Corporation. All rights reserved.

C:\Users\priya>ssh avatar@192.168.56.102
avatar@192.168.56.102's password:
Welcome to Ubuntu 26.04.1 LTS (GNU/Linux 7.0.0-34-generic x86_64)

 * Documentation:  https://docs.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed Sep 30 04:51:22 AM UTC 2026

  System load:             0.77
  Usage of /:              15.0% of 30.85GB
  Memory usage:            13%
  Swap usage:              0%
  Processes:               144
  Users logged in:         0
  IPv4 address for enp0s3: 10.0.2.15
  IPv6 address for enp0s3: fd17:625c:f037:2:a00:27ff:fec0:5897

 * Canonical Workshop gives developers fast, composable, reproducible, and
   secure developer environments that are perfect for agentic workflows.

   https://ubuntu.com/workshop

Expanded Security Maintenance for Applications is not enabled.

21 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


Last login: Wed Sep 30 04:51:26 2026 from 192.168.56.1
avatar@Avatargzb:~$ who
w
last
 04:52:02 up  1:20,  5 users,  load average: 0.70, 0.56, 0.39
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
avatar   pts/5    192.168.56.1     04:51    1.00s  0.25s  0.08s w
avatar            192.168.56.1     03:42           0.00s  0.16s sshd-sessio
avatar   pts/0    192.168.56.1     03:32   12:34   2.77s  2.77s -bash
avatar   tty1     -                03:31    1:19m  0.11s  0.11s -bash
Command 'last' not found, but can be installed with:
sudo apt install wtmpdb
```
## What I Learned

SSH allows a user to securely log in to a remote Linux server.

Linux provides information about **who logged in, when they logged in, and their session**.

## Project Connection

This information can help an incident detection system identify **unexpected or suspicious login activity**.
