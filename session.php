<?php
/**
 * Created by PhpStorm.
 * User: Robert
 * Date: 22/07/2017
 * Time: 01:44
 */

// Establishing Connection with Server by passing server_name, user_id and password as a parameter
$connection = mysql_connect("172.16.1.200", "datacrapper", "datacrapper");
// Selecting Database
$db = mysql_select_db("datacrapper", $connection);
session_start();// Starting Session
// Storing Session
$user_check=$_SESSION['login_user'];
// SQL Query To Fetch Complete Information Of User
$ses_sql=mysql_query("select username from login where username='$user_check'", $connection);
$row = mysql_fetch_assoc($ses_sql);
$login_session =$row['username'];
if(!isset($login_session)){
    mysql_close($connection); // Closing Connection
    header('Location: index.php'); // Redirecting To Home Page
}
?>