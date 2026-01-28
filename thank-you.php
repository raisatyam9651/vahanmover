<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You | Vahan Mover</title>
    <meta name="description" content="Thank you for contacting Vahan Mover. We have received your query.">

    <?php include 'includes/header-link.php'; ?>
</head>

<body>

    <!-- Navigation -->
    <?php include 'includes/navbar.php'; ?>

    <!-- Thank You Section -->
    <section
        style="min-height: 80vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 100px 20px;">
        <div class="container">
            <div class="glass-card" style="padding: 60px; max-width: 600px; margin: 0 auto;">
                <div
                    style="width: 80px; height: 80px; background: rgba(16, 185, 129, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 30px;">
                    <i class="fa-solid fa-check" style="font-size: 2.5rem; color: #10b981;"></i>
                </div>

                <h1 style="font-size: 2.5rem; margin-bottom: 20px; font-weight: 700;">Thank You!</h1>

                <p style="color: var(--color-text-dim); font-size: 1.2rem; line-height: 1.6; margin-bottom: 30px;">
                    Your quote request has been received successfully. Our team will review your details and get back to
                    you within 24 hours.
                </p>

                <a href="index.php" class="btn btn-primary" style="display: inline-block; text-decoration: none;">
                    <i class="fa-solid fa-house"></i> Back to Home
                </a>
            </div>
        </div>
    </section>

    <?php include 'includes/footer.php'; ?>

</body>

</html>