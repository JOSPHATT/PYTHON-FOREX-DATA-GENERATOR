#!/bin/sh

for i in `ls | grep "forex"`;
do
	rm $i
done

sleep 1

curl https://finance.yahoo.com/currencies >forex_data.txt

cat forex_data.txt | tr " " "\n" | head -n 7000 | grep "value" | grep "fin-streamer" | uniq >forex_values.txt

while read -r V
do
	string=$V;
	echo ${string:7:5}>>forex_value_edited.txt;   done<forex_values.txt

cat forex_data.txt | tr " " "\n" | head -n 8000 | grep "data-symbol" | uniq >forexdata.txt

while read -r L
do
	string=$L;
	echo ${string:12:9}>>forex_data_edited.txt;
done<forexdata.txt

cat forex_value_edited.txt >forex_value_edited$1.txt
cat forex_data_edited.txt | grep "=X" | sed 's/[^a-zA-Z0-9]//g' | uniq>forex_symbols.txt

#cat forex_symbols.txt | wc



cp forex_value_edited$1.txt /data/data/com.termux/files/home/FOREXPYTHON

cp forex_symbols.txt /data/data/com.termux/files/home/FOREXPYTHON
