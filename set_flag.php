php
<?php
setcookie("flag", "flag{r3fl3ct3d_xss_pwn3d}", time()+3600, "/");
echo "Flag cookie set. <a href='search.php'>Go to search</a>";
?>
