# 🐾 Refugios Colaboración Cochabamba: Gestión de Voluntarios e Incentivos

Este es un proyecto de gestión de la colaboración entre practicantes y refugios de animales en Cochabamba. El sistema simula la acumulación de horas de práctica, la recaudación de fondos (incluyendo la venta de huesos al horno en el mercado) y el cálculo de incentivos económicos para los practicantes.

---

## 🛠️ Arquitectura del Proyecto

El proyecto está dividido en una arquitectura de Backend y Frontend:

### 🐍 Backend (Python)

Ubicado en la carpeta `/backend/`.

* **`datos_refugios.py`**: Contiene la lógica central del negocio:
    * Estructura de datos (`REFUGIOS` y `PRACTICANTES`).
    * Funciones de registro de horas (práctica regular y producción de huesos).
    * Simulación de asignación de turnos (mercado).
    * Cálculo de incentivos (tarifa por hora + bono proporcional por fondos).
    * Exportación de datos a JSON para el Frontend.

### 💻 Frontend (HTML, CSS, JS)

Ubicado en la carpeta `/frontend/`.

* **`index.html`**: Página de inicio y login (simulado).
* **`cronograma.html`**: Dashboard principal que muestra los datos del refugio y los acumulados de los practicantes.
* **`/assets/style.css`**: Contiene todos los estilos, incluyendo el fondo de la página de inicio.
* **`/assets/js/app.js`**: JavaScript encargado de leer el archivo `reporte_datos.json` y actualizar las tablas en `cronograma.html`.

---

## 🚀 Cómo Ejecutar el Proyecto

Este proyecto requiere ejecutar la parte de Python para generar los datos antes de ver la interfaz web.

### Paso 1: Generar los Datos (Backend)

1.  Abre tu terminal en Visual Studio Code.
2.  Navega a la carpeta del backend: `cd backend`
3.  Ejecuta el script de Python:
    ```bash
    python datos_refugios.py
    ```
    *Resultado: Se simula una semana de trabajo y se crea el archivo `/frontend/data/reporte_datos.json`.*

### Paso 2: Ver el Frontend (Web)

1.  Vuelve a la carpeta raíz del proyecto: `cd ..`
2.  Abre el archivo `frontend/index.html` usando la extensión **Live Server** en VSC para evitar errores al leer el JSON.

### Paso 3: Iniciar Sesión (Mock)

Usa estas credenciales para acceder:

| ID del Refugio | Contraseña |
| :------------- | :--------- |
| **1** | **123** |
| **2** | **456** |

