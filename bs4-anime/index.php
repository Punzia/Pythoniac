<?php 
        //2>&1 <- adding output to exec
        ob_start();
        passthru('python /var/www/site/anime/anime.py');
        $output = ob_get_clean(); 

?>
<html>

<head>
    <title>Anime BS4</title>
	<link rel="icon" href="favicon.ico" type="image/x-icon"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://punzia.tech/libs/jquery/jquery-3.5.1.min.js"></script>
    <script src="https://punzia.tech/libs/semantic/semantic.min.js"></script>
    <link rel="stylesheet" href="https://punzia.tech/libs/semantic/semantic.min.css">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1 class="center_heading"> Current Airing Anime checked /w BeautifulSoup4</h1>
    <div class="container">
        <?PHP
        echo $output;
        ?>
    </div>
    <script>
    $(".cd-timeline-content-buttons").remove();
    </script>

</body>

</html>