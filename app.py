import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="NO ME REEMPLAZA LA IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar con información del autor
with st.sidebar:
    st.title("Créditos")
    st.markdown("---")
    st.markdown("""
    **Javier Horacio Pérez Ricárdez**  
    """)
    st.markdown("---")

# Función para mostrar audio con estilo
def styled_audio_player(audio_file, title, color):
    try:
        audio_bytes = open(audio_file, "rb").read()
        st.markdown(f"""
        <div style="background: {color}; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: white; text-align: center;">{title}</h3>
            <div style="display: flex; justify-content: center;">
                <audio controls style="width: 100%;">
                    <source src="data:audio/mp3;base64,{base64.b64encode(audio_bytes).decode()}" type="audio/mp3">
                </audio>
            </div>
        </div>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo {audio_file}")

# CSS personalizado
st.markdown("""
<style>
    /* Estilo para el encabezado */
    .header {
        background: linear-gradient(90deg, #1abc9c, #3498db);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Animación para el título */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
        display: inline-block;
    }
    
    /* Estilo para las pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 20px;
        background-color: #E8F8F5;
        border-radius: 10px 10px 0 0;
        font-weight: bold;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #16A085;
        color: white;
    }
    
    /* Estilo para los versos */
    .verse {
        background-color: #EAF2F8;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .chorus {
        background-color: #D5F5E3;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #16A085;
    }
    
    .bridge {
        background-color: #FDEBD0;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #E67E22;
    }
    
    /* Efecto hover para los elementos interactivos */
    .interactive:hover {
        transform: scale(1.02);
        transition: transform 0.3s ease;
    }
    
    /* Estilo para la imagen de información */
    .info-img {
        width: 100%;
        max-width: 400px;
        border-radius: 10px;
        margin: 15px auto;
        display: block;
    }
    
    /* Estilo para el sidebar */
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    
    /* Estilo para el título de secciones */
    .section-title {
        color: #E74C3C;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con efecto
st.markdown("""
<div class="header">
    <h1 style="color: white;"><span class="pulse-animation">🤖🎤</span> No Me Reemplaza la IA</h1>
    <p style="color: white; font-size: 1.2em;">Autor: Javier Horacio Pérez Ricárdez</p>
    <p style="color: white; font-size: 1.2em;">El RAP de la era digital</p>
</div>
""", unsafe_allow_html=True)

# Columnas para los reproductores
col1, col2 = st.columns(2)

with col1:
    styled_audio_player("NO_ME_REEMPLAZA_IA_a.mp3", "Versión A 🎧", "#3498DB")
    st.image("https://cdn.pixabay.com/photo/2021/08/04/13/06/ai-6521720_640.jpg", 
            use_container_width=True, caption="IA y creatividad humana")

with col2:
    styled_audio_player("NO_ME_REEMPLAZA_IA_b.mp3", "Versión B 🎶", "#9B59B6")
    st.image("https://cdn.pixabay.com/photo/2019/07/14/16/27/network-4337792_640.jpg", 
            use_container_width=True, caption="Tecnología y humanidad")

# Letra de la canción con pestañas
st.markdown("---")
tab1, tab2 = st.tabs(["📜 Letra Completa", "🎤 Karaoke"])

with tab1:
    st.markdown("""
    <div style="background-color: #F9F9F9; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #E74C3C; text-align: center;">No Me Reemplaza la IA</h3>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 1:</h4>
            <p>Yeah, dicen que la IA viene pa' quitar,<br>
            los empleos, los sueños, nos quiere desplazar.<br>
            Miro al futuro con duda y ansiedad,<br>
            pero el miedo no sirve, mejor es innovar.<br><br>
            Máquinas piensan, algoritmos hablan,<br>
            pero el corazón humano no se programa.<br>
            No tienen alma, no tienen pasión,<br>
            pueden aprender, pero sin compasión.</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Estribillo:</h4>
            <p>No me reemplaza la IA, no señor,<br>
            tengo visión, tengo flow, tengo amor.<br>
            Si cambia el mundo, yo cambio también,<br>
            aprendo, me adapto, renazco en el tren.<br><br>
            No me reemplaza la IA, yo sigo aquí,<br>
            con mente afilada y ganas de seguir.<br>
            Ella asiste, pero yo soy el actor,<br>
            el que crea, el que siente, el que da el valor.</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 2:</h4>
            <p>Cajeros se van, traductores igual,<br>
            pero surgen carreras del mundo digital.<br>
            Data science, machine learning, codear,<br>
            yo me entreno y me empiezo a programar.<br><br>
            No es enemigo, es solo evolución,<br>
            como el vapor, la rueda o el motor.<br>
            La clave es la mente en transformación,<br>
            educación con determinación.</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Estribillo (Repetición):</h4>
            <p>No me reemplaza la IA, no señor,<br>
            tengo visión, tengo flow, tengo amor.<br>
            Si cambia el mundo, yo cambio también,<br>
            aprendo, me adapto, renazco en el tren.<br><br>
            No me reemplaza la IA, yo sigo aquí,<br>
            con mente afilada y ganas de seguir.<br>
            Ella asiste, pero yo soy el actor,<br>
            el que crea, el que siente, el que da el valor.</p>
        </div>
        
        <div class="bridge">
            <h4 style="color: #E67E22;">Puente:</h4>
            <p>No temas al cambio, teme quedarte atrás,<br>
            la era digital solo quiere más.<br>
            De pensamiento, de corazón,<br>
            humano con IA: ¡combinación!</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso Final:</h4>
            <p>Así que levántate, ponte a estudiar,<br>
            el futuro es tuyo, empieza a innovar.<br>
            La IA no quita, transforma el papel,<br>
            y tú decides si vas a subirte en el tren.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h3 style="color: #E74C3C;">🎤 Karaoke Time! 🎤</h3>
        <p>¡Sigue la letra mientras suena la música!</p>
        <div style="height: 10px;"></div>
        <img src="https://cdn.pixabay.com/photo/2020/04/12/01/58/microphone-5032177_640.jpg" style="width: 100%; max-width: 400px; border-radius: 10px;" class="interactive">
    </div>
    """, unsafe_allow_html=True)
    
    # Simulador de karaoke con colores que cambian
    lyrics = [
        ("Yeah, dicen que la IA viene pa' quitar,", "#3498DB", "verse"),
        ("los empleos, los sueños, nos quiere desplazar.", "#3498DB", "verse"),
        ("Miro al futuro con duda y ansiedad,", "#3498DB", "verse"),
        ("pero el miedo no sirve, mejor es innovar.", "#3498DB", "verse"),
        ("", "", ""),
        ("Máquinas piensan, algoritmos hablan,", "#3498DB", "verse"),
        ("pero el corazón humano no se programa.", "#3498DB", "verse"),
        ("No tienen alma, no tienen pasión,", "#3498DB", "verse"),
        ("pueden aprender, pero sin compasión.", "#3498DB", "verse"),
        ("", "", ""),
        ("No me reemplaza la IA, no señor,", "#16A085", "chorus"),
        ("tengo visión, tengo flow, tengo amor.", "#16A085", "chorus"),
        ("Si cambia el mundo, yo cambio también,", "#16A085", "chorus"),
        ("aprendo, me adapto, renazco en el tren.", "#16A085", "chorus"),
        ("", "", ""),
        ("No me reemplaza la IA, yo sigo aquí,", "#16A085", "chorus"),
        ("con mente afilada y ganas de seguir.", "#16A085", "chorus"),
        ("Ella asiste, pero yo soy el actor,", "#16A085", "chorus"),
        ("el que crea, el que siente, el que da el valor.", "#16A085", "chorus"),
    ]
    
    for line, color, line_type in lyrics:
        if line:
            if line_type == "chorus":
                st.markdown(f'<div class="chorus" style="padding: 10px; margin: 5px 0;"><p style="font-size: 20px; color: {color}; text-align: center;">{line}</p></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<p style="font-size: 18px; color: {color}; text-align: center;">{line}</p>', unsafe_allow_html=True)
        else:
            st.write("")

# Sección de información adicional
st.markdown("---")
expander = st.expander("ℹ️ Sobre la IA y el futuro del trabajo")
with expander:
    st.markdown("""
    <div style="background-color: #F0F2F6; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2980B9;">IA y empleo: ¿Amenaza u oportunidad?</h3>
        <p>La Inteligencia Artificial está transformando el mundo laboral:</p>
        <ul>
            <li>🤖 Automatiza tareas repetitivas</li>
            <li>💡 Crea nuevas oportunidades laborales</li>
            <li>📚 Exige actualización constante de habilidades</li>
            <li>🤝 Mejora la productividad humana</li>
        </ul>
        <p>Como dice el RAP: "No es enemigo, es solo evolución"</p>
        <img class="info-img" src="https://cdn.pixabay.com/photo/2019/12/14/08/36/artificial-intelligence-4694899_640.jpg" alt="IA y humanos trabajando juntos">
        
        <h4 style="color: #E67E22; margin-top: 20px;">Habilidades que la IA no puede reemplazar:</h4>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin: 15px 0;">
            <div style="background: #D5F5E3; padding: 10px; border-radius: 8px; width: 120px; text-align: center;">Creatividad</div>
            <div style="background: #D5F5E3; padding: 10px; border-radius: 8px; width: 120px; text-align: center;">Empatía</div>
            <div style="background: #D5F5E3; padding: 10px; border-radius: 8px; width: 120px; text-align: center;">Liderazgo</div>
            <div style="background: #D5F5E3; padding: 10px; border-radius: 8px; width: 120px; text-align: center;">Innovación</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Efectos visuales
st.balloons()
