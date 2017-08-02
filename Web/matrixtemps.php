<?php 

require "login/loginheader.php"; 
?>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Datacrapper Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <link rel="icon" type="image/png" href="favicon.png" />
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="css/main.css" rel="stylesheet" media="screen">
  </head>
<body>
<div class="container">
      <div>
		<?php
		$cmd = shell_exec('sensors');
		?>
		<h2>The current temperatures of Matrix are:</h2>
		<pre> 
			<?=$cmd?>
		</pre>
		<br>
		<div class="form-signin">
		        <a href="/matrixtemps.php" class="btn btn-default btn-lg btn-block">Refresh Temperature Values</a>
		        <a href="/index.php" class="btn btn-default btn-lg btn-block">Return to Main Menu</a>
        	</div>	
	</div>
</div>
</body>
</html>	
