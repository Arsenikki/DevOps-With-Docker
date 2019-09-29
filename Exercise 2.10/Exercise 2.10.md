Rebuild images and start containers with docker-compose:

    docker-compose up --force-recreate

Changes in dockerfiles: 

    ENV API_URL=http://localhost/api/
    and
    ENV FRONT_URL=http://localhost/
