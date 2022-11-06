#!/bin/bash
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
