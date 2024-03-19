(function () {
    "use strict";

    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
        el = el.trim();
        if (all) {
            return [...document.querySelectorAll(el)];
        } else {
            return document.querySelector(el);
        }
    };

    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
        let selectEl = select(el, all);
        if (selectEl) {
            if (all) {
                selectEl.forEach((e) => e.addEventListener(type, listener));
            } else {
                selectEl.addEventListener(type, listener);
            }
        }
    };

    /**
     * Easy on scroll event listener
     */
    const onscroll = (el, listener) => {
        el.addEventListener("scroll", listener);
    };

    /**
     * Navbar links active state on scroll
     */
    let navbarlinks = select("#navbar .scrollto", true);
    const navbarlinksActive = () => {
        let position = window.scrollY + 200;
        navbarlinks.forEach((navbarlink) => {
            if (!navbarlink.hash) return;
            let section = select(navbarlink.hash);
            if (!section) return;
            if (
                position >= section.offsetTop &&
                position <= section.offsetTop + section.offsetHeight
            ) {
                navbarlink.classList.add("active");
            } else {
                navbarlink.classList.remove("active");
            }
        });
    };
    window.addEventListener("load", navbarlinksActive);
    onscroll(document, navbarlinksActive);

    /**
     * Scrolls to an element with header offset
     */
    const scrollto = (el) => {
        let header = select("#header");
        let offset = header.offsetHeight;

        if (!header.classList.contains("header-scrolled")) {
            offset -= 16;
        }

        let elementPos = select(el).offsetTop;
        window.scrollTo({
            top: elementPos - offset,
            behavior: "smooth",
        });
    };

    /**
     * Toggle .header-scrolled class to #header when page is scrolled
     */
    let selectHeader = select("#header");
    if (selectHeader) {
        const headerScrolled = () => {
            if (window.scrollY > 100) {
                selectHeader.classList.add("header-scrolled");
            } else {
                selectHeader.classList.remove("header-scrolled");
            }
        };
        window.addEventListener("load", headerScrolled);
        onscroll(document, headerScrolled);
    }

    /**
     * Back to top button
     */
    let backtotop = select(".back-to-top");
    if (backtotop) {
        const toggleBacktotop = () => {
            if (window.scrollY > 100) {
                backtotop.classList.add("active");
            } else {
                backtotop.classList.remove("active");
            }
        };
        window.addEventListener("load", toggleBacktotop);
        onscroll(document, toggleBacktotop);
    }

    /**
     * Mobile nav toggle
     */
    on("click", ".mobile-nav-toggle", function (e) {
        select("#navbar").classList.toggle("navbar-mobile");
        this.classList.toggle("bi-list");
        this.classList.toggle("bi-x");
    });

    /**
     * Mobile nav dropdowns activate
     */
    on(
        "click",
        ".navbar .dropdown > a",
        function (e) {
            if (select("#navbar").classList.contains("navbar-mobile")) {
                e.preventDefault();
                this.nextElementSibling.classList.toggle("dropdown-active");
            }
        },
        true
    );

    /**
     * Scrool with ofset on links with a class name .scrollto
     */
    on(
        "click",
        ".scrollto",
        function (e) {
            if (select(this.hash)) {
                e.preventDefault();

                let navbar = select("#navbar");
                if (navbar.classList.contains("navbar-mobile")) {
                    navbar.classList.remove("navbar-mobile");
                    let navbarToggle = select(".mobile-nav-toggle");
                    navbarToggle.classList.toggle("bi-list");
                    navbarToggle.classList.toggle("bi-x");
                }
                scrollto(this.hash);
            }
        },
        true
    );

    /**
     * Scroll with ofset on page load with hash links in the url
     */
    window.addEventListener("load", () => {
        if (window.location.hash) {
            if (select(window.location.hash)) {
                scrollto(window.location.hash);
            }
        }
    });

    /**
     * Initiate glightbox
     */
    const glightbox = GLightbox({
        selector: ".glightbox",
    });

    /**
     * Porfolio isotope and filter
     */
    window.addEventListener("load", () => {
        let portfolioContainer = select(".portfolio-container");
        if (portfolioContainer) {
            let portfolioIsotope = new Isotope(portfolioContainer, {
                itemSelector: ".portfolio-item",
            });

            let portfolioFilters = select("#portfolio-flters li", true);

            on(
                "click",
                "#portfolio-flters li",
                function (e) {
                    e.preventDefault();
                    portfolioFilters.forEach(function (el) {
                        el.classList.remove("filter-active");
                    });
                    this.classList.add("filter-active");

                    portfolioIsotope.arrange({
                        filter: this.getAttribute("data-filter"),
                    });
                },
                true
            );
        }
    });

    /**
     * Initiate portfolio lightbox
     */
    const portfolioLightbox = GLightbox({
        selector: ".portfolio-lightbox",
    });

    /**
     * Portfolio details slider
     */
    new Swiper(".portfolio-details-slider", {
        speed: 400,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        pagination: {
            el: ".swiper-pagination",
            type: "bullets",
            clickable: true,
        },
    });

    /**
     * Testimonials slider
     */
    new Swiper(".testimonials-slider", {
        speed: 600,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        slidesPerView: "auto",
        pagination: {
            el: ".swiper-pagination",
            type: "bullets",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20,
            },

            1200: {
                slidesPerView: 3,
                spaceBetween: 20,
            },
        },
    });

    /**
     * Initiate Pure Counter
     */
    new PureCounter();
})();

