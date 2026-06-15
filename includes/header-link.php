<?php
$protocol = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') ? "https://" : "http://";
$host = $_SERVER['HTTP_HOST'];
$script_dir = dirname($_SERVER['SCRIPT_NAME']);
$script_dir = str_replace('\\', '/', $script_dir);
if ($script_dir === '/blog' || substr($script_dir, -5) === '/blog') {
    $script_dir = dirname($script_dir);
}
$script_dir = str_replace('\\', '/', $script_dir);
$base_path = ($script_dir == '/') ? '/' : $script_dir . '/';
$base_url = $protocol . $host . $base_path;
?>
<base href="<?php echo $base_url; ?>">
<link rel="stylesheet" href="style.css">
<!-- Font Awesome for Icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- SEO Meta Tags -->
<!-- Google AdSense Tag -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4910239000711715" crossorigin="anonymous"></script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8KN112RYKL"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    gtag('js', new Date());

    gtag('config', 'G-8KN112RYKL');
</script>
<meta name="google-site-verification" content="xjeLREcMez2kegDf2QsMgGLabvzbJVgrIwn4XZR5R-c" />
<link rel="canonical" href="<?php echo 'https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI']; ?>" />
<?php
$current_page = basename($_SERVER['PHP_SELF']);
if ((strpos($current_page, 'bike-transport-') === 0 && $current_page != 'bike-transport-service.php') || 
    (strpos($current_page, 'car-transport-') === 0 && $current_page != 'car-transport-service.php')) {
    echo '<meta name="robots" content="noindex, follow" />';
} else {
    echo '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />';
}
?>
<meta name="author" content="Vahan Mover" />
<meta name="publisher" content="Vahan Mover Logistics" />
<script src="https://analytics.ahrefs.com/analytics.js" data-key="/oyw9ViZT9Ucyt/t72iARQ" async></script>