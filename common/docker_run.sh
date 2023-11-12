# docker-compose -f ./docker-compose.yml -p common --env-file ./.env up -d
docker-compose -f ./docker-compose.yml -p common --env-file ./.env up -d --force-recreate --build


# Error response from daemon: Conflict. The container name "/db-postgresql" is already in use by container
# docker rm -f db-mysql
# docker rm -f db-redis
# docker rm -f db-postgresql




# Recreate
# Need to find the mysql volume and remove it after password changed.
#docker volume ls
## docker volume inspect
#docker stop $(docker ps -q)
#docker-compose down --volumes
#docker volume ls --filter "name=common_" -q | grep '^common_' | awk '{print $1}' | xargs -r docker volume rm

# docker-compose -f ./docker-compose.yml -p common --env-file ./sec.env up -d --no-cache --build
