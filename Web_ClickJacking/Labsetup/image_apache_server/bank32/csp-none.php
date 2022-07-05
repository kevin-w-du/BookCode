<?php
 $csp= "Content-Security-Policy: frame-ancestors 'none'";
 header("$csp");
 echo "<h3>".$csp."</h3>";
?>
