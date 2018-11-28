<html>
 <head>
  <title>AWS Test</title>
 </head>
 <body>
 <?php
	#require_once("utils.php");
        echo '<p>Hello World</p>';
	echo $_GET['uname'];
        print_r($requests);
	print_r($user);
        $keys = array_keys($_COOKIE);
        #print_r ($keys);
        echo '<br>';
        $values = array_values($_COOKIE);
        #print_r ($values);
        $c = array_combine($keys,$values);
        #print_r($c);
        echo '<br>';
        echo 'Abhash Jain!'
 ?>
 </body>
</html>
