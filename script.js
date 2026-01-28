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

    // Form submission is now handled by submit.php
    // We only keep basic UI enhancements if needed, or remove the listener entirely.
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        // Optional: Client-side validation could go here
        console.log('Form ready for PHP submission');
    }
});
