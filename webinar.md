- [Процесс](#org894111b)
- [Поток](#org6e6dc76)
- [Что можно узнать про процесс?](#org4489b51)
- [создание процессов](#orgda58787)
- [CPU-bound / IO-bound задачи](#org80f12eb)
- [GIL](#orgeb329d0)
- [GIL](#org52bff51)
- [GIL](#org5cebcea)
- [GIL](#orgb0c63de)
- [Практика](#orgdb90323)
- [Дополнительная литература](#org9e2b58a)
- [Что такое Celery?](#org577b902)
- [Практика запуска задач на Celery](#org99d8fa4)
- [Что такое map-reduce](#orgcc8f331)
- [Практика запуска map-reduce на pyspark](#org33ad796)
- [Практика запуска map-reduce на pyspark](#org1445a37)
- [Вопросы-ответы](#org963d0b8)



<a id="org894111b"></a>

# Процесс

Это программа, находящаяся в режиме выполнения. Операционная система подгружает в оперативную память с каждым процессом  

-   Саму программу
-   Данные к программе
-   Стек программы

Переключение между процессами происходит на уровне ядра.  


<a id="org6e6dc76"></a>

# Поток

-   Каждый процесс состоит из минимум одного потока.
-   Потоки разделяют общее адресное пространство процесса.

Переключение между потоками может происходить как на уровне ядра, так и на уровне пользователя (процесса).  


<a id="org4489b51"></a>

# Что можно узнать про процесс?

```shell
ps alx
```

```shell
ls -l /proc/<PID>/
```


<a id="orgda58787"></a>

# создание процессов

Для создания нового процесса используются системные вызовы копирования процесса:  

-   **fork:** UNIX-системы
-   **CreateProcess:** Win2k-системы


<a id="org80f12eb"></a>

# CPU-bound / IO-bound задачи

-   **CPU-bound:** задачи, которые активно используют CPU. Арифметические операции, матричные вычисления, поиск строк, и т.д.
-   **IO-bound:** задачи, связанные с вводом-выводом данных. Работа с сетью, с файловыми системами, с пользовательским вводом


<a id="orgeb329d0"></a>

# GIL

<span class="underline"><span class="underline">[Python/ceval.c](https://github.com/python/cpython/blob/e62a694fee53ba7fc16d6afbaa53b373c878f300/Python/ceval.c#L238)</span></span>  

```C
/* This is the GIL */
static PyThread_type_lock
       interpreter_lock = 0;
```


<a id="org52bff51"></a>

# GIL

GIL гарантирует интерпретатору, что только один *поток* может быть запущен в текущий момент. Это сделано для безопасной работы управления памятью, вызова расширений написанных на других языках (на C).  


<a id="org5cebcea"></a>

# GIL

![img](/home/pimiento/yap/GIL.png)  

-   sys.getcheckinterval()  # -> Python2
-   sys.getswitchinterval() # -> Python3


<a id="orgb0c63de"></a>

# GIL

GIL замедляет CPU-bound задачи. Старая реализация GIL очень плохо работала с *CPU-bound + IO-bound* задачами. <span class="underline"><span class="underline">[Пример](https://dabeaz.blogspot.com/2010/01/python-gil-visualized.html)</span></span>, да и новая не лучше.  


<a id="orgdb90323"></a>

# Практика

<span class="underline"><span class="underline">[GitHub](https://github.com/pimiento/python_threads_examples/)</span></span>  


<a id="org9e2b58a"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[GIL](https://realpython.com/python-gil/)</span></span>
-   <span class="underline"><span class="underline">[UnderstandingGIL.pdf](https://www.dabeaz.com/python/UnderstandingGIL.pdf)</span></span>
-   <span class="underline"><span class="underline">[Groking The GIL](https://opensource.com/article/17/4/grok-gil)</span></span>
-   <span class="underline"><span class="underline">[GIL и его влияние на многопоточность в Python](https://habr.com/ru/post/592189/)</span></span>
-   <span class="underline"><span class="underline">[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)</span></span>


<a id="org577b902"></a>

# Что такое Celery?

<span class="underline"><span class="underline">[Официальная документация](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)</span></span>  
\newline{}  
*Celery* это брокер задач, который позволяет в фоновом, асинхронном режиме выполнять задачи в отдельных процессах/тредах и/или на других машинах.  


<a id="org99d8fa4"></a>

# Практика запуска задач на Celery

```shell
pip install celery
apt install rabbitmq-server
```

-   <span class="underline"><span class="underline">[Можно описывать сложные последовательности](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#groups)</span></span>


<a id="orgcc8f331"></a>

# Что такое map-reduce

Это процесс решения больших задач при помощи разбивки данных на части и решения задач с частями данных на разных машинах. MapReduce состоит из обязательных шагов:  

1.  Map — разбить данные на блоки (присвоить каждой записи некоторый ключ блока)
2.  Shuffle — присвоить каждому блоку некоторый ключ (*не-уникальный* между всеми блоками)
3.  Reduce — для каждого ключа выполнить некоторую функцию над всеми данными в этом ключе


<a id="org33ad796"></a>

# Практика запуска map-reduce на pyspark

*[тестовая сборка для работы с Hadoop](https://medium.com/analytics-vidhya/how-to-easily-install-hadoop-with-docker-ad094d556f11) (надо дополнительно поставить python на namenode)*  

-   <span class="underline"><span class="underline">[mapper.py](https://github.com/pimiento/python_threads_examples/blob/main/mapper.py)</span></span>
-   <span class="underline"><span class="underline">[reducer.py](https://github.com/pimiento/python_threads_examples/blob/main/reducer.py)</span></span>
-   создадим директорию в HDFS для данных и вывода (на NameNode)  
    
    ```shell
    hdfs dfs -mkdir /d
    ```


<a id="org1445a37"></a>

# Практика запуска map-reduce на pyspark

-   запуск на NameNode  
    
    ```shell
    hdfs dfs -rmdir\
         --ignore-fail-on-non-empty\
         /d/out
    hadoop jar /opt/hadoop-2.7.4/share\
           /hadoop/tools/lib/\
           hadoop-streaming-2.7.4.jar\
           -files /root/mapper.py,\
           /root/reducer.py\
           -mapper /root/mapper.py\
           -reducer /root/reducer.py\
           -input /d/out/98.txt\
           -output /d/out
    hdfs dfs -cat /d/out/part-00000
    ```


<a id="org963d0b8"></a>

# Вопросы-ответы

![img](/home/pimiento/yap/questions.jpg)
