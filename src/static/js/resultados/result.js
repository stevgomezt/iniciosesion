(function ($) {
    var $window = $(window),
        $body = $("body"),
        $sidebar = $("#sidebar");

    // Breakpoints.
    breakpoints({
        xlarge: ["1281px", "1680px"],
        large: ["981px", "1280px"],
        medium: ["737px", "980px"],
        small: ["481px", "736px"],
        xsmall: [null, "480px"],
    });

    // Play initial animations on page load.
    $window.on("load", function () {
        window.setTimeout(function () {
            $body.removeClass("is-preload");
        }, 100);
    });

    // Sidebar.
    if ($sidebar.length > 0) {
        var $sidebar_a = $sidebar.find("a");

        $sidebar_a
            .addClass("scrolly")
            .on("click", function () {
                var $this = $(this);

                // External link? Bail.
                if ($this.attr("href").charAt(0) != "#") return;

                // Deactivate all links.
                $sidebar_a.removeClass("active");

                // Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
                $this.addClass("active").addClass("active-locked");
            })
            .each(function () {
                var $this = $(this),
                    id = $this.attr("href"),
                    $section = $(id);

                // No section for this link? Bail.
                if ($section.length < 1) return;

                // Scrollex.
                $section.scrollex({
                    mode: "middle",
                    top: "-20vh",
                    bottom: "-20vh",
                    initialize: function () {
                        // Deactivate section.
                        $section.addClass("inactive");
                    },
                    enter: function () {
                        // Activate section.
                        $section.removeClass("inactive");

                        // No locked links? Deactivate all links and activate this section's one.
                        if ($sidebar_a.filter(".active-locked").length == 0) {
                            $sidebar_a.removeClass("active");
                            $this.addClass("active");
                        }

                        // Otherwise, if this section's link is the one that's locked, unlock it.
                        else if ($this.hasClass("active-locked"))
                            $this.removeClass("active-locked");
                    },
                });
            });
    }

    // Scrolly.
    $(".scrolly").scrolly({
        speed: 1000,
        offset: function () {
            // If <=large, >small, and sidebar is present, use its height as the offset.
            if (
                breakpoints.active("<=large") &&
                !breakpoints.active("<=small") &&
                $sidebar.length > 0
            )
                return $sidebar.height();

            return 0;
        },
    });
})(jQuery);

// Función para generar un número aleatorio entre min y max
function getRandomPercentage(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Función para asignar valores aleatorios a las barras de progreso y valores de porcentaje
function asignarValoresAleatorios() {
    const barrasDeProgreso = document.querySelectorAll(".skill-per");

    barrasDeProgreso.forEach((barra) => {
        const porcentaje = getRandomPercentage(0, 100);
        barra.style.width = porcentaje + "%";

        // Define los colores según los rangos especificados
        let color = "";
        if (porcentaje >= 0 && porcentaje < 20) {
            color = "rgb(231, 135, 1)";
        } else if (porcentaje >= 20 && porcentaje < 40) {
            color = "rgb(255 197 0)";
        } else if (porcentaje >= 40 && porcentaje < 60) {
            color = "rgb(254 255 0)";
        } else if (porcentaje >= 60 && porcentaje < 80) {
            color = "rgb(160 255 0)";
        } else {
            color = "rgb(0 209 33)";
        }

        barra.style.backgroundColor = color;

        // Actualiza el valor de porcentaje visible
        const contenedor = barra.parentElement;
        const porcentajeElement = contenedor.querySelector(".tooltipsg");
        porcentajeElement.textContent = porcentaje + "%";
    });
}

// Llamar a la función para asignar valores aleatorios al cargar la página
asignarValoresAleatorios();
