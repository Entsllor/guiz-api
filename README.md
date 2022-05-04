# Quiz API

> Тестовое задание на позицию Python разработчик

## Описание задачи

Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:

1. В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num":
   integer} ;

2. После получения запроса сервис, в свою очередь, запрашивает с публичного API
   https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.

3. Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая
   информация: 1. ID вопроса, Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса.
   В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы
   до тех пор, пока не будет получен уникальный
   вопрос для викторины.
4. Ответом на запрос из п.2 должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой
   объект.

В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2, его
настройке и запуску. А также пример запроса к POST API сервиса.

## Installation

```shell
git clone https://github.com/Entsllor/guiz-api
```


## Pre-requirements

Create ./app/.env file and set env variables

```dotenv
# ./app/.env
APP_DB_URL=postgresql+asyncpg://user:pass@db:5432/postgres
```

If you run project via docker-compose set hostname as 'db' (as in docker-compose.yml file)
else you can use 'localhost' or any other hostname.

All app variables should start with a specific prefix 'APP_'.

### Install docker and docker-compose

[Install Docker](https://docs.docker.com/engine/install/ubuntu/)

[Install Docker-compose](https://docs.docker.com/compose/install/)

## Run

Just write this command

```shell
docker-compose up --build
```
