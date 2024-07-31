const mobileMenu = document.getElementById('mobile-menu');
const navbarMenu = document.querySelector('.navbar__menu');

mobileMenu.addEventListener('click', () => {
  navbarMenu.classList.toggle('active');
});