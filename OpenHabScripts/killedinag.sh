#/bin/bash
ssh root@172.16.1.43 -t "kill $(ps | grep 'sh -c while true; do python /media/sdcard/EdiNag/workalerts.py; sleep 1; done' | awk '{print $1}'); exit"

sleep 2


ssh root@172.16.1.43 -t "kill $(ps | grep 'sh -c while true; do python /media/sdcard/EdiNag/workalerts.py; sleep 1; done' | awk '{print $1}'); exit" 
