## Create Docker credentials secret

export DOCKER_SERVER=https://index.docker.io/v1/

export DOCKER_USER=[...]


export DOCKER_PASS=[...]

kubectl create secret \
    docker-registry regcred \
    --docker-server=$DOCKER_SERVER \
    --docker-username=$DOCKER_USER \
    --docker-password=$DOCKER_PASS 