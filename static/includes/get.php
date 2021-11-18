<?php

function getNbPublishedword() {
    global $db;
    $sql = "SELECT COUNT(*) FROM motscles";
    $query = mysqli_query($db, $sql);
    $res = mysqli_fetch_array($query);
    $count = $res['COUNT(*)'];

    return $count;
}


?>