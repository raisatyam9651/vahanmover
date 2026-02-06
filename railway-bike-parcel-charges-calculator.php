<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- SEO Meta Tags -->
    <title>Railway Bike Parcel Charges Calculator | Indian Railways Bike Transport Rate</title>
    <meta name="description"
        content="Calculate approximate railway bike parcel charges for 2024. Get instant estimates for bike transport by train including packing and insurance cost.">
    <meta name="keywords"
        content="railway bike parcel charges calculator, bike transport by train cost, indian railways bike shifting rates, railway parcel calculator, two wheeler train transport cost">

    <?php include 'includes/header-link.php'; ?>

    <style>
        .calculator-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            color: var(--color-text-white);
            font-weight: 500;
        }

        .form-control {
            width: 100%;
            padding: 14px 18px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            color: var(--color-text-white);
            font-size: 1rem;
            transition: all 0.3s;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--color-primary);
            box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.2);
        }

        .form-control option {
            background: var(--color-bg-dark);
        }

        .result-box {
            background: linear-gradient(145deg, rgba(6, 182, 212, 0.1), rgba(59, 130, 246, 0.1));
            border: 1px solid var(--color-primary);
            border-radius: 16px;
            padding: 25px;
            margin-top: 30px;
            display: none;
            animation: fadeIn 0.5s ease-out;
        }

        .result-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 12px;
            padding-bottom: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--color-text-dim);
        }

        .result-row:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }

        .total-row {
            margin-top: 15px;
            padding-top: 15px;
            border-top: 2px dashed rgba(255, 255, 255, 0.2);
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--color-accent);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>

