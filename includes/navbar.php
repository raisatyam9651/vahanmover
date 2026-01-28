<?php
$current_page = basename($_SERVER['PHP_SELF']);
?>
    <!-- Navigation -->
    <nav style="position: absolute; width: 100%; top: 0; padding: 20px 0; z-index: 100;">
        <div class="container" style="display: flex; justify-content: space-between; align-items: center;">
            <div class="logo"
                style="font-size: 1.8rem; font-weight: 800; color: var(--color-primary); letter-spacing: -1px;">
                VAHAN MOVER<span style="color: var(--color-text-white);">.</span>
            </div>
            <div class="nav-links" style="display: flex; gap: 30px;">
                <a href="index.php"
                    style="color: <?php echo ($current_page == 'index.php') ? 'var(--color-primary)' : 'var(--color-text-white)'; ?>; text-decoration: none; font-weight: 500;">Home</a>
                <a href="bike-transport-service.php"
                    style="color: <?php echo ($current_page == 'bike-transport-service.php' || strpos($current_page, 'bike-transport-') === 0 && $current_page != 'bike-transport-service.php') ? 'var(--color-primary)' : 'var(--color-text-white)'; ?>; text-decoration: none; font-weight: 500;">Bike Transport</a>
                <a href="car-transport-service.php"
                    style="color: <?php echo ($current_page == 'car-transport-service.php' || strpos($current_page, 'car-transport-') === 0 && $current_page != 'car-transport-service.php') ? 'var(--color-primary)' : 'var(--color-text-white)'; ?>; text-decoration: none; font-weight: 500;">Car Transport</a>
                <a href="contact.php"
                    style="color: <?php echo ($current_page == 'contact.php') ? 'var(--color-primary)' : 'var(--color-text-white)'; ?>; text-decoration: none; font-weight: 500;">Contact</a>
            </div>
            <a href="contact.php" class="btn btn-primary" style="padding: 10px 24px; font-size: 0.9rem;">Get Quote</a>
        </div>
    </nav>
