<?php
 $csp= "Content-Security-Policy: frame-ancestors 'self'";
 header("$csp");
 echo "<h3>".$csp."</h3>";
?>
