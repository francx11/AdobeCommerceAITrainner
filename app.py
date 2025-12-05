import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Entrenador Adobe Commerce",
    page_icon="🧠",
    layout="wide"
)

# Título principal
st.title("Entrenador Adobe Commerce Developer Professional 🧠")

st.write("""
Bienvenido/a a tu entrenador para la certificación **Adobe Commerce Developer Professional**.

De momento esta es solo una maqueta inicial.  
Vamos a ir paso a paso añadiendo funcionalidades.
""")

# Barra lateral con modos
st.sidebar.header("Modo")
mode = st.sidebar.radio(
    "Elige modo",
    ["Chat tutor", "Simulador de examen (WIP)"]
)

if mode == "Chat tutor":
    st.subheader("Chat tutor (versión inicial)")
    user_input = st.text_area("Escribe aquí tu pregunta sobre Adobe Commerce o la certificación:")

    if st.button("Preguntar"):
        if user_input.strip():
            st.write("🔜 Aquí aparecerá la respuesta inteligente del tutor (por ahora es un placeholder).")
            st.write(f"Tu pregunta fue: **{user_input}**")
        else:
            st.warning("Por favor, escribe una pregunta antes de pulsar 'Preguntar'.")

else:
    st.subheader("Simulador de examen (en construcción)")
    st.info("Pronto podrás hacer tests tipo examen aquí. De momento solo es texto informativo.")