// Visualizar ruta del archivo seleccionado
document.getElementById("uploadBtn").onchange = function () {
    document.getElementById("uploadFile").value = this.value;
};

// Visualizar sectionResultados al elegir un archivo para procesar
document.getElementById("uploadBtn").addEventListener("change", function () {
    console.log("Evento change detectado"); // Esto debería aparecer en la consola cuando seleccionas un archivo
    var sectionResultados = document.getElementById("sectionResultados");
    if (this.files.length > 0) {
        console.log("Archivo seleccionado"); // Esto confirmará que realmente se seleccionó un archivo
        sectionResultados.style.display = "block";
    } else {
        sectionResultados.style.display = "none";
    }
});

// Validaciones en template editar
document
    .getElementById("numero_documento")
    .addEventListener("input", function () {
        this.value = this.value.replace(/[^0-9]/g, "");
    });

document.getElementById("nombre").addEventListener("input", function () {
    this.value = this.value.replace(/[^A-Za-z\s]+/g, "");
});

// Nuevas funciones

function showProcessingModal() {
    document.getElementById("processing-modal").style.display = "block";
    document.getElementById("overlay").style.display = "block"; // Mostrar el overlay

    // Agregar un evento de escucha de teclado para bloquear la tecla "Escape"
    window.addEventListener("keydown", blockEscapeKey);
}

// Función para ocultar el modal de procesamiento
function hideProcessingModal() {
    document.getElementById("processing-modal").style.display = "none";
    document.getElementById("overlay").style.display = "none"; // Ocultar el overlay

    // Remover el evento de escucha de teclado para la tecla "Escape"
    window.removeEventListener("keydown", blockEscapeKey);
}

// Función para bloquear la tecla "Escape"
function blockEscapeKey(event) {
    if (event.key === "Escape") {
        event.preventDefault(); // Evitar la acción predeterminada de la tecla "Escape"
    }
}

// Verificar si hay un mensaje en la URL y mostrarlo en un popup de alerta
const urlParams = new URLSearchParams(window.location.search);
const message = urlParams.get("message");
if (message) {
    alert(message);
    // Eliminar el parámetro de consulta de la URL
    history.replaceState({}, document.title, window.location.pathname);
}

function checkFile() {
    var fileInput = document.getElementById("file-input");
    var tipo_documento = document.getElementById("tipo_documento");
    var numero_documento = document.getElementById("numero_documento");
    var nombre = document.getElementById("nombre");
    var edad = document.getElementById("edad");
    var genero = document.getElementById("genero");
    var estado_civil = document.getElementById("estado_civil");
    var correo = document.getElementById("correo");
    var telefono = document.getElementById("telefono");
    var nivel_estudios = document.getElementById("nivel_estudios");
    var tipo_vivienda = document.getElementById("tipo_vivienda");
    var estrato = document.getElementById("estrato");
    var num_hijos = document.getElementById("num_hijos");
    var personas_cargo = document.getElementById("personas_cargo");
    var experiencia = document.getElementById("experiencia");
    var area_experiencia = document.getElementById("area_experiencia");
    var tiempo_ventas = document.getElementById("tiempo_ventas");
    var experiencia_general = document.getElementById("experiencia_general");
    var otra_area_experiencia = document.getElementById(
        "otra_area_experiencia"
    );
    var uploadBtn = document.getElementById("upload-btn");

    if (
        fileInput.files.length > 0 &&
        tipo_documento.value.trim() !== "" &&
        numero_documento.value.trim() !== "" &&
        nombre.value.trim() !== "" &&
        edad.value.trim() !== "" &&
        genero.value.trim() !== "" &&
        estado_civil.value.trim() !== "" &&
        correo.value.trim() !== "" &&
        telefono.value.trim() !== "" &&
        nivel_estudios.value.trim() !== "" &&
        tipo_vivienda.value.trim() !== "" &&
        estrato.value.trim() !== "" &&
        num_hijos.value.trim() !== "" &&
        personas_cargo.value.trim() !== "" &&
        experiencia.value.trim() !== "" &&
        area_experiencia.value.trim() !== "" &&
        tiempo_ventas.value.trim() !== "" &&
        experiencia_general.value.trim() !== "" &&
        otra_area_experiencia.value.trim() !== ""
    ) {
        uploadBtn.disabled = false;
    } else {
        uploadBtn.disabled = true;
    }
}

// Validacion en acciones
function confirmarEliminar(id, nombre) {
    if (confirm("¿Estás seguro de que quieres eliminar el registro de " + nombre + "?")) {
        document.getElementById("eliminarForm" + id).submit();
    }
}


function mostrarAlerta() {
    alert("Registro actualizado");
}

// Calcular edad
function calcularEdad(fechaNacimiento) {
    // Parsear la fecha de nacimiento a un objeto Date
    const dob = new Date(fechaNacimiento);
    // Obtener la fecha actual
    const today = new Date();
    // Calcular la diferencia de años
    let edad = today.getFullYear() - dob.getFullYear();
    // Corregir la edad si el cumpleaños aún no ha pasado este año
    const mesActual = today.getMonth();
    const diaActual = today.getDate();
    const mesNacimiento = dob.getMonth();
    const diaNacimiento = dob.getDate();
    if (
        mesActual < mesNacimiento ||
        (mesActual === mesNacimiento && diaActual < diaNacimiento)
    ) {
        edad--;
    }
    return edad;
}
