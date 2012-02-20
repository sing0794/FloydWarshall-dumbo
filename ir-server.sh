#!/bin/bash
INDIR="$1"
OUTDIR="$2"
hadoop fs -rmr $OUTDIR
dumbo start doccount.py -hadoop /usr/local/hadoop -input $INDIR -output $OUTDIR
D=$(dumbo cat $OUTDIR/part-00000 -hadoop /usr/local/hadoop)
hadoop fs -rmr $OUTDIR
dumbo start FloydWarshall.py -param $D -numreducetasks 44 -hadoop /usr/local/hadoop -input $INDIR -output $OUTDIR
dumbo cat $OUTDIR/part-00000 -hadoop /usr/local/hadoop > output.txt

