#!/bin/bash
#echo " This is a script to decode base64 encoded strings encoded multiple times"

[ $# -le 1 ] && { echo "Usage: $0 iterations filename"; exit 1; }

iterations=$1
filename=$2
code=$( cat $filename )
for ((i=1; i<=$iterations; i++)) 
do
code=$( echo "$code" | base64 -di )
echo -e "\nIteration number $i...."
echo $code
done
