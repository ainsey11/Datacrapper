<?php
/**
 * Created by PhpStorm.
 * User: Robert
 * Date: 22/07/2017
 * Time: 01:44
 */

session_start();
if(session_destroy()) // Destroying All Sessions
{
    header("Location: index.php"); // Redirecting To Home Page
}
?>