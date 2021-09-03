# Prog_Veeam_TEST

Задания выполнены на языке Python 3

## **Задача 1:**  
### _task_1.py_

Реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом. Конфигурационный файл должен иметь формат xml. Для каждого файла в конфигурационном файле должно быть указано его имя, исходный путь и путь, по которому файл требуется скопировать.

Пример
Конфигурационный файл:

```
<config>
    <file
            source_path="C:\Windows\system32"
            destination_path="C:\Program files"
            file_name="kernel32.dll"
    />
    <file
            source_path="/var/log"
            destination_path="/etc"
            file_name="server.log"
    />
</config>
```


дополнительные файлы:
* settings.ini
* config.xml
* config.xsd


## **Задача 2:** 
### _task_2.py_

Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл и проверяющую целостность файлов.
Пример
Файл сумм:
* file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
* file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
* file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
* file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709

Пример вызова:  
```
<your program> <path to the input file> <path to the directory containing the files to check>
```

Формат вывода:
```
file_01.bin OK
file_02.bin FAIL
file_03.bin NOT FOUND
file_04.txt OK
```

дополнительные файлы:
* check.txt
* file_01.bin
* file_02.bin
* file_04.txt

## **Задача 3:** 
### _task_3.py_

Напишите прототип тестовой системы, состоящей из двух тест-кейсов. В данной задаче использование стороннего модуля для автоматизации тестирования не приветствуется.
Тестовая система представляет собой иерархию классов, описывающую тест-кейсы. 

У каждого тест-кейса есть:
*	Номер (tc_id) и название (name)
*	Методы для подготовки (prep), выполнения (run) и завершения (clean_up) тестов. 
*	Метод execute, который задаёт общий порядок выполнения тест-кейса и обрабатывает исключительные ситуации. 

Все этапы выполнения тест-кейса, а также исключительные ситуации должны быть задокументированы в лог-файле или в стандартном выводе.

**Тест-кейс 1: Список файлов**
*	[prep] Если текущее системное время, заданное как целое количество секунд от начала эпохи Unix, не кратно двум, то необходимо прервать выполнение тест-кейса.
*	[run] Вывести список файлов из домашней директории текущего пользователя.
*	[clean_up] Действий не требуется.

**Тест-кейс 2: Случайный файл**
*	[prep] Если объем оперативной памяти машины, на которой исполняется тест, меньше одного гигабайта, то необходимо прервать выполнение тест-кейса.
*	[run] Создать файл test размером 1024 КБ со случайным содержимым.
*	[clean_up] Удалить файл test.


дополнительные файлы:
* logger.txt
