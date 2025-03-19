# Overview

# Running on Docker

## Build/Run the docker-compose

```bash
docker-compose up -d
```

## Check all active container Ports

```bash
docker ps --format "table {{.Names}}\t{{.Ports}}"
```
