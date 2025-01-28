# REST API для управления кошельками

Стек:

```FastAPI```
```PostgreSQL```
```Docker```
```Pytest```

Асинхронное приложение по работе с кошельками.

## Установка
### 1. Клонирование репозитория
```
Клонируйте проект при помощи Git
```
##### Пример
```
git clone https://github.com/LenaNS/CashFlow.git
```
### 2. Запустить приложение
```
Конфигурация находится в файле docker-compose.yml,
воспользуйтесь docker для установки
```
##### Пример
```
docker-compose up -d
```

Документация доступна по адресу ```http://127.0.0.1:8000/docs```

### Кошелёк
+ **POST**   ```/api/v1/wallets/<WALLET_UUID>/operation``` выполнение операции списания/начисления
+ **GET** ```/api/v1/wallets/{WALLET_UUID}``` просмотр баланса кошелька