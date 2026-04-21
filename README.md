# SRE Platform Infrastructure

Local SRE control plane for managing SONiC-VS datacenter fabrics.

## Services

| Service | Port | Description |
|---------|------|-------------|
| NetBox | http://localhost:8000 | Network inventory and IPAM |
| Jenkins | http://localhost:8080 | CI/CD pipeline orchestration |
| ansible-agent | — | Jenkins build agent with Ansible + fping |

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quick Start

```bash
# Create the external network (one-time)
docker network create sre-mgmt-net

# Start all services
docker-compose up -d

# Initialize NetBox with standard roles and manufacturers
python3 scripts/netbox_initial_setup.py
```

## ansible-agent

The agent container includes:
- `ansible-core` with collections: `community.general`, `ansible.posix`, `netbox.netbox`, `ansible.utils`
- `fping` for device discovery
- `sshpass` for SONiC-VS SSH access
- `pynetbox`, `pyyaml`, `netaddr`

Volume mounts (for local development):
- `NetworkAutomationCore` → `/workspace/automation`
- `NetworkInventoryData` → `/workspace/inventory`

In production, Jenkins clones repos from GitHub into the agent workspace.

## Jenkins Agent Setup

1. Create a **Permanent Agent** node named `ansible-agent` with label `ansible-agent`
2. Copy the agent secret from the Jenkins UI
3. Set it and restart:
   ```bash
   JENKINS_AGENT_SECRET=<secret> docker-compose up -d ansible-agent
   ```
