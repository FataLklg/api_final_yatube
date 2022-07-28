# Api_final_yatube
____
###### API проект для блога Yatube, в котором реализованы следующие возможности:
+ _создание постов, с выбором подходящей группы и их последующее редактирование (CRUD) автором поста_
+ _добавление и редактирование комментариев к постам_
+ _возможность подписки/отписки на(от) автора_
+ _поиск по подпискам_
### Как запустить проект:
____

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/FataLklg/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов:
___
- _GET-запрос на вывод всех постов:_
    http://127.0.0.1:8000/api/v1/posts/
    _Вывод:_
    ```
    [
    {
        "id": 1,
        "author": "test_user",
        "text": "Тестовый текст.",
        "pub_date": "2022-07-27T16:14:07.909958Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "test_user",
        "text": "Тестовый текст1.",
        "pub_date": "2022-07-27T16:17:29.687122Z",
        "image": null,
        "group": 1
    },
    ...
    ```
- _POST-запрос на добавление нового поста:_
    http://127.0.0.1:8000/api/v1/posts/
    ```
    {
        "text": "Новый пост",
        "group": 1
    }
    ```
    _Вывод:_
    ```
    {
        "id": 5,
        "author": "test_user",
        "text": "Новый пост",
        "pub_date": "2022-07-28T18:22:48.312554Z",
        "image": null,
        "group": 1
    }
    ```
- _POST-запрос на добавление нового комментария к созданному посту:_
    http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
    ```
    {
        "text": "Новый комментарий"
    }
    ```
    _Вывод:_
    ```
    {
        "id": 1,
        "author": "test_user",
        "text": "Новый комментарий",
        "created": "2022-07-28T18:28:52.407174Z",
        "post": 1
    }
    ```
- _GET-запрос на вывод всех сообществ:_
        http://127.0.0.1:8000/api/v1/groups/
        _Вывод:_
    ```
    {
        "id": 1,
        "title": "Живопись",
        "slug": "painting",
        "description": "Всё о живописи"
    },
    {
        "id": 2,
        "title": "Поэзия",
        "slug": "poetry",
        "description": "Всё о поэзии"
    },
    ```
- _POST-запрос для подписки:_
    http://127.0.0.1:8000/api/v1/follow/
    ```
    {
        "following": "test1_user"
    }
    ```
    _Вывод:_
    ```
    {
        "id": 12,
        "user": "test_user",
        "following": "test1_user"
    }
    ```
### Авторы:
___
- ##### __Антон Тарасов__

