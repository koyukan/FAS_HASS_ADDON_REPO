ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 \
    py3-urllib3

WORKDIR /data

# Copy files
COPY run.sh /
COPY dog_server.py /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]