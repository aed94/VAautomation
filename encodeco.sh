#!/bin/bash

[ $# -le 1 ] && { echo "Usage: $0 operation iterations filename"; exit 1; }

operation=$1
iterations=$2
filename=$3
code=$( cat $filename )
for ((i=1; i<=$iterations; i++)) 
do
if [ "$operation" == "decode" ]; then
code=$( echo "$code" | base64 -di )
elif [ "$operation" == "encode" ]; then
code=$( echo "$code" | base64 )
else 
echo "Please try again"
fi
echo -e "\nIteration number $i...."
echo $code
done
