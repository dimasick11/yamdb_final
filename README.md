# infra_sp2

Учебный проект от Яндекс.Практикум, представляет собой DRF API приложение базы отзывов о фильмах, книгах и музыке с пройденым код ревью.

##### **Стек технологий:**
* Python3
* Django
* Django REST Framework
* Docker
* Docker-compose

#### **Установка:**
1. В папке с репозиторием выполнить `sudo docker-compose up`
2. В запущенном контейнере выполнить `python3 manage.py migrate`, `python3 manage.py createsuperuser`, `python3 manage.py loaddata data/fixtures.json ` 
`

##### Подробная документация основана на Redoc и доступна по адресу: <http://127.0.0.1:8020/redoc> после запуска контейнера
