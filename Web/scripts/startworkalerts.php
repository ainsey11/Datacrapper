<?php

include 'fix_mysql.inc.php';

$DBhost = "localhost";
$DBuser = "datacrapperdbuser";
$DBpass = "aRdZA4SGugnNtoJk";
$DBName = "datacrapperdb";
$table = "workalerts";

$connection = ssh2_connect('172.16.1.41', 22);
ssh2_auth_password($connection, 'root', 'carsrule');
$stream = ssh2_exec($connection, 'cd /media/sdcard/EdiNag/; bash test.sh &');
stream_set_blocking($stream, true);
$stream_out = ssh2_fetch_stream($stream, SSH2_STREAM_STDIO);
#echo stream_get_contents($stream_out);

$id = uniqid();
$time = date_create()->format('Y-m-d H:i:s');
$pid = stream_get_contents($stream_out);
$action = "start";

$con = mysqli_connect($DBhost,$DBuser,$DBpass) or die("lolz good luck");

mysqli_select_db($con,"$DBName");
mysqli_query($con,
	"INSERT INTO $table (id,time,action,pid) 
	VALUES ('$id','$time','$action','$pid')");
mysqli_close($con);

print "Script launched. PID = $pid, DB info written at: $time, action was: $action, ID was $id";

?>

