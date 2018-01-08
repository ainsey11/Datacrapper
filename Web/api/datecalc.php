<html>
<body>
	<?php
#	print_r ($_GET)
	(int)$futureyear= ($_GET["futureyear"]);
	(int)$futuremonth= $_GET['futuremonth'];
	(int)$futureday= $_GET["futureday"];
	$cmd = shell_exec('python ../scripts/datecalc.py'.  '$futureyear $futuremonth $futureday');
	?>
</body>
</html>
