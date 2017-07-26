<?php require "login/loginheader.php"; ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Datacrapper Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <!-- Bootstrap -->
    <link href="css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="css/main.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <div class="form-signin">
        <div class="alert alert-success">Welcome to the Datacrapper Control Panel</div>
	<br>
	</div>
	<a href="content/launchworkalerts.php" class="btn btn-default btn-lg btn-block">Launch EdiNag Work Alerts</a>
	<a href="content/launchfblerts.php" class="btn btn-default btn-lg btn-block">Launch EdiNag Facebook Alerts</a>
	<a href="content/viewservertemps.php" class="btn btn-default btn-lg btn-block">View Matrix Temperatures</a>
	<a href="content/.php" class="btn btn-default btn-lg btn-block">Enter Matrix Control Panel</a>
	<a href="content/.php" class="btn btn-default btn-lg btn-block">Enter Datacrapper Control Admin Panel</a>
	<a href="content/.php" class="btn btn-default btn-lg btn-block">Other useful links and things</a>
	<div class="container">
		<div class="form-signin">
		<a href="login/logout.php" class="btn btn-default btn-lg btn-block">Logout</a>
		</div>
	</div>
  </body>
</html>
