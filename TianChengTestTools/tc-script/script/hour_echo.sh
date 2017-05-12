#!/bin/sh


 # 每天晚上23 点执行 clean操作
current_hour=`date +%k`
if [ "23" == $current_hour ] || [ "11" == $current_hour ]; then
	echo $current_hour
fi


