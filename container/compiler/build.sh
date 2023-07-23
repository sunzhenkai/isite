#!/bin/bash
set -x
BASE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd "$BASE" || exit 1

# build docker image
VERSION="$(cat $BASE/VERSION)"
IMAGE_NAME="sunzhenkai/isite-compiler"
REGISTRY=registry.cn-hangzhou.aliyuncs.com
docker build -t $IMAGE_NAME "$BASE" || exit 1
docker tag $IMAGE_NAME $REGISTRY/$IMAGE_NAME:$VERSION
docker push $REGISTRY/$IMAGE_NAME:$VERSION