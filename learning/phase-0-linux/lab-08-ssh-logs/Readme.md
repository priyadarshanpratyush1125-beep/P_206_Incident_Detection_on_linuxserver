# Lab 08 — SSH Logs

## Objective

Understand how Linux records SSH authentication events and how failed login attempts can be observed in logs.

## Commands Used

```bash id="w4n6pc"
systemctl status ssh
journalctl -u ssh -n 30
journalctl -u ssh -f
```

> If my system uses `sshd`, I use `sshd` instead of `ssh`.

## Terminal Output

### SSH Service

```c

```

### Recent SSH Logs

```c

```

### Failed Login Event

```c

```

## What I Observed

A failed SSH login generated an authentication-related event in the Linux journal.

The log contains useful information about the login attempt, such as the time and user involved.

## What I Learned

SSH authentication events can be monitored using `journalctl`.

Repeated failed authentication events can later be used as input for an **incident detection rule**.

## Project Connection

This is directly related to my project because the detector can monitor SSH logs and identify **repeated failed login attempts**.
