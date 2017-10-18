var=$( ls | wc -l )
echo $var

python PushjetService.py $var
