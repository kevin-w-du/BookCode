<?php
 $xframe = "X-Frame-Options: DENY";
 header($xframe);

 echo "<h3>".$xframe."</h3>"; 
?>
