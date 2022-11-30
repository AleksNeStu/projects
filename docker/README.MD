# I) URLS
[URL1](https://usrl1.com/) - URL1 desc\
[URL2](https://usrl2.com/) - URL2 desc


# II) Description
## [Dir](https://www.freecodecamp.org/news/where-are-docker-images-stored-docker-container-paths-explained/)
The storage location of Docker images and containers:
```
docker info
Fedora: /var/lib/docker/
        /var/lib/docker/overlay2 - images
Windows: C:\ProgramData\DockerDesktop
MacOS: ~/Library/Containers/com.docker.docker/Data/vms/0/
```

## Clean
## Purging All Unused or Dangling Images, Containers, Volumes, and Networks

Docker provides a single command that will clean up any resources — images, containers, volumes, and networks — that are _dangling_ (not tagged or associated with a container):

    docker system prune

Copy

To additionally remove any stopped containers and all unused images (not just dangling images), add the `-a` flag to the command:

    docker system prune -a

Copy

## Removing Docker Images

### Remove one or more specific images

Use the `docker images` command with the `-a` flag to locate the ID of the images you want to remove. This will show you every image, including intermediate image layers. When you’ve located the images you want to delete, you can pass their ID or tag to `docker rmi`:

**List:**

    docker images -a

Copy

**Remove:**

    docker rmi Image Image

Copy

### Remove dangling images

Docker images consist of multiple layers. Dangling images are layers that have no relationship to any tagged images. They no longer serve a purpose and consume disk space. They can be located by adding the filter flag `-f` with a value of `dangling=true` to the `docker images` command. When you’re sure you want to delete them, you can use the `docker image prune` command:

**Note:** If you build an image without tagging it, the image will appear on the list of dangling images because it has no association with a tagged image. You can avoid this situation by [providing a tag](https://docs.docker.com/engine/reference/commandline/build/#/tag-image--t) when you build, and you can retroactively tag an image with the [`docker tag`](https://docs.docker.com/engine/reference/commandline/tag/) command.

**List:**

    docker images -f dangling=true

Copy

**Remove:**

    docker image prune

Copy

### Removing images according to a pattern

You can find all the images that match a pattern using a combination of `docker images` and [`grep`](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux). Once you’re satisfied, you can delete them by using [`awk`](https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux) to pass the IDs to `docker rmi`. Note that these utilities are not supplied by Docker and are not necessarily available on all systems:

**List:**

    docker images -a |  grep "pattern"

Copy

**Remove:**

    docker images -a | grep "pattern" | awk '{print $3}' | xargs docker rmi

Copy

### Remove all images

All the Docker images on a system can be listed by adding `-a` to the `docker images` command. Once you’re sure you want to delete them all, you can add the `-q` flag to pass the image ID to `docker rmi`:

**List:**

    docker images -a

Copy

**Remove:**

    docker rmi $(docker images -a -q)

Copy

## Removing Containers

### Remove one or more specific containers

Use the `docker ps` command with the `-a` flag to locate the name or ID of the containers you want to remove:

**List:**

    docker ps -a

Copy

**Remove:**

    docker rm ID_or_Name ID_or_Name

Copy

### Remove a container upon exiting

If you know when you’re creating a container that you won’t want to keep it around once you’re done, you can run `docker run --rm` to automatically delete it when it exits:

**Run and Remove:**

    docker run --rm image_name

Copy

### Remove all exited containers

You can locate containers using `docker ps -a` and filter them by their status: `created`, `restarting`, `running`, `paused`, or `exited`. To review the list of `exited` containers, use the `-f` flag to filter based on status. When you’ve verified you want to remove those containers, use `-q` to pass the IDs to the `docker rm` command:

**List:**

    docker ps -a -f status=exited

Copy

**Remove:**

    docker rm $(docker ps -a -f status=exited -q)

Copy

### Remove containers using more than one filter

Docker filters can be combined by repeating the filter flag with an additional value. This results in a list of containers that meet either condition. For example, if you want to delete all containers marked as either `created` (a state which can result when you run a container with an invalid command) or `exited`, you can use two filters:

**List:**

    docker ps -a -f status=exited -f status=created

Copy

**Remove:**

    docker rm $(docker ps -a -f status=exited -f status=created -q)

Copy

### Remove containers according to a pattern

You can find all the containers that match a pattern using a combination of `docker ps` and [`grep`](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux). When you’re satisfied that you have the list you want to delete, you can use [`awk`](https://www.digitalocean.com/community/tutorials/how-to-use-the-awk-language-to-manipulate-text-in-linux) and `xargs` to supply the ID to `docker rm`. Note that these utilities are not supplied by Docker and are not necessarily available on all systems:

**List:**

    docker ps -a |  grep "pattern”

Copy

**Remove:**

    docker ps -a | grep "pattern" | awk '{print $1}' | xargs docker rm

Copy

### Stop and remove all containers

You can review the containers on your system with `docker ps`. Adding the `-a` flag will show all containers. When you’re sure you want to delete them, you can add the `-q` flag to supply the IDs to the `docker stop` and `docker rm` commands:

**List:**

    docker ps -a

Copy

**Remove:**

    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)

Copy

## Removing Volumes

### Remove one or more specific volumes - Docker 1.9 and later

Use the `docker volume ls` command to locate the volume name or names you wish to delete. Then you can remove one or more volumes with the `docker volume rm` command:

**List:**

    docker volume ls

Copy

**Remove:**

    docker volume rm volume_name volume_name

Copy

### Remove dangling volumes - Docker 1.9 and later

Since the point of volumes is to exist independent from containers, when a container is removed, a volume is not automatically removed at the same time. When a volume exists and is no longer connected to any containers, it’s called a _dangling volume_. To locate them to confirm you want to remove them, you can use the `docker volume ls` command with a filter to limit the results to dangling volumes. When you’re satisfied with the list, you can remove them all with `docker volume prune`:

**List:**

    docker volume ls -f dangling=true

Copy

**Remove:**

    docker volume prune

Copy

### Remove a container and its volume

If you created an unnamed volume, it can be deleted at the same time as the container with the `-v` flag. Note that this only works with _unnamed_ volumes. When the container is successfully removed, its ID is displayed. Note that no reference is made to the removal of the volume. If it is unnamed, it is silently removed from the system. If it is named, it silently stays present.

**Remove:**

    docker rm -v container_name

Copy



# III) Usage
1) Case1
2) Case2

# IV) Pros
1) Good1
2) Good2

# V) Cons
1) Bad1
2) Bad2

# VI) Compare
1) [difference between Docker Desktop for Linux and Docker Engine](https://docs.docker.com/desktop/faqs/linuxfaqs/#what-is-the-difference-between-docker-desktop-for-linux-and-docker-engine)\
   Docker Desktop for Linux and Docker Engine can be installed side-by-side on the same machine. Docker Desktop for Linux stores containers and images in an isolated storage location within a VM and offers controls to restrict its resources. Using a dedicated storage location for Docker Desktop prevents it from interfering with a Docker Engine installation on the same machine.
