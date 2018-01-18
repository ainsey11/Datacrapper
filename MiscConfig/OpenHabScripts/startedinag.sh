#/bin/bash
 
ssh root@172.16.1.43 -t "while true; do python /media/sdcard/EdiNag/workalerts.py; sleep 1; done" &
