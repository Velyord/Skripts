<?php 
date_default_timezone_set('Europe/Sofia');
	// Функция за извличане на всички снимки по местоположение
	function scanAllDir($dir) {
		$result = [];
		foreach(scandir($dir) as $filename) {
		    if ($filename[0] === '.') continue;
		    $filePath = $dir . '\\' . $filename;
		    if (is_dir($filePath)) {
		    	foreach (scanAllDir($filePath) as $childFilename) {
		        	$result[] = $filename . '\\' . $childFilename;
  				}
			} else {
  				$result[] = $filename;
			}
		}
		return $result;
	}
	$where = "C:\Users\Georgi\Desktop\Work\Pic-Matanov";
	$contents2 = scanAllDir($where);
	$file = fopen("fortable3.csv","w");
	
	$arrbig = array(); // за визуализация на екрана
	
	foreach ($contents2 as $value) {
		$arr = array();
		$arr["Path"] = $value;
		
		// Извличане на отделна информация за всяка снимка
		$exif = exif_read_data($where."\\".$value, 0, true);
		foreach ($exif as $key => $section) {
			foreach ($section as $name => $val) {
				echo "$key.$name: $val<br />\n"; // Визуализация на всички графи на информация за всяка снимка
				if(in_array($name, array("Path", "FileName", "Height", "Width", "Model", "DateTime", "FileDateTime"))) {
					$arr[$name]=$val;
				}			
			}
		}
		// вкарват се във втори масив, за да може липсващите стойности да се отбележат за базата данни по-късно
		$arr2 = array (
			"Path"	=> $arr["Path"],
			"FileName" => $arr["FileName"],
			"Height" => $arr["Height"],
			"Width" => $arr["Width"],
			"Model" => $arr["Model"],
			"DateTime" => $arr["DateTime"],
			"FileDateTime" => date('Y:m:d H:i:s',$arr["FileDateTime"])
		);
		$arrbig[] = $arr2;
		
		$txt = implode('";"', $arr2);
		fwrite($file, "\"$txt\"\n");
	}
	// за визуализиране на екрана
	echo "<pre>";
	print_r($arrbig);
	echo "/<pre>";
	
	fclose($file);
?>
