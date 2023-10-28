#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files avgmapper.py,avgreducer.py \
-input /mapreduce/average/testavg.txt \
-output /mapreduce/average/output04 \
-mapper avgmapper.py \
-reducer avgreducer.py 

