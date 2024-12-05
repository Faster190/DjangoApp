Игровой магазин.
========================
Сайт был написан без определённого ТЗ - функционал может быть расширен, внешний вид изменён.

### Компоненты программы:
В папке находятся несколько файлов, необходимых для работы сайта.
В директории "GameShop" находятся настройки самого проекта и адреса приложений, так как для удобства регистрация с авторизацией находятся отдельно от представлений, шаблонов, моделей и адресов основного сайта.
В директории "RegLog" находятся шаблоны, представления и адреса страниц с авторизацией, регистрацией, профилем и деавторизацией пользователя.
В директории "media" находятся обложки игр для отображения на сайте.
В директории "shop" находятся шаблоны, представления и адреса страниц с играми, главной страницей, играми по жанрам и "О сайте".
Файл "db.sqlite3" является базой данных сайта с играми и зарегистрированными пользователями.
Файл "manage.py" помогает запустить сервер.
Файл "requirements.txt" содержит названия необходимых библиотек для работы проекта.

### Описание работы сайта и взаимодействие с пользователем:
На главной странице показываются все игры на сайте с их жанрами. Нажав на плашку с игрой, переадресовывает на её личную страничку с описанием и кнопкой "Купить". В шапке сайта есть плашка "Жанры" - это выпадающее меню с жанрами - можно отфильтровать игры по жанрам. Во время входа пользователя при указании имени, которого нет в базе, или при вводе неверного пароля будет ошибка с пояснением. Чтобы зарегистрироваться, необходимо указать имя и почту, которые не используются каким-нибудь пользователем, в противном случае возникнет ошибка с пояснением причины. Пароли пользователей хранятся в базе в зашифрованном виде.

_________________________

* ### Как запустить?
В консоли, находясь в папке проекта, прописать "pyrhon manage.py runserver". Запустится тестовый сервер на компьютере, также в консоли будет адрес локального хоста сайта.
_________________________________
### Скриншоты работы программы:

Сайт:
![image](https://github.com/user-attachments/assets/f96d48e3-1f36-49a0-b42a-015871acfce1)
![image](https://github.com/user-attachments/assets/1d1e68d1-b6b1-4a97-a2a4-ae87df7dc83c)
![image](https://github.com/user-attachments/assets/59664023-541a-41ee-a133-7d385372f525)
![image](https://github.com/user-attachments/assets/dd8bcea4-82b5-4990-bfa4-5434e89925cf)
![image](https://github.com/user-attachments/assets/212f9d1e-4462-48d1-ad2c-0ec63832fa3c)


Ошибки:
![image](https://github.com/user-attachments/assets/b2e4978a-93c0-4716-afa9-b3a408eecb72)
![image](https://github.com/user-attachments/assets/c948366e-7eaf-4ba7-966e-1f0e61bc141f)



