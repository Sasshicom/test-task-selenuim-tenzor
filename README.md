# test-task-selenuim-tenzor
Реализация проекта автотестов на Selenuim + pytest с паттерном page-object-model
В проекте не используются библиотеки для логирования

Запуск тестов выполняется из корня проекта командами: 
    pytest .\tests\test_scenario1.py
    pytest .\tests\test_scenario2.py

Каждый отдельный тест внутри .py файла может быть вызван через "::" н-р:
    pytest .\tests\test_scenario1.py::test_check_img_size
