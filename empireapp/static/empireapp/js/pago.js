document.addEventListener("DOMContentLoaded", function() {
    // Ruta del archivo producto.html
    const rutaProducto = '../../index.html';

    // Obtiene el contenido del archivo producto.html
    fetch(rutaProducto)
        .then(response => response.text())
        .then(html => {
            // Crea un elemento HTML temporal para parsear el contenido
            const parser = new DOMParser();
            const productoHtml = parser.parseFromString(html, 'text/html');

            // Obtiene el valor de idPrecio
            const idPrecioElement = productoHtml.getElementById('idPrecio');
            const montoString = idPrecioElement.innerText;

            // Quitar el símbolo de dólar y los espacios en blanco del valor del monto
            const montoNumerico = parseInt(montoString.replace(/\D+/g, ''));

            // Actualiza el valor del campo oculto con el monto
            const montoInput = document.getElementById("monto");
            montoInput.value = montoNumerico;
        })
        .catch(error => console.error('Error al obtener el contenido del archivo:', error));
});

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const mensajeExito = document.getElementById('mensajeExito');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar envío del formulario

        // Mostrar mensaje de éxito
        mensajeExito.style.display = 'block';

        // Redirigir a otra página después de 3 segundos
        setTimeout(function() {
            // Cambiar la URL a la página deseada
            window.location.href = '../../index.html';
        }, 2000); // 2000 milisegundos = 3 segundos
    });
});

