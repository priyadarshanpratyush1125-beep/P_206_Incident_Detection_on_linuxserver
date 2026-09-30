# Lab 04 — Linux Processes
## Objective

Understand how Linux represents running programs using:

* PID
* PPID
* USER
* COMMAND

## Commands Used

```bash id="q3j7ka"
ps
ps -ef
ps -ef | grep ssh
sleep 300
ps -ef | grep sleep
ps -p <PID> -f
kill <PID>
```

## Terminal Output

### `ps`

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-04-processes$ ps
    PID TTY          TIME CMD
   1648 pts/0    00:00:02 bash
```

### `ps -ef | grep ssh`

``c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-04-processes$ ps -ef | grep ssh
root         939       1  0 03:31 ?        00:00:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root        1593     939  0 03:32 ?        00:00:00 sshd-session: avatar [priv]
avatar      1647    1593  1 03:32 ?        00:00:45 sshd-session: avatar@pts/0
root        2137     939  0 03:41 ?        00:00:00 sshd-session: avatar [priv]
avatar      2194    2137  1 03:42 ?        00:00:41 sshd-session: avatar@notty
avatar      2833       1  0 03:59 ?        00:00:00 ssh-agent -s
avatar      3822    1648 60 04:38 pts/0    00:00:00 grep --color=auto ssh
```cc

### Test `sleep` Process

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-04-processes$ sleep 300
^C
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-04-processes$ ps -ef | grep sleep
avatar      3764    2195  0 04:36 ?        00:00:00 sleep 180
avatar      3849    1648 50 04:38 pts/0    00:00:00 grep --color=auto sleep
```
## What I Learned

A **process** is a running instance of a program.

The **PID** identifies a process, while the **PPID** identifies its parent process.

## Project Connection

An incident detector needs process information to identify **which programs are running and who started them**.
