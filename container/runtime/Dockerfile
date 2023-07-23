FROM ubuntu:22.04
COPY sources.list /etc/apt/sources.list
COPY timezone /etc/
RUN apt update \
    && apt upgrade -y \
    && apt install -y python3 python3-pip libmysqlclient-dev python3-socks vim iputils-ping telnet libjpeg-dev \
    && python3 -m pip install --upgrade pip \
    && pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

ENTRYPOINT ["/usr/sbin/init"]