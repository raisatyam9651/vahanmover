<?php
$current_page = 'blog.php';
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- SEO Meta Tags -->
    <title>Expert Vehicle Shifting Guides & Resources | Vahan Mover Blog</title>
    <meta name="description"
        content="Read professional guides, tips, and step-by-step checklists for transporting cars and bikes across India. RTO rules, railways parcel guidelines, and packing guides.">
    <meta name="keywords"
        content="vehicle shifting guides, bike transport blog, car shifting guide, railway parcel guidelines, rto rules moving state, vehicle relocation checklist">

    <?php include '../includes/header-link.php'; ?>

    <style>
        .blog-header {
            min-height: 45vh;
            display: flex;
            align-items: center;
            padding-top: 100px;
            position: relative;
            background: linear-gradient(to right, #f1f5f9, #e2e8f0);
            overflow: hidden;
        }

        .blog-header::after {
            content: '';
            position: absolute;
            bottom: -50px;
            right: -50px;
            width: 300px;
            height: 300px;
            background: var(--color-primary);
            filter: blur(180px);
            opacity: 0.15;
            border-radius: 50%;
        }

        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            padding: 80px 0 100px;
        }

        .blog-card {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            transition: all 0.3s ease;
            border: 1px solid var(--glass-border);
            padding: 35px;
            overflow: hidden;
            position: relative;
        }

        .blog-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 0;
            background: linear-gradient(to bottom, var(--color-primary), var(--color-secondary));
            transition: height 0.3s ease;
        }

        .blog-card:hover::before {
            height: 100%;
        }

        .blog-card:hover {
            transform: translateY(-8px);
            border-color: rgba(6, 182, 212, 0.4);
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 15px 35px rgba(15, 23, 42, 0.08);
        }

        .blog-icon-box {
            width: 60px;
            height: 60px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 25px;
            font-size: 1.5rem;
            
        }

        .blog-category {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--color-accent);
            font-weight: 700;
            margin-bottom: 12px;
        }

        .blog-title {
            font-size: 1.4rem;
            font-weight: 700;
            line-height: 1.3;
            margin-bottom: 15px;
            color: var(--color-text-white);
        }

        .blog-excerpt {
            color: var(--color-text-dim);
            line-height: 1.6;
            font-size: 0.95rem;
            margin-bottom: 25px;
            flex-grow: 1;
        }

        .read-more-btn {
            color: var(--color-primary);
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
            font-size: 0.95rem;
        }

        .blog-card:hover .read-more-btn {
            color: var(--color-accent);
            gap: 12px;
        }

        @media (max-width: 768px) {
            .blog-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

    <!-- Navigation -->
    <?php include '../includes/navbar.php'; ?>

    <!-- Header -->
    <header class="blog-header">
        <!-- background blur glow -->
        <div style="position: absolute; top: 10%; left: -10%; width: 400px; height: 400px; background: var(--color-secondary); filter: blur(150px); opacity: 0.15; border-radius: 50%;"></div>
        
        <div class="container" style="position: relative; z-index: 2;">
            <div style="display: inline-block; padding: 8px 16px; background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 30px; margin-bottom: 20px; color: var(--color-primary); font-weight: 600; font-size: 0.9rem;">
                <i class="fa-solid fa-book-open"></i> Shifting Knowledge Hub
            </div>
            <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 15px; ">Guides & <span style="background: linear-gradient(to right, var(--color-primary), var(--color-secondary)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">Resources</span></h1>
            <p style="color: var(--color-text-dim); font-size: 1.25rem; max-width: 650px; line-height: 1.6;">
                Everything you need to know about transporting your car or bike across India. Step-by-step guides, safety checklists, and government regulations.
            </p>
        </div>
    </header>

    <!-- Blog Listing Section -->
    <main class="container">
        <div class="blog-grid">
            
            <!-- Article 1 -->
            <article class="glass-card blog-card">
                <div>
                    <div class="blog-icon-box" style="background: linear-gradient(135deg, var(--color-primary), var(--color-secondary));">
                        <i class="fa-solid fa-train"></i>
                    </div>
                    <div class="blog-category">Railways</div>
                    <h2 class="blog-title">Indian Railways Bike Transport: The Ultimate Guide (Luggage vs Parcel)</h2>
                    <p class="blog-excerpt">
                        Learn how to book and ship your two-wheeler via Indian Railways. Discover the step-by-step difference between Luggage booking and Parcel booking, necessary documents, platform procedures, packing checklist, and fuel rules.
                    </p>
                </div>
                <a href="blog/how-to-transport-bike-by-indian-railways" class="read-more-btn">Read Full Article <i class="fa-solid fa-arrow-right-long"></i></a>
            </article>

            <!-- Article 2 -->
            <article class="glass-card blog-card">
                <div>
                    <div class="blog-icon-box" style="background: linear-gradient(135deg, var(--color-accent), #10b981);">
                        <i class="fa-solid fa-car"></i>
                    </div>
                    <div class="blog-category">Car Shifting</div>
                    <h2 class="blog-title">Complete Car Shifting Guide: Safe Vehicle Relocation across India</h2>
                    <p class="blog-excerpt">
                        Planning to shift your car to another state? Read our expert comparison between open car carriers and closed containers, learn how to choose verified transporters, calculate actual transport costs, and get a vehicle preparation checklist.
                    </p>
                </div>
                <a href="blog/complete-guide-to-car-transportation-services-in-india" class="read-more-btn">Read Full Article <i class="fa-solid fa-arrow-right-long"></i></a>
            </article>

            <!-- Article 3 -->
            <article class="glass-card blog-card">
                <div>
                    <div class="blog-icon-box" style="background: linear-gradient(135deg, #8b5cf6, #d946ef);">
                        <i class="fa-solid fa-building-columns"></i>
                    </div>
                    <div class="blog-category">RTO Regulations</div>
                    <h2 class="blog-title">Understanding RTO Rules for Moving Vehicles to Another State</h2>
                    <p class="blog-excerpt">
                        Moving your vehicle permanently across state lines? Understand the RTO NOC procurement process (Forms 27 and 28), new state road tax payment procedures, claiming refund of lifetime road tax from parent RTO, and state deadlines.
                    </p>
                </div>
                <a href="blog/rto-rules-for-moving-vehicle-to-another-state" class="read-more-btn">Read Full Article <i class="fa-solid fa-arrow-right-long"></i></a>
            </article>

            <!-- Article 4 -->
            <article class="glass-card blog-card">
                <div>
                    <div class="blog-icon-box" style="background: linear-gradient(135deg, #f59e0b, #ef4444);">
                        <i class="fa-solid fa-toolbox"></i>
                    </div>
                    <div class="blog-category">Preparation</div>
                    <h2 class="blog-title">How to Prepare Your Two-Wheeler for Shifting: 6 Vital Steps</h2>
                    <p class="blog-excerpt">
                        Ensure your motorcycle or scooter reaches its destination scratch-free. Follow these hands-on steps for cleaning, fuel draining rules, side-mirror removal, accessory checks, key handovers, and documentation copies.
                    </p>
                </div>
                <a href="blog/how-to-prepare-your-two-wheeler-for-safe-shipping" class="read-more-btn">Read Full Article <i class="fa-solid fa-arrow-right-long"></i></a>
            </article>

            <!-- Article 5 -->
            <article class="glass-card blog-card">
                <div>
                    <div class="blog-icon-box" style="background: linear-gradient(135deg, #06b6d4, #3b82f6);">
                        <i class="fa-solid fa-shield-halved"></i>
                    </div>
                    <div class="blog-category">Insurance</div>
                    <h2 class="blog-title">Vehicle Transit Insurance Explained: Cover Types, Claims & Tips</h2>
                    <p class="blog-excerpt">
                        Protect your valuable vehicle against any transit risks. Understand the vital difference between third-party and comprehensive transit insurance, how vehicle valuation works, claim documentation, and filing procedures.
                    </p>
                </div>
                <a href="blog/vehicle-transit-insurance-guide-types-claims-and-importance" class="read-more-btn">Read Full Article <i class="fa-solid fa-arrow-right-long"></i></a>
            </article>

            <!-- Article 6 -->
            <article class="glass-card blog-card">
                <div>
                    <div class="blog-icon-box" style="background: linear-gradient(135deg, #14b8a6, #10b981);">
                        <i class="fa-solid fa-clipboard-list"></i>
                    </div>
                    <div class="blog-category">Relocation</div>
                    <h2 class="blog-title">Ultimate Shifting Checklist: Combining Home & Vehicle Relocation</h2>
                    <p class="blog-excerpt">
                        Managing both household shifting and vehicle relocation simultaneously can be overwhelming. Follow our structured timeline checklist (3 weeks out, 1 week out, moving day, delivery day) to coordinate a seamless relocation.
                    </p>
                </div>
                <a href="blog/moving-checklist-for-shifting-household-and-vehicles" class="read-more-btn">Read Full Article <i class="fa-solid fa-arrow-right-long"></i></a>
            </article>

        </div>
    </main>

    <!-- Footer -->
    <?php include '../includes/footer.php'; ?>

</body>

</html>
