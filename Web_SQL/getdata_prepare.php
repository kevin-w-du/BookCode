<?php
   $conn = new mysqli("localhost", "root", "seedubuntu", "dbtest");
   $sql = "SELECT Name, Salary, SSN
           FROM employee
           WHERE eid= ? and password=?";              
   if ($stmt = $conn->prepare($sql)) {               
      $stmt->bind_param("ss", $eid, $pwd);          
      $stmt->execute();                             
      $stmt->bind_result($name, $salary, $ssn);     
      while ($stmt->fetch()) {                      
         printf ("%s %s %s\n", $name, $salary, $ssn);
      }
   }
?>
