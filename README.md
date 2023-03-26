## Телеграмм бот HR_SMS&VIV

Для запуска:

Заменить файл ```expl.config.py``` на ```config.py```. В этом файле в переменную BOT_API_KEY положить ключ.

### Deploy

Создать образ приложения из Dockerfile
```
docker build . -t t_bot
```

Запустить контейнер с ботом

```
docker run t_bot
```

