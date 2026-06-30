// Mobile Menu Toggle
const hamburger = document.getElementById("hamburger");
const navMenu = document.getElementById("navMenu");

if (hamburger) {
  hamburger.addEventListener("click", () => {
    navMenu.classList.toggle("active");
    hamburger.classList.toggle("active");
  });
}

// Close mobile menu when clicking a link
document.querySelectorAll(".nav-link, .btn-quote").forEach((link) => {
  link.addEventListener("click", () => {
    navMenu.classList.remove("active");
    hamburger.classList.remove("active");
  });
});

// Navbar scroll effect
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
  if (window.scrollY > 100) {
    navbar.style.boxShadow = "0 5px 20px rgba(0, 0, 0, 0.1)";
    navbar.style.padding = "10px 0";
  } else {
    navbar.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.05)";
    navbar.style.padding = "18px 0";
  }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});

// Counter animation for stats
function animateCounter(element, target) {
  let current = 0;
  const increment = target / 50;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current) + "+";
  }, 30);
}

// Trigger counter animation when stats section is in view
const statElements = document.querySelectorAll(".stat h3, .stat-item h3");
const observerOptions = { threshold: 0.5 };

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting && !entry.target.dataset.animated) {
      const text = entry.target.textContent;
      const number = parseInt(text.replace(/\D/g, ""));
      if (!isNaN(number) && number > 0) {
        entry.target.dataset.animated = "true";
        animateCounter(entry.target, number);
      }
    }
  });
}, observerOptions);

statElements.forEach((el) => observer.observe(el));

// Auto-hide success alert after 5 seconds
const alert = document.querySelector(".alert-success");
if (alert) {
  setTimeout(() => {
    alert.style.transition = "opacity 0.5s, transform 0.5s";
    alert.style.opacity = "0";
    alert.style.transform = "translateY(-20px)";
    setTimeout(() => alert.remove(), 500);
  }, 5000);
}
