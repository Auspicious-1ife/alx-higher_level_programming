<!DOCTYPE html>
<html>
<head>
    <title>Change Header Color on Click</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

<div id="red_header">Click me to change header color</div>
<header>This is the header</header>

<script>
    $(document).ready(function(){
        $('#red_header').click(function(){
            $('header').css('color', '#FF0000');
        });
    });
</script>

</body>
</html>
