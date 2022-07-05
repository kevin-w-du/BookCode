<?php
 $csp= "Content-Security-Policy: frame-ancestors www.attacker32.com";
 header("$csp");
 echo "<h3>".$csp."</h3>";
?>
