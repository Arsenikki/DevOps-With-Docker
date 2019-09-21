docker run -it ubuntu
RUN apt-get update && apt-get install -y curl 
sh -c 'echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website;'