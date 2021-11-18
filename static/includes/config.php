<?php
$db_username = "admin";
$db_password = "admin";
$db_name = "dbvoice";
$db_host = "localhost";
$db = mysqli_connect($db_host, $db_username, $db_password,$db_name);

setlocale(LC_TIME, "fr_FR");