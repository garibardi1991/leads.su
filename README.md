# Проект по автоматизации тестирования LEADS.SU
<a target="_blank" href="https://leads.su/">Сайт проекта</a>

## :world_map: Содержание
- [Технологии и инструменты](#earth_africa-технологии-и-инструменты)
- [Примеры UI тестов](#pager-Примеры-UI-тестов)
- [Примеры API тестов](#scroll-Примеры-API-тестов)
- [Сборка в Jenkins с параметрами](#-Сборка-в-Jenkins-с-параметрами)
- [Allure отчет](#-Allure-отчет)
- [Отчет в Telegram с помощью бота](#-Отчет-в-Telegram-с-помощью-бота)
- [Видео прохождения тестов на Selenoid](#film_projector-Видео-прохождения-тестов-на-Selenoid)

## :earth_africa: Технологии и инструменты
<p>
<a href="https://www.jetbrains.com/pycharm/"><img src="icons/PyCharm_Icon.svg" width="50" height="50"  alt="Pycharm" title="IntelliJ IDEA"/></a>
<a href="https://www.python.org/"><img src="icons/python.svg" width="50" height="50"  alt="Python" title="Python"/></a>
<a href="https://github.com/"><img src="icons/Github.svg" width="50" height="50"  alt="Github" title="GitHub"/></a>
<a href="https://www.selenium.dev/"><img src="icons/selenium.svg" width="50" height="50"  alt="Selenium" title="Selenium"/></a>
<a href="https://selenide.org/"><img src="icons/Selenide.svg" width="50" height="50"  alt="Selenide" title="Selenide"/></a>
<a href="https://aerokube.com/selenoid/"><img src="icons/Selenoid.svg" width="50" height="50"  alt="Selenoid" title="Selenoid"/></a>
<a href="https://github.com/allure-framework/allure2"><img src="icons/Allure_Report.svg" width="50" height="50"  alt="Allure" title="Allure"/></a>
<a href="https://www.jenkins.io/"><img src="icons/Jenkins.svg" width="50" height="50"  alt="Jenkins" title="Jenkins"/></a>
<a href="https://github.com/yashaka/selene"><img src="icons/selene.png" width="50" height="50"  alt="Selene" title="Selene"/></a>
</p>

В данном проекте автотесты написаны на <code>Python</code> с использованием <code>Selenium</code>, <code>Selene</code> и <code>Pytest</code> для UI-тестов
>
> <code>Selenoid</code> выполняет запуск браузеров в контейнерах <code>Docker</code>.
>
> <code>Allure Report</code> формирует отчет о запуске тестов.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.


## :pager: Примеры UI тестов
- Проверка входа в систему
- Проверка отображения витрины в конструкторе
- Проверка работы кнопки сокращения ссылок


## :scroll: Примеры API тестов
- Пока в разработке

## <img src="icons/Jenkins.svg" width="25" height="25"  alt="Jenkins" title="Jenkins"/></a> Сборка в Jenkins с параметрами
>
> В сборке присутствуют настраиваемые параметры.
>
> Например версия запускаемого браузера или платформа тестируемого сайта. Сами тесты запускаются удаленно с помощью <code>Selenoid</code>
<p align="center">
<img title="Сборка в Jenkins с параметрами" src="icons/Jenkins parametrs.png">
</p>

## <img src="icons/Allure_Report.svg" width="25" height="25"  alt="Allure_Report" title="Allure_Report" title="Allure_Report"/></a> Allure отчет
>
> Allure формирует подробный отчет о прогоне тестов. Кастомные фильтры и листенеры делают отчет максимально понятным
>
> Например в отчет пишутся все селекторы и методы <code>Selene</code>, отчеты формируются по категориям, в конце приложен скриншот, видео запись прогона теста и логи.
Для API тестов полностью указаны данные запроса/ответа
<p align="center">
<img title="Allure отчет" src="icons/Allure1.png">
</p>
<p align="center">
<img title="Allure отчет" src="icons/Allure2.png">
</p>
<p align="center">
<img title="Allure отчет" src="icons/Allure3.png">
</p>

## <img width="4%" title="Telegram" src="icons/Telegram.svg"> Отчет в Telegram с помощью бота
>
> После прогона всех тестов в <code>Telegram</code> чат автоматически приходит сообщение с полной информацией о прогоне и ссылкой на <code>Allure</code>
>
<p>
<img title="Отчет в Telegram с помощью бота" src="icons/Telegram Results.png">
</p>

## :film_projector: Видео прохождения тестов на Selenoid
>
> <code>Selenoid</code> пишет видео прогона каждого теста и видео прикладывается в отчет <code>Allure</code>
>
<p>
<img title="Selenoid Video" src="icons/Allure4.gif" alt="video">
</p>