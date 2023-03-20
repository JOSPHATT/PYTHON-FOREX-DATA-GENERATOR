
#!/bin/bash

for i in `ls | grep "values_edited"`;
do
	rm $i
done


for((num=0; num<80; num=num+1));
do
	bash get_4rex_data_now.sh $num && python2 txt_2_csv.py values_edited$num.txt values_edited$num.csv;
	sleep 5; 
done 



