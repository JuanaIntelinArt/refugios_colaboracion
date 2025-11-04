import random
import json
import os # Necesario para crear la carpeta 'data' si no existe

# --- CONFIGURACIÓN GLOBAL ---
TASA_INCENTIVO_POR_HORA = 0.50     # 0.50 Bs. por hora de práctica.
PERCENTAJE_INCENTIVO_FONDOS = 0.10 # 10% de los fondos va a la bolsa de incentivos (bono).
CANTIDAD_PRACTICANTES_PRODUCCION = 3 
HORAS_PRODUCCION_TOTAL = 12        # 2 días * 6 horas por día.

# --- 1. ESTRUCTURA DE DATOS INICIAL ---
REFUGIOS = {
    1: {
        "nombre": "Esperanza Canina", "ubicacion": "Zona Norte",
        "perros_viejos": 20, "gatos_permanentes": 10, "necesidad_veterinaria": "Alta",
        "horas_practica_veterinaria": 0, "horas_practica_marketing": 0,
        "fondos_recaudados": 0.0, "horas_registradas_total": 0
    },
    2: {
        "nombre": "Patitas Felices", "ubicacion": "Zona Sur",
        "perros_viejos": 20, "gatos_permanentes": 10, "necesidad_veterinaria": "Media",
        "horas_practica_veterinaria": 0, "horas_practica_marketing": 0,
        "fondos_recaudados": 0.0, "horas_registradas_total": 0
    },
    3: {
        "nombre": "Rescate Cochabamba", "ubicacion": "Centro",
        "perros_viejos": 20, "gatos_permanentes": 10, "necesidad_veterinaria": "Alta",
        "horas_practica_veterinaria": 0, "horas_practica_marketing": 0,
        "fondos_recaudados": 0.0, "horas_registradas_total": 0
    },
    4: {
        "nombre": "Amigos de Cuatro Patas", "ubicacion": "Sacaba",
        "perros_viejos": 20, "gatos_permanentes": 10, "necesidad_veterinaria": "Media",
        "horas_practica_veterinaria": 0, "horas_practica_marketing": 0,
        "fondos_recaudados": 0.0, "horas_registradas_total": 0
    },
    5: {
        "nombre": "Corazón Animal", "ubicacion": "Tiquipaya",
        "perros_viejos": 20, "gatos_permanentes": 10, "necesidad_veterinaria": "Baja",
        "horas_practica_veterinaria": 0, "horas_practica_marketing": 0,
        "fondos_recaudados": 0.0, "horas_registradas_total": 0
    }
}

PRACTICANTES = [
    {"id": "VET001", "nombre": "Ana López", "carrera": "Veterinaria", "horas_acumuladas": 0, "incentivo_pendiente": 0.0},
    {"id": "MKT001", "nombre": "Juan Pérez", "carrera": "Marketing", "horas_acumuladas": 0, "incentivo_pendiente": 0.0},
    {"id": "VET002", "nombre": "Carlos Soto", "carrera": "Veterinaria", "horas_acumuladas": 0, "incentivo_pendiente": 0.0},
    {"id": "MKT002", "nombre": "Sofía Ramos", "carrera": "Marketing", "horas_acumuladas": 0, "incentivo_pendiente": 0.0},
    {"id": "VET003", "nombre": "David Cruz", "carrera": "Veterinaria", "horas_acumuladas": 0, "incentivo_pendiente": 0.0},
]

# --- 2. FUNCIONES DE LÓGICA DE NEGOCIO ---

def buscar_practicante(practicante_id: str):
    return next((p for p in PRACTICANTES if p["id"] == practicante_id), None)

def registrar_horas(practicante_id: str, refugio_id: int, num_horas: int):
    # ... (código para registrar horas) ... (Mantenemos la implementación anterior)
    if refugio_id not in REFUGIOS: return
    practicante = buscar_practicante(practicante_id)
    if not practicante: return
    practicante["horas_acumuladas"] += num_horas
    refugio = REFUGIOS[refugio_id]
    if practicante["carrera"] == "Veterinaria":
        refugio["horas_practica_veterinaria"] += num_horas
    else:
        refugio["horas_practica_marketing"] += num_horas
    refugio["horas_registradas_total"] += num_horas
    print(f"✅ Éxito: Se registraron {num_horas}h para {practicante['nombre']} en {refugio['nombre']}.")

def registrar_horas_produccion(practicante_ids: list, refugio_id: int):
    if refugio_id not in REFUGIOS: return
    if len(practicante_ids) != CANTIDAD_PRACTICANTES_PRODUCCION:
        print(f"❌ Error: Se requieren exactamente {CANTIDAD_PRACTICANTES_PRODUCCION} IDs.")
        return
        
    print(f"\n📢 Registrando **{HORAS_PRODUCCION_TOTAL}** horas de producción de huesos:")
    for practicante_id in practicante_ids:
        practicante = buscar_practicante(practicante_id)
        if practicante:
            practicante["horas_acumuladas"] += HORAS_PRODUCCION_TOTAL
            REFUGIOS[refugio_id]["horas_practica_marketing"] += HORAS_PRODUCCION_TOTAL
            REFUGIOS[refugio_id]["horas_registradas_total"] += HORAS_PRODUCCION_TOTAL
            print(f"   ✅ {practicante['nombre']} ha acumulado {HORAS_PRODUCCION_TOTAL} horas.")


