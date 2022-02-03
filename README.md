# Компиляция Cython

1.  Для компиляции cython-скриптов в Linux вам понадобится установить некоторые зависимости

        apt install build-essential
        # поменяйте на используемую вами версию
        apt install python3.8-dev
        pip3 install cython --upgrade
2.  генерируем C-файл

        cython3 -D --embed -3 -o <scriptname>.c <scriptname>.pyx
3.  компилируем бинарник

        # поменяйте на используемую вами версию
        gcc -Os -I /usr/include/python3.8 -o <scriptname> <scriptname>.c -lpython3.8 -lpthread -lm -lutil -ldl
4.  можно запускать

        ./<scriptname>
