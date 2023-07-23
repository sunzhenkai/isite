#!/bin/bash
set -xe
BASE=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
cd "$BASE"

# build docker image
VERSION="$(cat $BASE/VERSION)"
IMAGE_NAME="sunzhenkai/isite-runtime"
REGISTRY=registry.cn-hangzhou.aliyuncs.com
docker build -t $IMAGE_NAME "$BASE"
docker tag $IMAGE_NAME $REGISTRY/$IMAGE_NAME:$VERSION
docker push $REGISTRY/$IMAGE_NAME:$VERSION