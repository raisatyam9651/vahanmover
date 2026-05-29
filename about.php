<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | Vahan Mover</title>
    <meta name="description"
        content="Learn more about Vahan Mover, India's premier platform for connecting you with verified, professional vehicle relocation services.">

    <?php include 'includes/header-link.php'; ?>
    <style>
        .terms-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            margin-top: -80px;
            position: relative;
            z-index: 10;
        }
    </style>
</head>

<body>

    <!-- Navigation -->
    <?php include 'includes/navbar.php'; ?>

    <!-- Hero Section -->
    <section class="hero"
        style="min-height: 50vh; display: flex; align-items: center; padding-top: 100px; position: relative; background: linear-gradient(to right, #0f172a, #1e293b);">
        <div class="container">
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 20px; color: white;">About <span
                    style="color: var(--color-primary);">Us</span></h1>
            <p style="color: var(--color-text-dim); font-size: 1.2rem; max-width: 600px;">Simplifying vehicle transportation across India with trust, transparency, and technology.</p>
        </div>
    </section>

    <!-- Content Section -->
    <section style="padding: 0 0 80px;">
        <div class="container">
            <div class="terms-card">

                <div style="margin-bottom: 30px;">
                    <h3 style="color: var(--color-primary); margin-bottom: 15px; font-size: 1.3rem;">Who We Are</h3>
                    <p style="color: var(--color-text-dim); line-height: 1.8;">Vahan Mover is India's leading platform dedicated exclusively to vehicle transportation. We understand that your car or bike is more than just a vehicle; it's a valuable asset and often holds sentimental value. That's why we've created a seamless, reliable bridge between individuals looking to shift their vehicles and verified, professional packers and movers across the country.</p>
                </div>

                <div style="margin-bottom: 30px;">
                    <h3 style="color: var(--color-primary); margin-bottom: 15px; font-size: 1.3rem;">Our Mission</h3>
                    <p style="color: var(--color-text-dim); line-height: 1.8;">Our mission is simple: to eliminate the stress, uncertainty, and hidden costs traditionally associated with vehicle relocation. We strive to provide a transparent ecosystem where customers can easily request quotes, compare services, and trust that their vehicles are in safe hands.</p>
                </div>

                <div style="margin-bottom: 30px;">
                    <h3 style="color: var(--color-primary); margin-bottom: 15px; font-size: 1.3rem;">How We Work</h3>
                    <p style="color: var(--color-text-dim); line-height: 1.8;">We act as a premium aggregator and lead generation platform. When you submit a request on Vahan Mover, our system instantly matches your specific route and vehicle type with our network of pre-vetted logistics partners. These partners then provide you with competitive, customized quotes. You deal directly with the service provider, ensuring clear communication and the best possible price without middleman markups.</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 40px; margin-bottom: 30px;">
                    <div style="background: rgba(6, 182, 212, 0.05); padding: 20px; border-radius: 10px; text-align: center; border: 1px solid rgba(6, 182, 212, 0.2);">
                        <h4 style="font-size: 2rem; color: var(--color-accent); margin-bottom: 5px;">15,000+</h4>
                        <p style="color: var(--color-text-dim);">Vehicles Shifted</p>
                    </div>
                    <div style="background: rgba(6, 182, 212, 0.05); padding: 20px; border-radius: 10px; text-align: center; border: 1px solid rgba(6, 182, 212, 0.2);">
                        <h4 style="font-size: 2rem; color: var(--color-primary); margin-bottom: 5px;">450+</h4>
                        <p style="color: var(--color-text-dim);">Cities Covered</p>
                    </div>
                    <div style="background: rgba(6, 182, 212, 0.05); padding: 20px; border-radius: 10px; text-align: center; border: 1px solid rgba(6, 182, 212, 0.2);">
                        <h4 style="font-size: 2rem; color: #10b981; margin-bottom: 5px;">100%</h4>
                        <p style="color: var(--color-text-dim);">Verified Partners</p>
                    </div>
                </div>

                <div style="margin-top: 50px; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.1);">
                    <p style="color: var(--color-text-dim);">Ready to shift your vehicle? <a href="contact.php" style="color: var(--color-primary); text-decoration: none;">Get a free quote today!</a></p>
                </div>

            </div>
        </div>
    </section>

    <?php include 'includes/footer.php'; ?>

</body>

</html>