<body>

    <!-- Navigation -->
    <?php include 'includes/navbar.php'; ?>

    <!-- Hero Section -->
    <section class="hero"
        style="min-height: 90vh; display: flex; align-items: center; padding-top: 100px; position: relative; overflow: hidden;">
        <!-- Background Elements -->
        <div
            style="position: absolute; top: 10%; left: -5%; width: 300px; height: 300px; background: var(--color-primary); filter: blur(150px); opacity: 0.2;">
        </div>
        <div
            style="position: absolute; bottom: 10%; right: -5%; width: 400px; height: 400px; background: var(--color-secondary); filter: blur(150px); opacity: 0.2;">
        </div>

        <div class="container">
            <div class="row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center;">

                <!-- Content -->
                <div>
                    <div
                        style="display: inline-block; padding: 8px 16px; background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 30px; margin-bottom: 20px; color: var(--color-primary); font-weight: 600; font-size: 0.9rem;">
                        <i class="fa-solid fa-calculator"></i> Free Cost Estimator
                    </div>
                    <h1 style="font-size: 3.2rem; line-height: 1.1; margin-bottom: 24px; font-weight: 800;">
                        Railway Bike Parcel <br>
                        <span
                            style="background: linear-gradient(to right, var(--color-primary), var(--color-secondary)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;">Charges
                            Calculator</span>
                    </h1>
                    <p style="font-size: 1.1rem; color: var(--color-text-dim); margin-bottom: 40px; line-height: 1.7;">
                        Planning to transport your bike by Indian Railways? Use our advanced calculator to get an
                        instant estimate of parcel charges, packing costs, and insurance fees. Be prepared before you
                        visit the station.
                    </p>

                    <div class="cta-container" style="display: flex; gap: 20px;">
                        <a href="#calculator" class="btn btn-primary"><i class="fa-solid fa-calculator"></i> Calculate
                            Now</a>
                        <a href="tel:+916388717912" class="btn btn-secondary"><i class="fa-solid fa-phone"></i> Talk to
                            Expert</a>
                    </div>
                </div>

                <!-- Calculator -->
                <div id="calculator">
                    <div class="calculator-card floating">
                        <h3 style="margin-bottom: 25px; font-size: 1.5rem; text-align: center;">Estimate Your Cost</h3>

                        <form id="railwayCostForm" onsubmit="calculateCost(event)">
                            <div class="form-group">
                                <label class="form-label">Bike Engine Capacity (CC)</label>
                                <select class="form-control" id="bikeCC" required>
                                    <option value="" disabled selected>Select Engine CC</option>
                                    <option value="100-150">100cc - 150cc (e.g., Splendor, Shine)</option>
                                    <option value="150-250">150cc - 250cc (e.g., Pulsar, Apache)</option>
                                    <option value="250-350">250cc - 350cc (e.g., Bullet, Classic)</option>
                                    <option value="350+">Above 350cc (Superbikes)</option>
                                </select>
                            </div>

                            <div class="form-group">
                                <label class="form-label">Total Distance (km)</label>
                                <input type="number" class="form-control" id="distance" placeholder="Ex: 1200" min="10"
                                    required>
                            </div>

                            <div class="form-group">
                                <label class="form-label">Declared Value of Bike (₹)</label>
                                <input type="number" class="form-control" id="declaredValue" placeholder="Ex: 50000"
                                    min="1000" required>
                                <small style="color: var(--color-text-dim); font-size: 0.8rem;">(Used for insurance
                                    calculation)</small>
                            </div>

                            <button type="submit" class="btn btn-primary" style="width: 100%;">Calculate
                                Charges</button>
                        </form>

                        <!-- Result Display -->
                        <div id="resultBox" class="result-box">
                            <h4
                                style="color: var(--color-primary); margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px;">
                                Cost Estimate Breakdown</h4>

                            <div class="result-row">
                                <span>Freight Charges (Approx)</span>
                                <span id="resFreight" style="font-weight: 600;">₹0</span>
                            </div>
                            <div class="result-row">
                                <span>Packing Charges</span>
                                <span id="resPacking" style="font-weight: 600;">₹0</span>
                            </div>
                            <div class="result-row">
                                <span>Insurance & Handling</span>
                                <span id="resInsurance" style="font-weight: 600;">₹0</span>
                            </div>

                            <div class="result-row total-row">
                                <span>Total Estimated Cost</span>
                                <span id="resTotal">₹0</span>
                            </div>
                            <p
                                style="margin-top: 15px; font-size: 0.8rem; color: var(--color-text-dim); text-align: center;">
                                *Note: This is an approximate estimate. Actual charges by Indian Railways may vary
                                slightly based on train type and station rules.
                            </p>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Content Sections -->
    <section style="padding: 80px 0; background: rgba(255,255,255,0.02);">
        <div class="container">
            <div style="max-width: 900px; margin: 0 auto;">

                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">Railway Bike Parcel: <span
                        style="color: var(--color-primary);">Important Information</span></h2>
                <p style="color: var(--color-text-dim); margin-bottom: 40px; font-size: 1.1rem; line-height: 1.8;">
                    Understanding the cost structure and rules for transporting a bike via train is crucial for a smooth
                    experience. Indian Railways offers reliable services, but charges depend heavily on the weight of
                    your vehicle and the distance to be covered.
                </p>

                <div style="display: grid; gap: 30px;">

                    <div class="glass-card" style="padding: 30px;">
                        <h3 style="margin-bottom: 15px; color: var(--color-accent); font-size: 1.4rem;">1. Luggage vs.
                            Parcel Booking</h3>
                        <p style="color: var(--color-text-dim); line-height: 1.6;">
                            <strong>Luggage Booking:</strong> You travel on the same train, and the bike is carried in
                            the luggage van not too far from you. You must have a confirmed ticket.<br><br>
                            <strong>Parcel Booking:</strong> You book the bike as a parcel, and it is sent separately.
                            You don't need to travel on the same train. This is often used when sending bikes to friends
                            or family, or when you are traveling by flight.
                        </p>
                    </div>

                    <div class="glass-card" style="padding: 30px;">
                        <h3 style="margin-bottom: 15px; color: var(--color-secondary); font-size: 1.4rem;">2. Mandatory
                            Documents</h3>
                        <ul
                            style="color: var(--color-text-dim); line-height: 1.8; list-style-type: none; padding-left: 0;">
                            <li><i class="fa-solid fa-check"
                                    style="color: var(--color-primary); margin-right: 10px;"></i> Original Registration
                                Certificate (RC) & Xerox Copy</li>
                            <li><i class="fa-solid fa-check"
                                    style="color: var(--color-primary); margin-right: 10px;"></i> Valid Insurance Policy
                                Copy</li>
                            <li><i class="fa-solid fa-check"
                                    style="color: var(--color-primary); margin-right: 10px;"></i> Government ID Proof of
                                the Sender (Aadhar/DL)</li>
                        </ul>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq" style="padding: 80px 0;">
        <div class="container">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-size: 3rem; margin-bottom: 15px; font-weight: 700;">Frequently Asked <span
                        style="color: var(--color-primary);">Questions</span></h2>
            </div>

            <div class="faq-grid">
                <div class="glass-card faq-card">
                    <h4 style="margin-bottom: 10px;">Is packing mandatory for railway bike transport?</h4>
                    <p style="color: var(--color-text-dim); line-height: 1.6;">Yes, proper packing of the headlight,
                        fuel tank, and mirrors is mandatory to avoid damage and fire hazards. Railways stations have
                        packing agents, but professional packing is recommended.</p>
                </div>
                <div class="glass-card faq-card">
                    <h4 style="margin-bottom: 10px;">Do I need to empty the fuel tank?</h4>
                    <p style="color: var(--color-text-dim); line-height: 1.6;">Absolutely. As per railway safety rules,
                        the fuel tank must be completely dry. If fuel is found, you may be fined heavily (approx ₹1000 -
                        ₹5000).</p>
                </div>
                <div class="glass-card faq-card">
                    <h4 style="margin-bottom: 10px;">Can I track my bike parcel?</h4>
                    <p style="color: var(--color-text-dim); line-height: 1.6;">Yes, if you book it as a parcel, you will
                        receive a Railway Receipt (RR) number which can be used to track the status on the Indian
                        Railways parcel website.</p>
                </div>
                <div class="glass-card faq-card">
                    <h4 style="margin-bottom: 10px;">Whats cheaper: Train or Private Transporters?</h4>
                    <p style="color: var(--color-text-dim); line-height: 1.6;">Trains are generally cheaper for long
                        distances but require significant effort (booking, loading, unloading). Private transporters
                        offer door-to-door convenience at a slightly higher premium but save time and hassle.</p>
                </div>
            </div>
        </div>
    </section>

    <?php include 'includes/footer.php'; ?>

    <!-- Calculator Script -->
    <script>
        function calculateCost(e) {
            e.preventDefault();

            // Get inputs
            const cc = document.getElementById('bikeCC').value;
            const dist = parseFloat(document.getElementById('distance').value);
            const val = parseFloat(document.getElementById('declaredValue').value);

            if (!cc || !dist || !val) {
                alert("Please fill all fields");
                return;
            }

            // --- Calculation Logic (Estimates) ---

            // 1. Base Freight Calculation
            let baseRatePerKm = 0;
            if (cc === '100-150') baseRatePerKm = 2.5;
            else if (cc === '150-250') baseRatePerKm = 3.2;
            else if (cc === '250-350') baseRatePerKm = 3.8;
            else baseRatePerKm = 4.5; // 350+

            // Min freight charge logic
            let freight = Math.max(300, (dist * baseRatePerKm) / 10);
            // Note: Railway freight formula is complex, this is a simplified estimation for user guidance (approx ₹2.5 - ₹4.5 per 10km block roughly)
            // Adjusting formula to be more realistic: roughly Rs 400-800 for shorter, Rs 1500-2500 for longer

            // Improved estimate formula:
            // Base + (Rate * Distance)
            let baseFee = 300;
            if (cc == '350+') baseFee = 500;

            // Rate per km varies by distance slabs usually, simplifying to linear for estimate
            // 150cc approx 1.5rs/km average over long haul
            let rateFactor = 1.2;
            if (cc === '150-250') rateFactor = 1.5;
            if (cc === '250-350') rateFactor = 1.8;
            if (cc === '350+') rateFactor = 2.5;

            freight = baseFee + (dist * rateFactor);

            // 2. Packing Cost (Market standard at stations)
            let packing = 350;
            if (cc === '150-250') packing = 500;
            if (cc === '250-350' || cc === '350+') packing = 800;

            // 3. Insurance (1% of declared value is standard railway insurance fee approx)
            let insurance = val * 0.01;
            // Add Handling/Porter charges (approx 200)
            insurance += 200;

            // Total
            let total = freight + packing + insurance;

            // Update UI
            document.getElementById('resFreight').innerText = '₹' + Math.round(freight);
            document.getElementById('resPacking').innerText = '₹' + Math.round(packing);
            document.getElementById('resInsurance').innerText = '₹' + Math.round(insurance);
            document.getElementById('resTotal').innerText = '₹' + Math.round(total);

            // Show result
            document.getElementById('resultBox').style.display = 'block';
        }
    </script>
</body>

</html>