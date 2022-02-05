- [Процесс](#orgf89a8f4)
- [Поток](#org28bb040)
- [Что можно узнать про процесс?](#org15b4dae)
- [создание процессов](#orgead8013)
- [CPU-bound / IO-bound задачи](#org05797c9)
- [GIL](#org8fa6a2f)
- [GIL](#org97bd1f7)
- [GIL](#orgadae331)
- [GIL](#org03400aa)
- [Практика](#org867bf1a)
- [Дополнительная литература](#org5be5e6f)
- [Что такое Celery?](#orgb09e9b0)
- [Практика запуска задач на Celery](#org5e20da1)
- [Что такое map-reduce](#orgba10464)
- [Практика запуска map-reduce на pyspark](#orgb2ae65a)
- [Вопросы-ответы](#orgb785fc1)



<a id="orgf89a8f4"></a>

# Процесс

Это программа, находящаяся в режиме выполнения. Операционная система подгружает в оперативную память с каждым процессом

-   Саму программу
-   Данные к программе
-   Стек программы

Переключение между процессами происходит на уровне ядра.


<a id="org28bb040"></a>

# Поток

-   Каждый процесс состоит из минимум одного потока.
-   Потоки разделяют общее адресное пространство процесса.

Переключение между потоками может происходить как на уровне ядра, так и на уровне пользователя (процесса).


<a id="org15b4dae"></a>

# Что можно узнать про процесс?

```shell
ps alx
```

```shell
ls -l /proc/<PID>/
```


<a id="orgead8013"></a>

# создание процессов

Для создания нового процесса используются системные вызовы копирования процесса:

-   **fork:** UNIX-системы
-   **CreateProcess:** Win2k-системы


<a id="org05797c9"></a>

# CPU-bound / IO-bound задачи

-   **CPU-bound:** задачи, которые активно используют CPU. Арифметические операции, матричные вычисления, поиск строк, и т.д.
-   **IO-bound:** задачи, связанные с вводом-выводом данных. Работа с сетью, с файловыми системами, с пользовательским вводом


<a id="org8fa6a2f"></a>

# GIL

<span class="underline"><span class="underline">[Python/ceval.c](https://github.com/python/cpython/blob/e62a694fee53ba7fc16d6afbaa53b373c878f300/Python/ceval.c#L238)</span></span>

```C
/* This is the GIL */
static PyThread_type_lock
       interpreter_lock = 0;
```


<a id="org97bd1f7"></a>

# GIL

GIL гарантирует интерпретатору, что только один *поток* может быть запущен в текущий момент. Это сделано для безопасной работы управления памятью, вызова расширений написанных на других языках (на C).


<a id="orgadae331"></a>

# GIL

![img](/home/pimiento/yap/GIL.png)

-   sys.getcheckinterval()  # -> Python2
-   sys.getswitchinterval() # -> Python3


<a id="org03400aa"></a>

# GIL

GIL замедляет CPU-bound задачи. Старая реализация GIL очень плохо работала с *CPU-bound + IO-bound* задачами. <span class="underline"><span class="underline">[Пример](https://dabeaz.blogspot.com/2010/01/python-gil-visualized.html)</span></span>


<a id="org867bf1a"></a>

# Практика

<span class="underline"><span class="underline">[GitHub](https://github.com/pimiento/python_threads_examples/)</span></span>


<a id="org5be5e6f"></a>

# Дополнительная литература

-   <span class="underline"><span class="underline">[GIL](https://realpython.com/python-gil/)</span></span>
-   <span class="underline"><span class="underline">[UnderstandingGIL.pdf](https://www.dabeaz.com/python/UnderstandingGIL.pdf)</span></span>
-   <span class="underline"><span class="underline">[Groking The GIL](https://opensource.com/article/17/4/grok-gil)</span></span>
-   <span class="underline"><span class="underline">[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)</span></span>


<a id="orgb09e9b0"></a>

# Что такое Celery?

<span class="underline"><span class="underline">[Официальная документация](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)</span></span>
\newline{}
*Celery* это брокер задач, который позволяет в фоновом, асинхронном режиме выполнять задачи в отдельных процессах/тредах и/или на других машинах.


<a id="org5e20da1"></a>

# Практика запуска задач на Celery

```shell
pip install celery
apt install rabbitmq-server
```


<a id="orgba10464"></a>

# Что такое map-reduce

Это процесс решения больших задач при помощи разбивки данных на части и решения задач с частями данных на разных машинах. MapReduce состоит из обязательных шагов:

1.  Map — разбить данные на блоки (присвоить каждой записи некоторый ключ блока)
2.  Shuffle — присвоить каждому блоку некоторый ключ (*не-уникальный* между всеми блоками)
3.  Reduce — для каждого ключа выполнить некоторую функцию над всеми данными в этом ключе


<a id="orgb2ae65a"></a>

# Практика запуска map-reduce на pyspark

<span class="underline"><span class="underline">[GitHub](https://github.com/pimiento/python_threads_examples/)</span></span>
*[тестовая сборка для работы с Hadoop](https://medium.com/analytics-vidhya/how-to-easily-install-hadoop-with-docker-ad094d556f11) (надо дополнительно поставить python на namenode)*


<a id="orgb785fc1"></a>

# Вопросы-ответы

![img](/home/pimiento/yap/questions.jpg)
