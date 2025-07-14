# DNS API

Это сервис для хранения доменов и записей. Реализован полный CRUD (Create, Read, Update, Delete).

## Функциональность 

### Домены

GET / - получить список доменов пользователя

GET /{domain_id} - получить домен по id

POST / - создать домен

PUT /{domain_id} - обновить домен

DELETE /{domain_id} - удалить домен

### Записи

`GET /{domain_id}/record` - получить записи по конкретному домену

`GET /{domain_id}/record/{record_id}` - получить запись по id для конкретного домена

`POST /{domain_id}/record` - создать запись для домена

`PUT /{domain_id}/record/{record_id}` - обновить запись

`DELETE /{domain_id}/record/{record_id}` - удалить запись

## Запуск

1. Подготовка окружения

make install-requirements

2. Запуск БД и приложения в докере

make docker

3. Подключение к БД

make db

4. Запуск приложения 

make app
