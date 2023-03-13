#!/bin/bash
i=0
while read line 
do
        arr[$i]="$line"
        i=$((i+1))
done < forex_symbols.txt
#echo ${arr[@]}

for fl in `ls | grep "value" | grep ".txt"`;
do
	echo $fl>>files.txt
done


for fil in `cat files.txt`;
do 
    values_line=$(tr -s '\n ' ',' < $fil)
    x=$values_line
    echo "${x%?}">>forex_new_data.txt
done

while read line
do
	echo $line
	sleep 1
done <forex_new_data.txt
