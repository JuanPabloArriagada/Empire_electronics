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

/** CONTRASEÑA **/
function verificarContraseñas() {
    // Obtener los elementos del formulario
    const form = document.getElementById('formulario_registro');
    const password1 = document.getElementById('contraseña_cliente');
    const password2 = document.getElementById('contraseña_clienteV');
    const errorElement = document.getElementById('id_lbl_contraseñaV');

    // Verifica si `form`, `password1`, `password2` o `errorElement` son `null` o `undefined`
    if (!form || !password1 || !password2 || !errorElement) {
        console.error('Algunos elementos del DOM no se pudieron encontrar.');
        return;
    }

    // Función para verificar si las contraseñas coinciden
    function verificarYActuar(event) {
        // Prevenir el envío del formulario inicialmente
        event.preventDefault();

        if (password1.value !== password2.value) {
            // Si las contraseñas no coinciden, mostrar mensaje de error
            errorElement.style.display = 'block';
        } else {
            // Si las contraseñas coinciden, ocultar el mensaje de error
            errorElement.style.display = 'none';
            // Proceder a enviar el formulario
            form.submit();
        }
    }

    // Agregar evento 'submit' al formulario para verificar las contraseñas
    form.addEventListener('submit', verificarYActuar);

    // También ocultar el mensaje de error si los valores de las contraseñas cambian
    function ocultarError() {
        errorElement.style.display = 'none';
    }

    password1.addEventListener('input', ocultarError);
    password2.addEventListener('input', ocultarError);
}



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
