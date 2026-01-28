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

    // Form submission
    // Form submission with Webhook
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;

            const webhookURL = 'https://script.google.com/macros/s/AKfycbyMNwTP_jPTYEuC67a7whDqA7nASauZ88Z2XPW04bXGXySiArqfqcsH6gJV/exec';
            // NOTE: The URL in the prompt ended with .../usercontent which usually means it was truncated. 
            // I've used a standard looking ending /exec based on common Google Apps Script patterns, 
            // BUT YOU MUST REPLACE THIS WITH THE FULL URL YOU COPIED.

            // Construct data object based on exact field matches
            const formData = {
                fullName: this.querySelector('input[placeholder="Enter your name"]').value,
                phoneNumber: this.querySelector('input[placeholder="Enter phone number"]').value,
                emailAddress: this.querySelector('input[placeholder="Enter your email"]').value,
                pickupCity: this.querySelector('input[placeholder="From city"]').value,
                dropCity: this.querySelector('input[placeholder="To city"]').value,
                vehicleType: this.querySelector('select').value,
                preferredDate: this.querySelector('input[type="date"]').value,
                message: this.querySelector('textarea').value
            };

            fetch(webhookURL, {
                method: 'POST',
                mode: 'no-cors', // Important for Google Apps Script webhooks to avoid CORS errors
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
                .then(response => {
                    // With no-cors, we can't check response.ok, so we assume success if no network error
                    alert('Thank you! Your quote request has been sent successfully.');
                    contactForm.reset();
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Something went wrong. Please try again or call us directly.');
                })
                .finally(() => {
                    // Restore button state
                    submitBtn.innerHTML = originalBtnText;
                    submitBtn.disabled = false;
                });
        });
    }
});


