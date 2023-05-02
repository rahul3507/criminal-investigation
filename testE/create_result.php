<?php
	$f0 = $_GET["f0"];
	$f1 = $_GET["f1"];

	$total = $f0 +$f0*.5 + $f1;
    
    echo "<p id='s'>$total</p>";
?>