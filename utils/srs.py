import datetime

def calcular_proximo_repaso(calidad_respuesta, repeticiones_previas, factor_facilidad, intervalo_previo):
    """
    Algoritmo SM-2 para calcular la próxima fecha de revisión de un tema o flashcard.
    
    Parámetros:
    - calidad_respuesta: Int de 0 a 5. 
        (0 = Olvido total, 3 = Recordé con esfuerzo, 5 = Recordé perfectamente)
    - repeticiones_previas: Cuántas veces seguidas has recordado esto correctamente.
    - factor_facilidad: Multiplicador base (usualmente inicia en 2.5).
    - intervalo_previo: Días que pasaron desde la última revisión.
    
    Retorna:
    - (nuevas_repeticiones, nuevo_factor, nuevo_intervalo, fecha_proxima_revision)
    """
    
    # Si la calidad es menor a 3, significa que fallaste o te costó demasiado. Se reinicia el conteo.
    if calidad_respuesta < 3:
        repeticiones_previas = 0
        nuevo_intervalo = 1 # Repasar al día siguiente
    else:
        # Si respondiste bien (3, 4 o 5)
        if repeticiones_previas == 0:
            nuevo_intervalo = 1
        elif repeticiones_previas == 1:
            nuevo_intervalo = 6
        else:
            # Multiplicamos el intervalo anterior por el factor de facilidad
            nuevo_intervalo = round(intervalo_previo * factor_facilidad)
        
        repeticiones_previas += 1

    # Ajustamos el factor de facilidad basado en la calidad de la respuesta
    nuevo_factor = factor_facilidad + (0.1 - (5 - calidad_respuesta) * (0.08 + (5 - calidad_respuesta) * 0.02))
    
    # El factor nunca debe caer por debajo de 1.3 (para evitar que se estanque)
    if nuevo_factor < 1.3:
        nuevo_factor = 1.3

    # Calculamos la fecha exacta del próximo repaso
    fecha_proxima_revision = datetime.date.today() + datetime.timedelta(days=nuevo_intervalo)

    return repeticiones_previas, round(nuevo_factor, 2), nuevo_intervalo, fecha_proxima_revision

# --- EJEMPLO DE USO ---
# Si un usuario crea una tarjeta nueva hoy:
# repeticiones = 0, factor = 2.5, intervalo = 0
# 
# Si el usuario responde con una nota de "4" (Bien):
# calcular_proximo_repaso(4, 0, 2.5, 0)
