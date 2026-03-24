import streamlit as st
from streamlit_calendar import calendar  # <--- ESTO SIEMPRE ARRIBA

# Luego el resto de tu código...
st.sidebar.title("StudyOS 📓")

# --- CONFIGURACIÓN DE LA BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("StudyOS 📓")

# Nueva navegación corregida
navegacion = st.sidebar.radio(
    "Navegación",
    ["🏠 Inicio", "🗓️ Calendario", "🎓 Universidad", "📝 Exámenes", "⚡ Sistema de Estudio"]
)

# --- LÓGICA DE LAS SECCIONES ---

if navegacion == "🏠 Inicio":
    st.title("Panel de Control")
    # Aquí va tu código actual de métricas (Tarjetas, Próximo Examen, Horas)
    
elif navegacion == "🗓️ Calendario":
    st.title("Tu Agenda")
           

# --- SECCIÓN CALENDARIO ---
if navegacion == "🗓️ Calendario":
    st.title("📅 Agenda Académica")
    
    # 1. Configuración de opciones del calendario
    calendar_options = {
        "editable": True,
        "selectable": True,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridMonth,timeGridWeek,timeGridDay",
        },
        "initialView": "dayGridMonth", # Vista mensual por defecto
    }

    # 2. Base de datos temporal de eventos (Luego la conectaremos a Notion o SQL)
    if "eventos" not in st.session_state:
        st.session_state.eventos = [
            {"title": "Examen Biología", "start": "2026-03-25", "end": "2026-03-25", "color": "#FF4B4B"},
            {"title": "Repaso Flashcards", "start": "2026-03-24T10:00:00", "end": "2026-03-24T11:00:00", "color": "#3D5A80"}
        ]

    # 3. Renderizar el calendario
    state = calendar(
        events=st.session_state.eventos,
        options=calendar_options,
        key="calendar",
    )

    # 4. Lógica para Agregar / Editar (Interacción)
    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("➕ Nuevo Evento / Recordatorio")
        nuevo_titulo = st.text_input("Nombre del evento")
        fecha_evento = st.date_input("Fecha")
        hora_evento = st.time_input("Hora (opcional)")
        
        if st.button("Guardar en Agenda"):
            nuevo_ev = {
                "title": nuevo_titulo,
                "start": f"{fecha_evento}T{hora_evento}",
                "color": "#2E7D32"
            }
            st.session_state.eventos.append(nuevo_ev)
            st.rerun()

    with col2:
        st.subheader("🔔 Recordatorios")
        if st.session_state.eventos:
            for ev in st.session_state.eventos:
                st.write(f"📍 {ev['title']} - {ev['start']}")
        else:
            st.info("No hay recordatorios pendientes.")

    # 5. Captura de eventos del calendario (clics)
    if state.get("eventClick"):
        st.write(f"Has seleccionado: **{state['eventClick']['event']['title']}**")
        if st.button("Eliminar evento seleccionado"):
            # Lógica para filtrar y eliminar
            st.session_state.eventos = [e for e in st.session_state.eventos if e['title'] != state['eventClick']['event']['title']]
            st.rerun()
    # Lógica del calendario

elif navegacion == "🎓 Universidad":
    st.title("Gestión Universitaria")
    st.info("Aquí puedes gestionar tus materias activas, créditos y profesores.")
    # Aquí puedes añadir una base de datos de tus materias del semestre

elif navegacion == "📝 Cursos":
    st.title("Gestion de Cursos")
    st.warning("Próximos retos académicos.")
    # Aquí puedes poner la tabla de fechas de exámenes y notas

elif navegacion == "⚡ Sistema de Estudio":
    st.title("Método de Estudio")
    # Aquí es donde integraríamos la fórmula de Repetición Espaciada que vimos antes
