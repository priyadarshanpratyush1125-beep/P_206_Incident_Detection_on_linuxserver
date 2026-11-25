# Python Agent Configuration

## Overview

The Python monitoring agent will be responsible for collecting security-related events from remote Linux servers and forwarding detected incidents to the central P_206 application.

To make the agent easier to configure on different machines, its settings should be maintained separately from the detection logic.

## Configuration Options

The agent will require the following settings:

- **Server ID:** A unique identifier for the monitored Linux server.
- **Log File Path:** Location of the Linux authentication log.
- **API Endpoint:** Address of the central Flask backend.
- **Request Timeout:** Maximum time allowed for API communication.
- **Monitoring Interval:** Time between monitoring checks.

## Example Configuration

```ini
[agent]
server_id = linux-server-01
monitoring_interval = 10

[logs]
auth_log = /var/log/auth.log

[server]
api_endpoint = https://your-server.example/api/incidents
request_timeout = 10
```

## Security Considerations

- Keep API credentials outside the configuration file.
- Use HTTPS when communicating with the central backend.
- Validate incident data before transmission.
- Avoid storing passwords or sensitive authentication information in logs.

## Future Scope

The configuration system will be integrated with the Python monitoring agent during the implementation phase.
