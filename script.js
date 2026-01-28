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
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Thank you for your inquiry! Our team will contact you within 24 hours.');
            this.reset();
        });
    }
});


