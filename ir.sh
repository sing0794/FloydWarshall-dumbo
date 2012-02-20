#!/bin/bash
hadoop fs -rmr output
dumbo start doccount.py -hadoop /usr/lib/hadoop -input input -output output
D=$(dumbo cat output/part-00000 -hadoop /usr/lib/hadoop)
hadoop fs -rmr output
dumbo start FloydWarshall.py -param $D -hadoop /usr/lib/hadoop -input input -output output 
dumbo cat output/part-00000 -hadoop /usr/lib/hadoop > output.txt

