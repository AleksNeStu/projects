
# How to Disable Auto-Start of Docker Containers on Fedora Linux

Follow these steps to prevent Docker containers from automatically starting after a system reboot.

---

## 1. List All Containers
To identify all containers and their current status, run:
```bash
docker ps -a --format "table {{.ID}}\t{{.Names}}\t{{.State}}\t{{.Status}}"
```

---

## 2. Stop All Running Containers
Stop all currently running containers with the following command:
```bash
docker stop $(docker ps -q)
```

---

## 3. Check the Restart Policy of a Specific Container
For any container, check its restart policy by running:
```bash
docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' <container_id_or_name>
```

---

## 4. Disable Auto-Restart for All Containers
Disable the auto-restart policy for all containers in one go:
```bash
docker ps -a -q | xargs -I {} docker update --restart=no {}
```

---

## 5. Verify Changes
Recheck the restart policy for a container to confirm the change:
```bash
docker inspect -f '{{.HostConfig.RestartPolicy.Name}}' <container_id_or_name>
```

---

## 6. (Optional) Disable Docker Service Auto-Start
If you want to prevent Docker itself from starting at boot, disable the Docker service:
```bash
sudo systemctl disable docker
```

To re-enable it later:
```bash
sudo systemctl enable docker
```

---

By following these steps, Docker containers will no longer auto-start after a system reboot.
