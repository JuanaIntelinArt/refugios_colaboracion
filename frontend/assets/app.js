const NOMBRES_REFUGIOS = {
    "1": "Esperanza Canina", "2": "Patitas Felices", "3": "Rescate Cochabamba",
    "4": "Amigos de Cuatro Patas", "5": "Corazón Animal"
};

const urlParams = new URLSearchParams(window.location.search);
const refugioId = urlParams.get('refugio');

// Función para cargar los datos del JSON y actualizar el DOM
async function cargarDatosYActualizarUI() {
    const nombreRefugioElement = document.getElementById('nombreRefugio');
    const fondosElement = document.getElementById('fondos-recaudados');
    const horasElement = document.getElementById('horas-totales');
    const tablaPracticantes = document.querySelector('#practicantes-table tbody');

    // 1. Mostrar el nombre del refugio logeado
    if (refugioId && NOMBRES_REFUGIOS[refugioId]) {
        nombreRefugioElement.textContent = NOMBRES_REFUGIOS[refugioId];
    } else {
        nombreRefugioElement.textContent = "Desconocido (Error)";
        return;
    }

    try {
        // La ruta asume que el JSON está en /frontend/data/ y el script está en /frontend/assets/js/
        const response = await fetch('./data/reporte_datos.json'); 
        if (!response.ok) throw new Error(`HTTP status: ${response.status}`);
        
        const data = await response.json();
        console.log("Datos cargados del backend:", data);

        const refugioActual = data.refugios[refugioId];
        
        if(refugioActual) {
            // 2. Actualizar Totales del Refugio
            fondosElement.textContent = `$${refugioActual.fondos_recaudados.toFixed(2)}`;
            horasElement.textContent = refugioActual.horas_registradas_total;
            
            // 3. Llenar la Tabla de Practicantes
            tablaPracticantes.innerHTML = ''; // Limpiar contenido anterior
            data.practicantes.forEach(p => {
                const row = tablaPracticantes.insertRow();
                row.insertCell().textContent = p.nombre;
                row.insertCell().textContent = p.carrera;
                row.insertCell().textContent = p.horas_acumuladas;
                row.insertCell().textContent = p.incentivo_pendiente.toFixed(2); // Formato de 2 decimales
            });
        }

    } catch (error) {
        console.error("Error al cargar datos. Asegúrate de que el script Python se ejecutó y Live Server está activo:", error);
    }
}

// Ejecutar al cargar la página
window.onload = cargarDatosYActualizarUI;