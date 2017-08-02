<?php 

require "../login/loginheader.php"; 
?>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Matrix Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <link rel="icon" type="image/png" href="favicon.png" />
    <link href="../css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="../css/main.css" rel="stylesheet" media="screen">
  </head>
<body>
<div class="container">
      <div>
		<?php
		$cmd = shell_exec('df -h');
		?>
		<h2>The current disk stats for Matrix are:</h2>
		<pre> 
			<?=$cmd?>
		</pre>
		<br>
		<div class="form-signin">
		        <a href="diskstats.php" class="btn btn-default btn-lg btn-block">Refresh Disk Statistics</a>
		        <a href="index.php" class="btn btn-default btn-lg btn-block">Return to MCP Menu</a>
		        <a href="/index.php" class="btn btn-default btn-lg btn-block">Return to Main Menu</a>
        	</div>	
	</div>
</div>
</body>
</html>	
