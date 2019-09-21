FROM node:alpine as base

WORKDIR /app
COPY . /app

RUN npm install && \
    npm run build 

FROM node:alpine AS release
COPY --from=base /app/ /app/
WORKDIR /app
RUN npm install -g serve

ENV API_URL=http://localhost/api/

CMD ["serve", "-s", "-l", "5000","dist"]