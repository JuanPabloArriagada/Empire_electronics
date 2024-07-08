// Función para validar el RUT chileno
function validateRut(rut) {
    // Eliminar puntos y guiones
    rut = rut.replace(/[.-]/g, '');

    // Verificar que el RUT tenga al menos 9 caracteres
    if (rut.length < 9) {
        return false;
    }

    // Separar el cuerpo y el dígito verificador
    const cuerpo = rut.slice(0, -1);
    const dv = rut.slice(-1).toUpperCase();

    // Calcular el dígito verificador esperado
    let suma = 0;
    let multiplo = 2;

    for (let i = 1; i <= cuerpo.length; i++) {
        const index = multiplo * rut.charAt(cuerpo.length - i);
        suma += index;

        if (multiplo < 7) {
            multiplo += 1;
        } else {
            multiplo = 2;
        }
    }

    const dvEsperado = 11 - (suma % 11);
    let dvFinal = dvEsperado.toString();

    if (dvEsperado === 11) {
        dvFinal = '0';
    } else if (dvEsperado === 10) {
        dvFinal = 'K';
    }

    // Comparar el dígito verificador esperado con el ingresado
    return dvFinal === dv;
}

// Función para manejar la validación del RUT en el formulario
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.register-form');
    const rutInput = form.querySelector('input[name="rut"]');
    
    form.addEventListener('submit', function (event) {
        const rutValue = rutInput.value;
        if (!validateRut(rutValue)) {
            event.preventDefault();
            alert('El RUT ingresado no es válido. Por favor, ingrese un RUT válido.');
        }
    });
});
