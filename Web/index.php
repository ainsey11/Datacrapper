<?php require "login/loginheader.php"; ?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Datacrapper</title>
    <meta name="viewport" content="width=device-width, initial-scale=10.0">
    <link rel="icon" type="image/png" href="favicon.png" />
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
	<a href="/launch/index.php" class="btn btn-default btn-lg btn-block">Start Launch Panel</a>
	<a href="/launchworkalerts.php" class="btn btn-default btn-lg btn-block">Start Kill Panel</a>
	<a href="mcp/index.php" class="btn btn-default btn-lg btn-block">Enter Matrix Control Panel</a>
	<a href="dcp/index.php" class="btn btn-default btn-lg btn-block">Enter Datacrapper Control Admin Panel</a>
	<a href="somerandomlinkivenotworkedout.php" class="btn btn-default btn-lg btn-block">Other useful links and things</a>
	<div class="container">
		<div class="form-signin">
		<a href="login/logout.php" class="btn btn-default btn-lg btn-block">Logout</a>
		</div>
	</div>
  </body>
</html>
