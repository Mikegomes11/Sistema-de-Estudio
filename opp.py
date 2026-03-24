import streamlit as st

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
    # Lógica del calendario

elif navegacion == "🎓 Universidad":
    st.title("Gestión Universitaria")
    st.info("Aquí puedes gestionar tus materias activas, créditos y profesores.")
    # Aquí puedes añadir una base de datos de tus materias del semestre

elif navegacion == "📝 Exámenes":
    st.title("Control de Exámenes")
    st.warning("Próximos retos académicos.")
    # Aquí puedes poner la tabla de fechas de exámenes y notas

elif navegacion == "⚡ Sistema de Estudio":
    st.title("Método de Estudio")
    # Aquí es donde integraríamos la fórmula de Repetición Espaciada que vimos antes
