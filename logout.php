<?php
/**
 * Created by PhpStorm.
 * User: Robert
 * Date: 22/07/2017
 * Time: 00:56
 */
session_start(); //Start the current session
session_destroy(); //Destroy it! So we are logged out now
header("location:login.php?msg=Successfully Logged out"); // Move back to login.php with a logout message
?>