FROM ubuntu:22.04
COPY sources.list /etc/apt/sources.list
COPY timezone /etc/
RUN apt update \
    && apt install -y npm
RUN npm set registry=https://registry.npmmirror.com
ENTRYPOINT ["/usr/sbin/init"]