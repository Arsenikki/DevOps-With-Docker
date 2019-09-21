FROM ubuntu

RUN apt-get update && apt-get install -y curl 
WORKDIR /app
COPY script.sh .

CMD ["/bin/bash", "script.sh"]