- [Посещаемость](#org1c9cd2b)
- [Процесс](#orga4ba244)
- [Поток](#org1366820)
- [Что можно узнать про процесс?](#org89d6c36)
- [создание процессов](#org5277fbc)
- [создание потоков](#orgd644526)
- [CPU-bound / IO-bound задачи](#org8c9eab5)
- [GIL](#org1eebd95)
- [GIL](#org521282f)
- [GIL](#orgfff31f4)
- [GIL](#orgd9e8a43)
- [Практика](#org0308ef3)
- [Дополнительная литература](#orgdc40d22)
- [Что такое Celery?](#org99792ff)
- [Практика запуска задач на Celery](#org7d55189)
- [Практика запуска задач на Celery](#orgc392076)
- [Celery и Django](#org058de32)
- [Почитать](#orgb429866)
- [Что такое map-reduce](#org3460efd)
- [Практика запуска map-reduce на pyspark](#orgdac1090)
- [Практика запуска map-reduce на pyspark](#org194ec8f)
- [Вопросы-ответы](#org5e10886)



<a id="org1c9cd2b"></a>

# Посещаемость

![img](qrcode.png)  


<a id="orga4ba244"></a>

# Процесс

Это программа, находящаяся в режиме выполнения. Операционная система подгружает в оперативную память с каждым процессом  

-   Саму программу
-   Данные к программе
-   Стек программы

Переключение между процессами происходит на уровне ядра.  


<a id="org1366820"></a>

# Поток

****Потоков не существует! Есть только процессы, но чуть-чуть другие \Smiley[][yellow]****  
![img](CLONEFlags.png)  

-   Каждый процесс состоит из минимум одного потока.
-   Потоки разделяют общее адресное пространство процесса.

<span class="underline"><span class="underline">[подробнее (SO)](https://stackoverflow.com/a/809049)</span></span>  


<a id="org89d6c36"></a>

# Что можно узнать про процесс?

```shell
# посмотреть все процессы
ps alx
# посмотреть все процессы пользователя
ps a -u
ps a -u redis
# добавить информацию о тредах
ps -eLf
# здесь "хранится" процесс
ls -l /proc/<PID>/
```


<a id="org5277fbc"></a>

# создание процессов

Для создания нового процесса используются системные вызовы копирования процесса:  

-   **clone:** UNIX-системы
-   **CreateProcess:** Win2k-системы


<a id="orgd644526"></a>

# создание потоков

В Linux это тот же $clone$, только мы говорим ему, не копировать память, а "шарить"  
![img](PwTDC.png)  


<a id="org8c9eab5"></a>

# CPU-bound / IO-bound задачи

-   **CPU-bound:** задачи, которые активно используют CPU. Арифметические операции, матричные вычисления, поиск строк, и т.д.
-   **IO-bound:** задачи, связанные с вводом-выводом данных. Работа с сетью, с файловыми системами, с пользовательским вводом


<a id="org1eebd95"></a>

# GIL

<span class="underline"><span class="underline">[Python/ceval.c](https://github.com/python/cpython/blob/e62a694fee53ba7fc16d6afbaa53b373c878f300/Python/ceval.c#L238)</span></span>  

```C
/* This is the GIL */
static PyThread_type_lock
       interpreter_lock = 0;
```


<a id="org521282f"></a>

# GIL

GIL гарантирует интерпретатору, что только один *поток* может быть запущен в текущий момент. Это сделано для безопасной работы управления памятью, вызова расширений написанных на других языках (на C).  


<a id="orgfff31f4"></a>

# GIL

![img](GIL.png)  

-   sys.getcheckinterval()  # -> Python2
-   sys.getswitchinterval() # -> Python3


<a id="orgd9e8a43"></a>

# GIL

GIL замедляет CPU-bound задачи. Старая реализация GIL очень плохо работала с *CPU-bound + IO-bound* задачами. <span class="underline"><span class="underline">[Пример](https://dabeaz.blogspot.com/2010/01/python-gil-visualized.html)</span></span>, да и новая не лучше.  


<a id="org0308ef3"></a>

# Практика

<span class="underline"><span class="underline">[GitHub](https://github.com/pimiento/python_threads_examples/)</span></span>  


<a id="orgdc40d22"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[GIL](https://realpython.com/python-gil/)</span></span>
-   <span class="underline"><span class="underline">[UnderstandingGIL.pdf](https://www.dabeaz.com/python/UnderstandingGIL.pdf)</span></span>
-   <span class="underline"><span class="underline">[Groking The GIL](https://opensource.com/article/17/4/grok-gil)</span></span>
-   <span class="underline"><span class="underline">[GIL и его влияние на многопоточность в Python](https://habr.com/ru/post/592189/)</span></span>
-   <span class="underline"><span class="underline">[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)</span></span>


<a id="org99792ff"></a>

# Что такое Celery?

<span class="underline"><span class="underline">[Официальная документация](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)</span></span>  
\newline{}  
*Celery* это брокер задач, который позволяет в фоновом, асинхронном режиме выполнять задачи в отдельных процессах/тредах и/или на других машинах.  


<a id="org7d55189"></a>

# Практика запуска задач на Celery

```shell
pip install celery
apt install rabbitmq-server
```

-   <span class="underline"><span class="underline">[Можно описывать сложные последовательности](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#groups)</span></span>


<a id="orgc392076"></a>

# Практика запуска задач на Celery

```shell
cd celery_example
docker compose up -d
celery -A tasks worker --loglevel=INFO
./runner.py
```


<a id="org058de32"></a>

# Celery и Django

![img](django_celery.png)  


<a id="orgb429866"></a>

# Почитать

-   [Habr](https://habr.com/ru/companies/otus/articles/503380/)
-   [Перевод документации](https://django.fun/ru/articles/tutorials/django-i-celery-1-ustanovka/)


<a id="org3460efd"></a>

# Что такое map-reduce

Это процесс решения больших задач при помощи разбивки данных на части и решения задач с частями данных на разных машинах. MapReduce состоит из обязательных шагов:  

1.  Map — разбить данные на блоки (присвоить каждой записи некоторый ключ блока)
2.  Shuffle — присвоить каждому блоку некоторый ключ (*не-уникальный* между всеми блоками)
3.  Reduce — для каждого ключа выполнить некоторую функцию над всеми данными в этом ключе


<a id="orgdac1090"></a>

# Практика запуска map-reduce на pyspark

*[тестовая сборка для работы с Hadoop](https://medium.com/analytics-vidhya/how-to-easily-install-hadoop-with-docker-ad094d556f11) (надо дополнительно поставить python на namenode)*  

-   <span class="underline"><span class="underline">[mapper.py](https://github.com/pimiento/python_threads_examples/blob/main/mapper.py)</span></span>
-   <span class="underline"><span class="underline">[reducer.py](https://github.com/pimiento/python_threads_examples/blob/main/reducer.py)</span></span>


<a id="org194ec8f"></a>

# Практика запуска map-reduce на pyspark

-   запуск на NameNode  
    
    ```shell
    hdfs dfs -rm -r -skipTrash\
         /d/out
    hadoop jar /opt/hadoop-2.7.4/share\
           /hadoop/tools/lib/\
           hadoop-streaming-2.7.4.jar\
           -files /root/mapper.py,\
           /root/reducer.py\
           -mapper /root/mapper.py\
           -reducer /root/reducer.py\
           -input /d/in/98.txt\
           -output /d/out
    hdfs dfs -cat /d/out/part-00000
    ```


<a id="org5e10886"></a>

# Вопросы-ответы

![img](questions.jpg)