def registrar_recaudacion(refugio_id: int, monto: float):
    if refugio_id not in REFUGIOS: return
    REFUGIOS[refugio_id]["fondos_recaudados"] += monto
    print(f"✅ Éxito: **{monto:.2f} Bs.** recaudados en {REFUGIOS[refugio_id]['nombre']}.")

def asignar_turno_mercado():
    # ... (código para asignar turno) ... (Mantenemos la implementación anterior)
    practicantes_mkt = [p for p in PRACTICANTES if p["carrera"] == "Marketing"]
    practicantes_vet = [p for p in PRACTICANTES if p["carrera"] == "Veterinaria"]
    asignados = []
    if practicantes_mkt: asignados.append(random.choice(practicantes_mkt)); practicantes_mkt.remove(asignados[0])
    disponibles_restantes = practicantes_mkt + practicantes_vet
    if disponibles_restantes:
        segundo_asignado = random.choice(disponibles_restantes)
        if segundo_asignado['id'] not in [p['id'] for p in asignados]: 
            asignados.append(segundo_asignado)
    if len(asignados) < 2: return []
    nombres_asignados = [p['nombre'] for p in asignados]
    print(f"\n📢 **Turno del Mercado Asignado (Sábado):** {nombres_asignados[0]} y {nombres_asignados[1]}")
    return nombres_asignados


def simular_venta_huesos(refugio_id: int):
    if refugio_id not in REFUGIOS: return
    CANTIDAD_HUESOS = 200
    INVERSION_HUESOS = 100.0
    CAPITAL_PRODUCTOS = 1000.0
    precios_posibles = [5, 8, 10]
    ingreso_huesos = sum(random.choice(precios_posibles) for _ in range(CANTIDAD_HUESOS))
    ganancia_huesos = ingreso_huesos - INVERSION_HUESOS
    ganancia_productos = CAPITAL_PRODUCTOS * 0.25 
    ganancia_total_semanal = ganancia_huesos + ganancia_productos
    registrar_recaudacion(refugio_id, ganancia_total_semanal)
    print("-" * 40)
    print(f"📈 **Resultado Puesto Mercado:** {ganancia_total_semanal:.2f} Bs. Neta")
    print("-" * 40)


def calcular_incentivos():
    for p in PRACTICANTES:
        p['incentivo_pendiente'] = p['horas_acumuladas'] * TASA_INCENTIVO_POR_HORA
    
    fondos_totales_recaudados = sum(r['fondos_recaudados'] for r in REFUGIOS.values())
    bolsa_bono = fondos_totales_recaudados * PERCENTAJE_INCENTIVO_FONDOS
    horas_totales_practicantes = sum(p['horas_acumuladas'] for p in PRACTICANTES)
    
    if horas_totales_practicantes > 0:
        print(f"\n📢 **BONO DE FONDOS**: {bolsa_bono:.2f} Bs. a distribuir.")
        for p in PRACTICANTES:
            proporcion_horas = p['horas_acumuladas'] / horas_totales_practicantes
            bono_individual = bolsa_bono * proporcion_horas
            p['incentivo_pendiente'] += bono_individual

# --- 3. EXPORTACIÓN DE DATOS ---

def exportar_datos_json():
    """Exporta las estructuras de datos REFUGIOS y PRACTICANTES a un archivo JSON."""
    datos_para_exportar = {
        "timestamp": "Reporte generado",
        "refugios": REFUGIOS,
        "practicantes": PRACTICANTES
    }
    # Ruta relativa correcta: desde /backend/ hasta /frontend/data/
    ruta_archivo = "../frontend/data/reporte_datos.json" 
    
    # Crea la carpeta 'data' si no existe
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos_para_exportar, f, ensure_ascii=False, indent=4)
        print(f"\n💾 **EXPORTACIÓN EXITOSA** a {ruta_archivo}")
    except Exception as e:
        print(f"\n❌ Error al exportar a JSON: {e}")

# --- 4. SIMULACIÓN DE EJECUCIÓN DEL PROYECTO ---

if __name__ == "__main__":
    
    print("--- INICIO DE SIMULACIÓN SEMANAL ---")
    registrar_horas("VET001", 1, 15)  
    registrar_horas("MKT001", 3, 20)  
    registrar_horas("VET002", 2, 10)  
    registrar_horas("MKT002", 4, 15)  

    # Horas de Producción de Huesos (3 personas, 12 horas c/u)
    registrar_horas_produccion(["VET001", "MKT001", "VET003"], 1)

    print("\n--- REGISTRO DE RECAUDACIÓN DE FONDOS ---")
    registrar_recaudacion(1, 500.00) 
    registrar_recaudacion(3, 300.00)
    
    print("\n--- LOGÍSTICA DEL MERCADO ---")
    asignar_turno_mercado() 
    simular_venta_huesos(1) # Simulación de la venta semanal

    print("\n--- CÁLCULO Y EXPORTACIÓN ---")
    calcular_incentivos()

    # Genera el archivo para que el frontend lo lea
    exportar_datos_json()