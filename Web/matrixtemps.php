<?php 

require "login/loginheader.php"; 
?>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Datacrapper Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="css/main.css" rel="stylesheet" media="screen">
  </head>
<body>
<div class="container">
      <div class="form-signin">
		<?php
			$cmd = 'sensors';
			$output = shell_exec($cmd);
		<?>
		The temps are: <?=$output?> <br />
	</div>
</div>
</body>
</html>	
