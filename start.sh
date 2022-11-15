#!/bin/sh

for filename in input.yaml set1.yaml set2.yaml
do
 echo "################################################################"
 echo "Processing $filename" 
 python pizza.py $filename
 echo "################################################################"
done