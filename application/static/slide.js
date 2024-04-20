// Select the mobile menu toggle button and the menu links
const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

// Add a click event listener to the mobile menu toggle button
menu.addEventListener('click', function() {
  // Toggle the 'is-active' class on the mobile menu toggle button
  menu.classList.toggle('is-active');
  // Toggle the 'active' class on the menu links to show/hide them
  menuLinks.classList.toggle('active');
});
