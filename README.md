# Local SRE Platform Infrastructure

This repository manages the local **SRE Control Plane** (NetBox & Jenkins). It is designed to manage any number of network sites (e.g., `syd1`, `mel1`) by connecting to them via their management IP addresses.

## Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) 
## 1. Start the Platform (NetBox & Jenkins)
To spin up the core SRE services, run:
```bash
docker-compose up -d
```
- **NetBox:** [http://localhost:8000](http://localhost:8000) (Default Token: `0123456789abcdef0123456789abcdef01234567`)
- **Jenkins:** [http://localhost:8080](http://localhost:8080)

## 2. Initialize Platform Metadata
Before syncing any network data, run the initialization script to prepare standard roles and manufacturers:
```bash
python3 scripts/netbox_initial_setup.py
```

## 3. Onboarding a New Site (e.g., mel1)
To add a new site to the ecosystem:
1.  **Bootstrap the data:**
    ```bash
    python3 ../NetworkAutomationCore/scripts/bootstrap_new_site.py mel1 "Melbourne Branch"
    ```
2.  **Edit the data:** Modify `NetworkInventoryData/intent/sites/mel1/devices.yml` to set the correct management IPs.
3.  **Sync to NetBox:**
    ```bash
    python3 ../NetworkAutomationCore/scripts/netbox_sync.py
    ```

## 4. Sync Network Intent
To sync all existing sites in the inventory:
```bash
# This script scans NetworkInventoryData/intent/sites/* for all site and device data
python3 ../NetworkAutomationCore/scripts/netbox_sync.py
```

## Role Naming Convention
We follow a 3-character role naming convention across the entire ecosystem:
- `acc`: Access
- `dis`: Distribution
- `cor`: Core
- `tra`: Transit
