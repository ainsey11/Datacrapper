<html>
<body>
<?php
	$date = strtotime("January 8, 2018 5:00 PM");
	$remaining = $date - time();
	$days_remaining = floor($remaining / 86400);
	echo "There are $days_remaining";
	?>	
</body>
</html>

