for i in `ls *csv`
do
	rm $i
done

sleep 1

bash ./trading_data_MAIN.sh && sleep 1 && python ./trading_data_MAIN2.py && sleep 1 && python RSI_VALS.py
