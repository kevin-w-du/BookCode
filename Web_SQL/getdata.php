<?php
   function getDB() {
     $dbhost="localhost";
     $dbuser="root";
     $dbpass="seedubuntu";
     $dbname="dbtest";

     // Create a DB connection
     $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
     if ($conn->connect_error) {
         die("Connection failed: " . $conn->connect_error . "\n");
     }
     return $conn;
   }

   $eid = $_GET['EID'];
   $pwd = $_GET['Password'];

   $conn = new mysqli("localhost", "root", "seedubuntu", "dbtest");
   $sql = "SELECT Name, Salary, SSN             
           FROM employee
           WHERE eid= '$eid' and password='$pwd'";  

   $result = $conn->query($sql);
   if ($result) {
      // Print out the result
      while ($row = $result->fetch_assoc()) {
        printf ("Name: %s -- Salary: %s -- SSN: %s\n",
                $row["Name"], $row["Salary"], $row['SSN']);
      }
      $result->free();
   }
   $conn->close();
?>

