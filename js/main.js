document.addEventListener('DOMContentLoaded', () => {
    // Load Header and Footer dynamically
    Promise.all([
        fetch('header.html').then(response => response.text()),
        fetch('footer.html').then(response => response.text())
    ]).then(([headerHtml, footerHtml]) => {
        const headerPlaceholder = document.getElementById('common-header');
        const footerPlaceholder = document.getElementById('common-footer');
        
        if (headerPlaceholder) headerPlaceholder.innerHTML = headerHtml;
        if (footerPlaceholder) footerPlaceholder.innerHTML = footerHtml;

        // Set active nav link based on current URL
        const currentPath = window.location.pathname.split('/').pop() || 'index.html';
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            const linkPath = link.getAttribute('href');
            if (linkPath === currentPath) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    }).catch(error => console.error("Error loading header/footer:", error));

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.navbar');
        if (nav) {
            if (window.scrollY > 50) {
                nav.classList.add('shadow-md', 'bg-opacity-90');
                nav.classList.remove('shadow-sm');
            } else {
                nav.classList.add('shadow-sm');
                nav.classList.remove('shadow-md', 'bg-opacity-90');
            }
        }
    });

    // Initialize Hero Swiper
    if (typeof Swiper !== 'undefined') {
        new Swiper(".heroSwiper", {
            loop: true,
            speed: 1000,
            autoplay: {
                delay: 4000,
                disableOnInteraction: false
            },
            effect: "fade",
            fadeEffect: {
                crossFade: true
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev"
            }
        });
    }

    // Initialize Testimonial Swiper
    if (typeof Swiper !== 'undefined') {
        const testSwiper = document.querySelector('.testimonialSwiper');
        if (testSwiper) {
            new Swiper(".testimonialSwiper", {
                loop: true,
                speed: 800,
                autoplay: {
                    delay: 3000,
                    disableOnInteraction: false
                },
                pagination: {
                    el: ".swiper-pagination",
                    clickable: true
                },
                spaceBetween: 24,
                breakpoints: {
                    320: { slidesPerView: 1 },
                    768: { slidesPerView: 2 },
                    1024: { slidesPerView: 3 }
                }
            });
        }
    }

    // Initialize AOS Animation
    if (typeof AOS !== 'undefined') {
        AOS.init({
            once: true,
            offset: 100
        });
    }
});
