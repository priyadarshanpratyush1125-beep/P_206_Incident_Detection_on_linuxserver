# Distributed Linux Server Monitoring Architecture

## Overview

Currently, P_206 detects security incidents locally using Python scripts and Linux authentication logs. It can identify suspicious SSH login attempts and other activities on a monitored Linux server.

However, monitoring multiple Linux servers from a single dashboard requires a more flexible approach.

To address this limitation, I am planning to extend the project with a lightweight Python-based monitoring agent.

## Proposed Architecture

The idea is to run a small Python agent on each Linux server that needs to be monitored.

The agent will collect relevant system events, monitor SSH authentication logs and identify suspicious login activity. Whenever an incident is detected, it will send the event details to the central Flask backend through a secure API connection.

The central application will receive these events, store them in the SQLite database and display them on the existing incident detection dashboard.

## Key Components

- **Python Monitoring Agent:** Runs on remote Linux servers and monitors relevant system activity.
- **Log Monitoring:** Reads authentication logs to identify failed SSH attempts and suspicious login patterns.
- **Flask REST API:** Receives incident information from connected agents.
- **SQLite Database:** Stores incidents along with their timestamps and source server details.
- **Web Dashboard:** Provides a centralized view of incidents from multiple Linux servers.

## Expected Benefits

- Monitor multiple Linux servers from one dashboard.
- Reduce the need for a resource-intensive centralized security monitoring setup.
- Reuse the existing Python detection logic and Flask backend.
- Make deployment and monitoring easier for smaller environments.

## Future Improvements

- Implement the Python monitoring agent.
- Add secure authentication for individual agents.
- Support monitoring multiple remote servers.
- Introduce email notifications for critical incidents.
- Add agent health monitoring and connection status.

## Note

This document describes the proposed architecture. The distributed monitoring functionality will be implemented and tested in the next development phase.
