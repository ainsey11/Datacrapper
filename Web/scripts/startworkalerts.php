<?php

$connection = ssh2_connect('172.16.1.41', 22);
ssh2_auth_password($connection, 'robert', 'carsrule');
$stream = ssh2_exec($connection, 'cd /home/robert/code/Datacrapper/; bash test.sh');
stream_set_blocking($stream, true);
$stream_out = ssh2_fetch_stream($stream, SSH2_STREAM_STDIO);
echo stream_get_contents($stream_out);

?>

