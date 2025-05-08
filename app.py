import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="CUMBIA DE LINKEDIN",
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
    .header {
        background: linear-gradient(90deg, #1abc9c, #3498db);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .pulse-animation {
        animation: pulse 2s infinite;
        display: inline-block;
    }
    .verse, .chorus, .bridge {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .verse { background-color: #EAF2F8; }
    .chorus {
        background-color: #D5F5E3;
        border-left: 5px solid #16A085;
    }
    .bridge {
        background-color: #FDEBD0;
        border-left: 5px solid #E67E22;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con efecto
st.markdown("""
<div class="header">
    <h1 style="color: white;"><span class="pulse-animation">🤖🎤</span> Cumbia de Linkedin</h1>
    <p style="color: white; font-size: 1.2em;">Autor: Javier Horacio Pérez Ricárdez</p>
    <p style="color: white; font-size: 1.2em;">Cumbia de Linkedin</p>
</div>
""", unsafe_allow_html=True)

# Columnas para los reproductores
col1, col2 = st.columns(2)

with col1:
    styled_audio_player("cumbia_de_linkedin_a.mp3", "Versión A 🎧", "#3498DB")
    st.image("https://cdn.pixabay.com/photo/2021/08/04/13/06/ai-6521720_640.jpg", 
             use_container_width=True, caption="IA y creatividad humana")

with col2:
    styled_audio_player("cumbia_de_linkedin_b.mp3", "Versión B 🎶", "#9B59B6")
    st.image("https://cdn.pixabay.com/photo/2019/07/14/16/27/network-4337792_640.jpg", 
             use_container_width=True, caption="Tecnología y humanidad")

# Letra de la canción con pestañas
st.markdown("---")
tab1, tab2 = st.tabs(["📜 Letra Completa", "🎤 Karaoke"])

with tab1:
    st.markdown("""
    <div style="background-color: #F9F9F9; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #E74C3C; text-align: center;">🎶 Cumbia del LinkedIn 🎶</h3>

        <div class="verse">
            <h4 style="color: #2980B9;">Verso 1:</h4>
            <p>Ya son las ocho y yo aquí otra vez,<br>
            abro mi LinkedIn con café al revés.<br>
            Foto de perfil, sonrisa profesional,<br>
            pero con mil correos sin contestar.</p>
        </div>

        <div class="chorus">
            <h4 style="color: #16A085;">Coro:</h4>
            <p>¡Muévelo, muévelo, como un CEO!<br>
            Etiqueta al jefe, que esto ya prendió.<br>
            Dale “me gusta” al post del de al lado,<br>
            aunque no sepas bien qué ha publicado.<br><br>
            ¡LinkedIn, LinkedIn, red laboral!<br>
            Aquí todos somos "líderes" sin igual.<br>
            ¡LinkedIn, LinkedIn, puro perfil!<br>
            Con frases motivantes de Brasil a Madrid.</p>
        </div>

        <div class="verse">
            <h4 style="color: #2980B9;">Verso 2:</h4>
            <p>Cien conexiones, dos entrevistas,<br>
            pero nadie me contesta las vistas.<br>
            Yo sigo firme, actualizo el CV,<br>
            aunque la empresa aún no sé si es de fe.</p>
        </div>

        <div class="bridge">
            <h4 style="color: #E67E22;">Puente:</h4>
            <p>¡Atención reclutadores!<br>
            Les bailo esta cumbia con mil honores.<br>
            Tengo experiencia, tengo pasión,<br>
            ¡y en Excel hago hasta reguetón!</p>
        </div>

        <div class="chorus">
            <h4 style="color: #16A085;">Coro:</h4>
            <p>¡Muévelo, muévelo, como un CFO!<br>
            Sube tu diploma, ponle flow.<br>
            Haz un reel con tu productividad,<br>
            aunque en pijama esté la realidad.</p>
        </div>

        <div class="verse">
            <h4 style="color: #2980B9;">Final:</h4>
            <p>¡LinkedIn! Aquí todo es networking,<br>
            hasta con mi ex jefe que me sigue stalkeando.<br>
            ¡Cumbia profesional, viral sin igual,<br>
            para que el algoritmo nos quiera ayudar!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
