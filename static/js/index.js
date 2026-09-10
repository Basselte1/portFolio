

// Definir et initialise objet puis passer la classe ('') utiliser pour l'auto saisir
let typed = new Typed('.auto-typing', {
        strings: ['solutions informatiques','Developpement','applications web','applications mobiles','logiciels desktop','conception sites internet','hébergement sur mesure'], // passer objet qui contient les options
        typeSpeed: 100,  // vitesse de saisir
        backSpeed: 100, // vitesse de disparition des elements
        loop: true, //affichage des elements en boucle
        fadeOut: true, //effet
        fadeOutClass: 'typed-fade-out',
        fadeOutDelay:500,
})

    /// togle navbar

    function toggleMenu() {
    const navLinks = document.getElementById("nav-links");
    navLinks.classList.toggle("active");
    }
    //section swipper

    var swiper = new Swiper(".mySwiper", {
      slidesPerView: 2, //nombre de logos visible sur mobile
      spaceBetween: 10, //espace entre les logos
        loop: true, //boucle continue
        autoplay: {
            delay: 1500,
            disableOnInteraction: false,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
          640: { slidesPerView: 3, spaceBetween: 20 },
          768: { slidesPerView: 4, spaceBetween: 30 },
            1024: { slidesPerView: 5, spaceBetween: 40 }
        }
});

 //modal
  document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById("successModal");
    const closeBtn = document.querySelector(".close");

    // Affiche la modal si elle contient un message
    if (modal && modal.querySelector("p") && modal.querySelector("p").textContent.trim() !== "") {
      modal.style.display = "block";
    }

    // Ferme la modal en cliquant sur le bouton X
    if (closeBtn) {
      closeBtn.onclick = function () {
        modal.style.display = "none";
      };
    }

    // Ferme la modal si clic à l’extérieur
    window.onclick = function (event) {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    };
});