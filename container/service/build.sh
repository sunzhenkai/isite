#!/bin/bash
set -x
BASE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
ROOT="$BASE/../.."
DIR_DIST="$ROOT/container/service/dist"
DIR_WEB="$ROOT/web"
DIR_SERVER="$ROOT/server"
DIR_CONTAINER="$ROOT/container"
RUNTIME_VERSION=$(cat $ROOT/container/runtime/VERSION)
COMPILER_VERSION=$(cat $ROOT/container/compiler/VERSION)
COMPILER_CONTAINER_NAME="isite-compiler-$COMPILER_VERSION"
COMPILER_IMAGE_NAME="sunzhenkai/isite-compiler"
REGISTRY=registry.cn-hangzhou.aliyuncs.com

# create dist dir
[ -e "$DIR_DIST" ] && rm -r "$DIR_DIST"
mkdir -p "$DIR_DIST"

BuildServer() {
    cd "$DIR_SERVER" || exit 1
    cp -r api "$DIR_DIST"
    cp -r isite "$DIR_DIST"
    cp -r static "$DIR_DIST"
    cp -r templates "$DIR_DIST"
    cp -r web "$DIR_DIST"
    cp requirements "$DIR_DIST"
    cp manage.py "$DIR_DIST"
}
 
BuildWeb() {
    docker inspect --format='{{.Name}}' $(docker ps -aq) | grep $COMPILER_CONTAINER_NAME
    [ ! $? -eq 0 ] && {
        docker run -it -d --privileged \
            -v $DIR_WEB:/code \
            --name=$COMPILER_CONTAINER_NAME $REGISTRY/$COMPILER_IMAGE_NAME:$COMPILER_VERSION 
    }
    docker exec -t $COMPILER_CONTAINER_NAME /bin/bash -c "cd /code && npm install && npm run build"

    cd "$DIR_WEB" || exit 1
    cp -r dist "$DIR_DIST/templates"
    cp -r static/* "$DIR_DIST/templates/dist/static/"
}

BuildServer
BuildWeb

# build docker image
VERSION="$(cat $BASE/VERSION)"
IMAGE_NAME="sunzhenkai/isite-service"
REGISTRY=registry.cn-hangzhou.aliyuncs.com
docker build -t $IMAGE_NAME "$BASE" || exit 1
docker tag $IMAGE_NAME $REGISTRY/$IMAGE_NAME:$VERSION
docker push $REGISTRY/$IMAGE_NAME:$VERSION
