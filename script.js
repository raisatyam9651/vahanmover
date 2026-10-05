document.addEventListener('DOMContentLoaded', () => {
    // Console log for verification
    console.log('Shifter - Pan-India Vehicle Transport initialized');

    // Future interactive elements

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Form input focus effects
    document.querySelectorAll('input, select, textarea').forEach(input => {
        input.addEventListener('focus', function () {
            this.style.borderColor = 'var(--color-primary)';
            this.style.boxShadow = '0 0 0 3px rgba(6, 182, 212, 0.1)';
        });
        input.addEventListener('blur', function () {
            this.style.borderColor = 'rgba(255,255,255,0.1)';
            this.style.boxShadow = 'none';
        });
    });

    // Universal Form Submission Handler for Frappe CRM & Google Sheets
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            // Check if form already has action and name attributes properly set
            const hasNames = contactForm.querySelector('[name="phone"], [name="email"]');
            if (contactForm.getAttribute('action') === 'submit.php' && hasNames) {
                // Let native browser POST to submit.php proceed
                return;
            }

            e.preventDefault();

            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.innerHTML : '';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting...';
            }

            // Extract values smartly by name or position/placeholder
            const fullName = contactForm.querySelector('[name="full_name"]')?.value ||
                contactForm.querySelector('input[placeholder*="name" i]')?.value || '';

            const phone = contactForm.querySelector('[name="phone"]')?.value ||
                contactForm.querySelector('input[type="tel"]')?.value ||
                contactForm.querySelector('input[placeholder*="phone" i]')?.value || '';

            const email = contactForm.querySelector('[name="email"]')?.value ||
                contactForm.querySelector('input[type="email"]')?.value || '';

            const pickupCity = contactForm.querySelector('[name="pickup_city"]')?.value ||
                contactForm.querySelector('input[placeholder*="From" i]')?.value ||
                contactForm.querySelector('input[placeholder*="Pickup" i]')?.value || '';

            const dropCity = contactForm.querySelector('[name="drop_city"]')?.value ||
                contactForm.querySelector('input[placeholder*="To" i]')?.value ||
                contactForm.querySelector('input[placeholder*="Drop" i]')?.value || '';

            const vehicleType = contactForm.querySelector('[name="vehicle_type"]')?.value ||
                contactForm.querySelector('select')?.value || '';

            const preferredDate = contactForm.querySelector('[name="preferred_date"]')?.value ||
                contactForm.querySelector('input[type="date"]')?.value || '';

            const message = contactForm.querySelector('[name="message"]')?.value ||
                contactForm.querySelector('textarea')?.value || '';

            const formData = new FormData();
            formData.append('full_name', fullName);
            formData.append('phone', phone);
            formData.append('email', email);
            formData.append('pickup_city', pickupCity);
            formData.append('drop_city', dropCity);
            formData.append('vehicle_type', vehicleType);
            formData.append('preferred_date', preferredDate);
            formData.append('message', message);
            formData.append('submission_id', 'SUB-' + Date.now());
            formData.append('ajax', '1');

            fetch('submit.php', {
                method: 'POST',
                body: formData
            })
            .then(res => res.json())
            .then(data => {
                window.location.href = 'thank-you.php';
            })
            .catch(err => {
                console.warn('Submission completed or redirecting...', err);
                window.location.href = 'thank-you.php';
            });
        });
    }
});
