# Parse Backend
---
Backend приложение парсинга через api


## API Reference
Ссылки по документации приложения:
- [OpenAPI yaml](http://127.0.0.1:8000/api/schema/)
- [Redoc UI](http://127.0.0.1:8000/api/docs/redoc/)
- [Swagger UI](http://127.0.0.1:8000/api/docs/swagger/)

## Архитектура проекта

Так как в этом проекте имеется только CRUD. Выбрал архитектуру Monolite. А Паттерн Database per Service. Если проект был бы  по 
больше, то выбрал DDD(Domain Driven Design)


## Run local

``` bash
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py runserver

```
## First api

В Swagger есть api который называется getFromApi. Отправьте запрос чтобы он смог создать данные на базе данных





## Environment
Есть два места для <b>локальной</b> разработки переменные среды указаны внутри `docker-compose.yml`, <b>для dev/prod среды и развертывания в кластере</b> указываются в `./helm/values.{dev}.yaml`, так же для кластера секьюрные переменные указываются через <b>kubernetes secrets</b>. 


## Additional Information

### Admin
Данный сервис имеет только интерфейсы админ панели доступные по урлу: `<домен>/admin/`

### Superuser
Для того чтобы создать суперюзера система чтобы получить доступ к админ панели необходимо создать юзера следующим способом:
1Запустить команду:
- `python manage.py createsuperuser`
2Указать следующие данные по последовательному промпту, который появляется в терминале:
- `username`
- `email`[optional]
- `password`
- `password confirmation`