FROM node:alpine

ENV API_URL=http://localhost/api/

WORKDIR /app
COPY . /app

RUN npm install

CMD npm start