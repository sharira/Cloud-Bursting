<head>
<title>Delete Table Row with animation</title>
<style>
table
{
	border-collapse: collapse;
	border: 1px solid #0098D3;
}
th 
{
	padding:5px;
	background:#cc0000;
	color:#FFF;
}
td
{
	border: 1px solid #0098D3;
	color:gray;
}
tr:nth-child(even){background-color: #f2f2f2}
.deleteLink
{
	text-decoration:underline;
	color:blue;
}
.deleteLink:hover
{
	cursor:pointer;
	text-decoration:none;
}
tr td a img 
{
	float:left;
}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
function deleteStudent(id) {
	//$.post("delete.php" , {sid:id} , function(data){
	//	$("#" + id).fadeOut('slow' , function(){$(this).remove();if(data)alert(data);});
	//});
	console.log(id);	
	var rc = confirm("Do you really want to delete the reservation?");
	if(rc==true){
		var myurl = "../../../cgi-bin/delete.py?id="+id;
		$.ajax({
			url: myurl,
			type:"POST",
			success: callbackfunc,
			error: errorfunc
		});
	}
    }
function callbackfunc(response){
	console.log("Success!");
	console.log(response);	
}
function errorfunc(response){
	console.log("Error!");
	console.log(response);	
}
	</script>
	</head>
<?php
	$con = new mysqli('localhost' , 'vcl_admin' , 'Admin123~' , 'vcl');
	$query = "SELECT * from aws_reservation where username='" . $_GET['uname'] ."'";
	$result = $con->query($query);
	$numRow = mysqli_num_rows($result);
	if($numRow > 0){
	echo '<center><h1>List of AWS Reservations for '. $_GET['uname'] .'</h1></center>';
	echo '<center><table  >';
	echo '<tr>
		 <th>DNS IP</th>
		 <th>UserName</th>
		 <th>Password</th>
		  <th>Start time</th>
		<th>End Time</th></tr>';
	
	while($row = $result->fetch_assoc())
		echo '<tr id="' . $row['instance_id'] . '">
			 <td>' . $row['dns_ip'] . '</td>
			 <td>' . $row['instance_username'] . '</td>
			 <td>' . $row['password'] . '</td>
			 <td> '. $row["start_time"] . '</td>' . 
			 '<td>' . $row["end_time"] . '</td>' . 
			 '<td ><a class="deleteLink" onclick="deleteStudent(\''.$row['instance_id'].'\')">Delete Reservation</a></td>' .
			 '</tr>';
 
	echo '</table></center>';
	} else {
		echo '<center><H2>'.$_GET['uname'].' doesn\'t have any AWS reservations!</h2></center>';
	}
 ?>
 

 
