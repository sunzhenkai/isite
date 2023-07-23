FROM registry.cn-hangzhou.aliyuncs.com/sunzhenkai/isite-runtime:v1.0.0
WORKDIR /app/isite
COPY dist/ .
COPY entrypoint.sh .

RUN pip3 install -r requirements
EXPOSE 18080

ENTRYPOINT ["bash", "entrypoint.sh"]