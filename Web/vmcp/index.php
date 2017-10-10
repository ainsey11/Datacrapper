<?php require "../login/loginheader.php"; ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Matrix</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <link rel="icon" type="image/png" href="favicon.png" />
    <!-- Bootstrap -->
    <link href="../css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="../css/main.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <div class="form-signin">
        <div class="alert alert-success">Welcome to the Matrix Control Panel</div>
	<br>
	</div>
	<a href="matrixtemps.php" class="btn btn-default btn-lg btn-block">View VM Status</a>
	<a href="http://matrix:5000" class="btn btn-default btn-lg btn-block">Start VM</a>
	<a href="http://matrix:8384" class="btn btn-default btn-lg btn-block">Reboot VM</a>
	<a href="http://matrix:8384" class="btn btn-default btn-lg btn-block">Reset VM</a>
	<a href="http://matrix:8384" class="btn btn-default btn-lg btn-block">Shutdown VM</a>
	<a href="http://matrix:8384" class="btn btn-default btn-lg btn-block">Save VM</a>
	<a href="http://matrix:8384" class="btn btn-default btn-lg btn-block">Suspend VM</a>
	<a href="http://matrix:8384" class="btn btn-default btn-lg btn-block">Resume VM</a>
	<div class="container">
		<div class="form-signin">
		<a href="../index.php" class="btn btn-default btn-lg btn-block">Return to Main Menu</a>
		<a href="login/logout.php" class="btn btn-default btn-lg btn-block">Logout</a>
		</div>
	</div>
  </body>
</html>
