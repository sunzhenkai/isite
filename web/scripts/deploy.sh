#!/bin/sh
set -x
set -e

[ -e ../server/templates/dist ] && rm -r ../server/templates/dist
cp -r dist ../server/templates/ && cp -r src/static/* ../server/templates/dist/static/
cd ../server 
[ -d static ] && rm -rf static
source venv/bin/activate && python3 manage.py collectstatic 