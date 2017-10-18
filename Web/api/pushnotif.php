<html>
<body>

	<?php
	(string)$argument = $_GET["name"];
	$cmd = shell_exec('python ../scripts/pushjet/PushjetService.py ' . $argument);
	?>
	
</body>
</html>
 					
