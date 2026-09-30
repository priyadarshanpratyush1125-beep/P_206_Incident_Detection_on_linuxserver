# Lab 07 — Linux Logs
## Objective

Understand how Linux stores system events in the **systemd journal** and how to monitor new events in real time.

## Commands Used

```bash id="h8r3mp"
journalctl -n 30
journalctl -n 20 --no-pager
journalctl -f
```

## Terminal Output

### Recent Logs

```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-07-logs$ journalctl -n 30
Sep 30 04:40:14 Avatargzb systemd[1]: sysst>
Sep 30 04:40:14 Avatargzb systemd[1]: Finis>
Sep 30 04:43:15 Avatargzb systemd[1]: Start>
Sep 30 04:43:20 Avatargzb 50-motd-news[3986>
Sep 30 04:43:20 Avatargzb 50-motd-news[3986>
Sep 30 04:43:20 Avatargzb 50-motd-news[3986>
Sep 30 04:43:20 Avatargzb systemd[1]: motd->
Sep 30 04:43:20 Avatargzb systemd[1]: Finis>
Sep 30 04:43:20 Avatargzb systemd[1]: motd->
Sep 30 04:45:00 Avatargzb kernel: workqueue>
Sep 30 04:50:25 Avatargzb systemd[1]: Start>
Sep 30 04:50:26 Avatargzb systemd[1]: sysst>
```
```c
avatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-07-logs$ journalctl -f
Sep 30 04:51:28 Avatargzb systemd[1]: session-7.scope: Deactivated successfully.
Sep 30 04:51:27 Avatargzb sshd-session[4772]: pam_unix(sshd:session): session closed for user avatar
Sep 30 04:51:28 Avatargzb systemd[1]: session-7.scope: Consumed 5.638s CPU time over 6.233s wall clock time, 31.5M memory peak.
Sep 30 04:51:27 Avatargzb sshd-session[4772]: syslogin_perform_logout: logout() returned an error
Sep 30 04:51:28 Avatargzb systemd-logind[841]: Session 7 logged out. Waiting for processes to exit.
Sep 30 04:51:28 Avatargzb systemd-logind[841]: Removed session 7.
Sep 30 04:51:42 Avatargzb sshd-session[4881]: Accepted password for avatar from 192.168.56.1 port 52544 ssh2
Sep 30 04:51:42 Avatargzb sshd-session[4881]: pam_unix(sshd:session): session opened for user avatar(uid=1000) by avatar(uid=0)
Sep 30 04:51:42 Avatargzb systemd-logind[841]: New session '8' of user 'avatar' with class 'user' and type 'tty'.
Sep 30 04:51:43 Avatargzb systemd[1]: Started session-8.scope - Session 8 of User avatar.
^[[A^Cavatar@Avatargzb:~/HCLTech_Project/learning/phase-0-linux/lab-07-logs$ journalctl -f
Sep 30 04:51:28 Avatargzb systemd[1]: session-7.scope: Deactivated successfully.
Sep 30 04:51:27 Avatargzb sshd-session[4772]: pam_unix(sshd:session): session closed for user avatar
Sep 30 04:51:28 Avatargzb systemd[1]: session-7.scope: Consumed 5.638s CPU time over 6.233s wall clock time, 31.5M memory peak.
Sep 30 04:51:27 Avatargzb sshd-session[4772]: syslogin_perform_logout: logout() returned an error
Sep 30 04:51:28 Avatargzb systemd-logind[841]: Session 7 logged out. Waiting for processes to exit.
Sep 30 04:51:28 Avatargzb systemd-logind[841]: Removed session 7.
Sep 30 04:51:42 Avatargzb sshd-session[4881]: Accepted password for avatar from 192.168.56.1 port 52544 ssh2
Sep 30 04:51:42 Avatargzb sshd-session[4881]: pam_unix(sshd:session): session opened for user avatar(uid=1000) by avatar(uid=0)
Sep 30 04:51:42 Avatargzb systemd-logind[841]: New session '8' of user 'avatar' with class 'user' and type 'tty'.
Sep 30 04:51:43 Avatargzb systemd[1]: Started session-8.scope - Session 8 of User avatar.
```

## What I Observed

* Recent system events were displayed by `journalctl`.
* New events appeared while using `journalctl -f`.
* Actions performed in another terminal generated new log entries.

## What I Learned

`journalctl` allows me to inspect events recorded in the systemd journal.

`journalctl -f` is useful for **live monitoring of new system events**.

## Project Connection

The incident detection system can monitor Linux logs and use these events as input for detecting suspicious activities.
