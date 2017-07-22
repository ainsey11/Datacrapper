
<?php
/**
 * Created by PhpStorm.
 * User: Robert
 * Date: 22/07/2017
 * Time: 00:55
 */

/**********************************************************************
  *dbHost = Host of the MySQL DataBase Server
 *dbUser = Username
 *dbPass = Password
 *dbName = Name of your DataBase
 **********************************************************************/
$dbHost = '172.16.1.200';
$dbUser = 'datacrapper';
$dbPass = 'datacrapper';
$dbName = 'datacrapperdb';
$dbC = mysqli_connect($dbHost, $dbUser, $dbPass, $dbName)
or die('Error Connecting to MySQL DataBase');
?>