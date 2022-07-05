<?php
 $csp= "Content-Security-Policy: frame-ancestors *";
 header("$csp");
 echo "<h3>".$csp."</h3>";
?>
