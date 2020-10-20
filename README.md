# yamdb_final
[![Yamdb-app workflow](https://github.com/dimasick11/yamdb_final/workflows/Yamdb-app_workflow/badge.svg)](https://github.com/dimasick11/yamdb_final/actions)

Учебный проект от Яндекс.Практикум, представляет собой DRF API приложение базы отзывов о фильмах, книгах и музыке с пройденым код ревью.

##### **Стек технологий:**
* Python3
* Django
* Django REST Framework
* Docker
* Docker-compose

## Build
`docker-compose build`.

## Migrate databases
`docker-compose run --rm web code/manage.py migrate`.

## Run
`docker-compose up`.

##### Подробная документация основана на Redoc и доступна по адресу: <http://127.0.0.1:8020/redoc> после запуска контейнера
