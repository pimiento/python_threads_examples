- [Процесс](#org762bda2)
- [Поток](#org5dc47c6)
- [Что можно узнать про процесс?](#orgfeba161)
- [создание процессов](#org6cce12c)
- [CPU-bound / IO-bound задачи](#org5ad0424)
- [GIL](#org07b0b1a)
- [GIL](#org60438bc)
- [GIL](#orge3bb46a)
- [GIL](#org92cb10f)
- [Практика](#orge33495c)
- [Дополнительная литература](#org66964be)
- [Что такое Celery?](#org88fd6aa)
- [Практика запуска задач на Celery](#org4de842c)
- [Что такое map-reduce](#org1bd1356)
- [Практика запуска map-reduce на pyspark](#orgc1da91f)
- [Практика запуска map-reduce на pyspark](#org67f9531)
- [Вопросы-ответы](#orgcbd9bab)



<a id="org762bda2"></a>

# Процесс

Это программа, находящаяся в режиме выполнения. Операционная система подгружает в оперативную память с каждым процессом  

-   Саму программу
-   Данные к программе
-   Стек программы

Переключение между процессами происходит на уровне ядра.  


<a id="org5dc47c6"></a>

# Поток

-   Каждый процесс состоит из минимум одного потока.
-   Потоки разделяют общее адресное пространство процесса.

Переключение между потоками может происходить как на уровне ядра, так и на уровне пользователя (процесса).  


<a id="orgfeba161"></a>

# Что можно узнать про процесс?

```shell
ps alx
```

```shell
ls -l /proc/<PID>/
```


<a id="org6cce12c"></a>

# создание процессов

Для создания нового процесса используются системные вызовы копирования процесса:  

-   **fork:** UNIX-системы
-   **CreateProcess:** Win2k-системы


<a id="org5ad0424"></a>

# CPU-bound / IO-bound задачи

-   **CPU-bound:** задачи, которые активно используют CPU. Арифметические операции, матричные вычисления, поиск строк, и т.д.
-   **IO-bound:** задачи, связанные с вводом-выводом данных. Работа с сетью, с файловыми системами, с пользовательским вводом


<a id="org07b0b1a"></a>

# GIL

<span class="underline"><span class="underline">[Python/ceval.c](https://github.com/python/cpython/blob/e62a694fee53ba7fc16d6afbaa53b373c878f300/Python/ceval.c#L238)</span></span>  

```C
/* This is the GIL */
static PyThread_type_lock
       interpreter_lock = 0;
```


<a id="org60438bc"></a>

# GIL

GIL гарантирует интерпретатору, что только один *поток* может быть запущен в текущий момент. Это сделано для безопасной работы управления памятью, вызова расширений написанных на других языках (на C).  


<a id="orge3bb46a"></a>

# GIL

![img](/home/pimiento/yap/GIL.png)  

-   sys.getcheckinterval()  # -> Python2
-   sys.getswitchinterval() # -> Python3


<a id="org92cb10f"></a>

# GIL

GIL замедляет CPU-bound задачи. Старая реализация GIL очень плохо работала с *CPU-bound + IO-bound* задачами. <span class="underline"><span class="underline">[Пример](https://dabeaz.blogspot.com/2010/01/python-gil-visualized.html)</span></span>, да и новая не лучше.  


<a id="orge33495c"></a>

# Практика

<span class="underline"><span class="underline">[GitHub](https://github.com/pimiento/python_threads_examples/)</span></span>  


<a id="org66964be"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[GIL](https://realpython.com/python-gil/)</span></span>
-   <span class="underline"><span class="underline">[UnderstandingGIL.pdf](https://www.dabeaz.com/python/UnderstandingGIL.pdf)</span></span>
-   <span class="underline"><span class="underline">[Groking The GIL](https://opensource.com/article/17/4/grok-gil)</span></span>
-   <span class="underline"><span class="underline">[GIL и его влияние на многопоточность в Python](https://habr.com/ru/post/592189/)</span></span>
-   <span class="underline"><span class="underline">[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)</span></span>


<a id="org88fd6aa"></a>

# Что такое Celery?

<span class="underline"><span class="underline">[Официальная документация](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)</span></span>  
\newline{}  
*Celery* это брокер задач, который позволяет в фоновом, асинхронном режиме выполнять задачи в отдельных процессах/тредах и/или на других машинах.  


<a id="org4de842c"></a>

# Практика запуска задач на Celery

```shell
pip install celery
apt install rabbitmq-server
```

-   <span class="underline"><span class="underline">[Можно описывать сложные последовательности](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#groups)</span></span>


<a id="org1bd1356"></a>

# Что такое map-reduce

Это процесс решения больших задач при помощи разбивки данных на части и решения задач с частями данных на разных машинах. MapReduce состоит из обязательных шагов:  

1.  Map — разбить данные на блоки (присвоить каждой записи некоторый ключ блока)
2.  Shuffle — присвоить каждому блоку некоторый ключ (*не-уникальный* между всеми блоками)
3.  Reduce — для каждого ключа выполнить некоторую функцию над всеми данными в этом ключе


<a id="orgc1da91f"></a>

# Практика запуска map-reduce на pyspark

*[тестовая сборка для работы с Hadoop](https://medium.com/analytics-vidhya/how-to-easily-install-hadoop-with-docker-ad094d556f11) (надо дополнительно поставить python на namenode)*  

-   <span class="underline"><span class="underline">[mapper.py](https://github.com/pimiento/python_threads_examples/blob/main/mapper.py)</span></span>
-   <span class="underline"><span class="underline">[reducer.py](https://github.com/pimiento/python_threads_examples/blob/main/reducer.py)</span></span>
-   создадим директорию в HDFS для данных и вывода (на NameNode)  
    
    ```shell
    hdfs dfs -mkdir /d
    ```


<a id="org67f9531"></a>

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


<a id="orgcbd9bab"></a>

# Вопросы-ответы

![img](/home/pimiento/yap/questions.jpg)
