<!DOCTYPE html>
<html>
<head><title>Search Results</title></head>
<body>
<h1>Search Results</h1>
<?php
 // **VULNERABLE SINK**: Directly echoing GET parameter without sanitization
 if (isset($_GET['query'])) {
 $query = $_GET['query']; // Source
 echo "<p>You searched for: ". $query. "</p>";
 // In a real app, search results would follow
 } else {
 echo "<p>Enter a search term.</p>";
 }
?>
<form method="GET">
<input type="text" name="query">
<input type="submit" value="Search">
</form>
</body>
</html>
