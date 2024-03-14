FROM node:alpine
COPY . .

RUN apk add --update nodejs npm

WORKDIR ./vue-chat-app

RUN npm install

CMD npm run serve

EXPOSE 8080
