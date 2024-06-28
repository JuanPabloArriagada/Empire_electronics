document.addEventListener("DOMContentLoaded", function () {
    var numberCart = document.getElementById("empire-cart__number");
    var contenedorCart = document.getElementById("empire-cart-container");
    // Función para mostrar u ocultar el contenedor
    function toggleContenedor() {
        if (contenedorCart.style.display === "none") {
            contenedorCart.style.display = "flex";
        } else {
            contenedorCart.style.display = "none";
        }
    }
    // Ocultar el contenedor al cargar la página
    contenedorCart.style.display = "none";

    // Agregar evento de clic a la numberCart
    numberCart.addEventListener("click", toggleContenedor);
});
document.addEventListener("DOMContentLoaded", function () {
    var numberCart = document.getElementById("empire-usuario");
    var contenedorCart = document.getElementById("empire-usuario-container");
    // Función para mostrar u ocultar el contenedor
    function toggleContenedor() {
        if (contenedorCart.style.display === "none") {
            contenedorCart.style.display = "flex";
        } else {
            contenedorCart.style.display = "none";
        }
    }
    // Ocultar el contenedor al cargar la página
    contenedorCart.style.display = "none";

    // Agregar evento de clic a la numberCart
    numberCart.addEventListener("click", toggleContenedor);
});


// Función para cargar las comunas desde el archivo JSON
// Ruta del archivo JSON
const jsonUrl = 'https://gist.github.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd?permalink_comment_id=4161463#gistcomment-4161463';

// Función para cargar el JSON y llenar el select
function loadCommunes() {
    fetch(jsonUrl)
        .then(response => response.json())
        .then(data => {
            // Toma la primera región (Arica y Parinacota) para este ejemplo
            const region = data.regions[0];

            // Accede a las comunas de la región
            const comunas = region.communes;

            // Encuentra el select de comunas en el DOM
            const selectElement = document.getElementById('comunas-select');

            // Itera sobre cada comuna y añade una opción al select
            comunas.forEach(comuna => {
                const option = document.createElement('option');
                option.value = comuna.id;
                option.textContent = comuna.name;
                selectElement.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error al cargar el archivo JSON:', error);
        });
}

// Llama a la función cuando el documento haya cargado
document.addEventListener('DOMContentLoaded', loadCommunes);
