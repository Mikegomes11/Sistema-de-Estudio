import streamlit as st

# 1. Configuración inicial de la página (Debe ser la primera instrucción)
st.set_page_config(
    page_title="StudyOS | Gestión Universitaria",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inyección de CSS Personalizado (Paleta de tonos fríos y alto contraste)
def cargar_css():
    st.markdown("""
        <style>
        /* Fondo principal y texto */
        .stApp {
            background-color: #F4F7F9;
            color: #111827;
        }
        
        /* Barra lateral (Deep Navy) */
        [data-testid="stSidebar"] {
            background-color: #1A2B4C;
        }
        [data-testid="stSidebar"] * {
            color: #E2E8F0 !important;
        }
        
        /* Tarjetas y contenedores (Icy White) */
        .css-1r6slb0, .css-1n76uvr {
            background-color: #FFFFFF;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            padding: 1.5rem;
            border-left: 5px solid #006B6B;
        }

        /* Títulos y encabezados */
        h1, h2, h3 {
            color: #0F172A !important;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
        }
        
        /* Botones (Cool Teal/Emerald) */
        .stButton>button {
            background-color: #006B6B;
            color: white;
            border-radius: 6px;
            border: none;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #004D4D;
            transform: translateY(-2px);
        }
        </style>
    """, unsafe_allow_html=True)

# 3. Función principal de navegación
def main():
    cargar_css()
    
    st.sidebar.title("StudyOS 🧠")
    st.sidebar.markdown("---")
    
    # Menú de navegación
    menu = st.sidebar.radio(
        "Navegación",
        ("🏠 Inicio", "📅 Calendario", "📚 Materias", "📝 Exámenes", "⚡ Sistema de Estudio")
    )
    
    st.sidebar.markdown("---")
    st.sidebar.info("Próximo repaso: Microbiología I") # Placeholder de recordatorio

    # Enrutamiento (Aquí importarías las funciones de la carpeta 'modulos')
    if menu == "🏠 Inicio":
        st.title("Panel de Control")
        st.write("Bienvenido a tu sistema integral de estudio. Aquí verás un resumen de tu semana.")
        
        # Ejemplo de métricas rápidas
        col1, col2, col3 = st.columns(3)
        col1.metric("Tarjetas por repasar hoy", "42", "-5 de ayer")
        col2.metric("Próximo Examen", "12 Días", "Biología Celular")
        col3.metric("Horas de estudio (Semana)", "14.5 h", "+2.1 h")
        
    elif menu == "📅 Calendario":
        st.title("Calendario y Horarios")
        st.write("Interfaz de calendario semanal en construcción...")
        # st.plotly_chart(fig) -> Podrías usar Plotly para diagramas de Gantt o un wrapper de FullCalendar.
        
    elif menu == "📚 Materias":
        st.title("Gestión de Materias")
        st.write("Módulos y apuntes en construcción...")
        
    elif menu == "📝 Exámenes":
        st.title("Cronograma de Exámenes")
        st.write("Timeline de evaluaciones en construcción...")
        
    elif menu == "⚡ Sistema de Estudio":
        st.title("Sistema Inteligente (Active Recall & SRS)")
        st.write("Motor de repetición espaciada en construcción...")

if __name__ == "__main__":
    main()
