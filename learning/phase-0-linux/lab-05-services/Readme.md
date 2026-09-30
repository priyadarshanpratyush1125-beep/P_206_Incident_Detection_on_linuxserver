# Lab 05 — Linux Services
## Objective

Understand how Linux manages services using **systemd** and how a service is connected to its running process.

## Commands Used

```bash
systemctl status ssh
systemctl is-active ssh
systemctl list-units --type=service --state=running
ps -ef | grep ssh
```

> If your system uses `sshd` instead of `ssh`, use `sshd` in the commands.

## Terminal Output

### SSH Service Status

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-05-services$ systemctl status ssh
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/syste>
     Active: active (running) since Wed 202>
 Invocation: 1023fe5767fe46a6a5e08afabb7698>
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)
   Main PID: 939 (sshd)
      Tasks: 1 (limit: 6210)
     Memory: 9.1M (peak: 13.2M)
        CPU: 1.344s
```


### Running Services

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-05-services$ systemctl list-units --type=service --state=running
  UNIT                           LOAD   ACT>
  chrony.service                 loaded act>
  cron.service                   loaded act>
  dbus.service                   loaded act>
  fwupd.service                  loaded act>
  getty@tty1.service             loaded act>
  ModemManager.service           loaded act>
  multipathd.service             loaded act>
  networkd-dispatcher.service    loaded act>
  polkit.service                 loaded act>
  rsyslog.service                loaded act>
```

### SSH Process

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-05-services$ ps -ef | grep ssh
root         939       1  0 03:31 ?        00:00:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root        1593     939  0 03:32 ?        00:00:00 sshd-session: avatar [priv]
avatar      1647    1593  1 03:32 ?        00:00:47 sshd-session: avatar@pts/0
root        2137     939  0 03:41 ?        00:00:00 sshd-session: avatar [priv]
avatar      2194    2137  1 03:42 ?        00:00:52 sshd-session: avatar@notty
avatar      2833       1  0 03:59 ?        00:00:00 ssh-agent -s
avatar      4317    4075 42 04:46 pts/3    00:00:00 grep --color=auto ssh
```

## What I Learned

**systemd** manages services in Linux.

The service is responsible for starting/managing the actual process that performs the work.

## Project Connection

For incident detection, monitoring services and their processes can help identify **unexpected service states or suspicious processes** running on the server.
