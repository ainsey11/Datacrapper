<?php require "login/loginheader.php"; ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Matrix</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <link rel="icon" type="image/png" href="favicon.png" />
    <!-- Bootstrap -->
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="css/main.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <div class="form-signin">
        <div class="alert alert-success">Welcome to the Matrix Control Panel</div>
	<br>
	</div>
	<a href="/launchworkalerts.php" class="btn btn-default btn-lg btn-block">Restart Apache</a>
	<a href="content/launchfblerts.php" class="btn btn-default btn-lg btn-block">Restart MySQL</a>
	<a href="matrixtemps.php" class="btn btn-default btn-lg btn-block">Restart Zoneminder</a>
	<a href="matrixtemps.php" class="btn btn-default btn-lg btn-block">Restart Plex Media Server</a>
	<a href="matrixtemps.php" class="btn btn-default btn-lg btn-block">Restart Sonarr</a>
	<a href="matrixtemps.php" class="btn btn-default btn-lg btn-block">Restart Couchpotato</a>
	<a href="matrixtemps.php" class="btn btn-default btn-lg btn-block">Restart SabNZBD</a>
	<a href="content/.php" class="btn btn-default btn-lg btn-block">View Local Matrix Monitoring</a>
	<a href="content/.php" class="btn btn-default btn-lg btn-block">View Matrix Temperatures</a>
	<a href="content/.php" class="btn btn-default btn-lg btn-block">View Matrix Disk Space Statistics</a>
	<div class="container">
		<div class="form-signin">
		<a href="login/logout.php" class="btn btn-default btn-lg btn-block">Logout</a>
		</div>
	</div>
  </body>
</html>
