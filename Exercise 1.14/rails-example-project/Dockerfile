FROM ruby:2.6.0

WORKDIR /app/
COPY . /app/

RUN apt-get update
RUN apt-get install -y nodejs

RUN gem install bundler && bundle install

EXPOSE 3000
RUN rails db:migrate

CMD ["rails", "server"]