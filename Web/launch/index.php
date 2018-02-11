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
	<a href="http://matrix:8989" class="btn btn-default btn-lg btn-block">Launch Sonarr</a>
	<a href="http://matrix:7878" class="btn btn-default btn-lg btn-block">Launch Radarr</a>
	<a href="http://matrix:8080" class="btn btn-default btn-lg btn-block">Launch SabNZBD</a>
	<a href="http://matrix:32400/Web" class="btn btn-default btn-lg btn-block">Launch Plex</a>
	<a href="http://matrix:8112" class="btn btn-default btn-lg btn-block">Launch Deluge</a>
	<a href="http://matrix/zm" class="btn btn-default btn-lg btn-block">Launch Zoneminder Console</a>
	<a href="http://matrix:8181/" class="btn btn-default btn-lg btn-block">Launch PlexPy Console</a>
	<a href="http://matrix:3000/" class="btn btn-default btn-lg btn-block">Launch Grafana</a>
	<a href="http://matrix:8880/" class="btn btn-default btn-lg btn-block">Launch OpenHab UI Selector</a>
	<div class="container">
		<div class="form-signin">
		<a href="../index.php" class="btn btn-default btn-lg btn-block">Return to Main Menu</a>
		<a href="../login/logout.php" class="btn btn-default btn-lg btn-block">Logout</a>
		</div>
	</div>
  </body>
</html>
