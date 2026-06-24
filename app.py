import streamlit as st

from secret_santa_logic.email_send import send_email
from secret_santa_logic.logic_asignment import asignment

# Aquí importarás tus funciones lógicas existentes
# from secret_santa_logic.logic_asignment import asignar_amigos_secretos
# from secret_santa_logic.email_send import enviar_correos

st.title("🎄 Generador de Secret Santa")

# 1. Inicializar la lista de participantes en la memoria de la app
if "participantes" not in st.session_state:
    st.session_state.participantes = []

# 2. Formulario para agregar una nueva persona
st.subheader("Agregar Participante")
with st.form("form_agregar", clear_on_submit=True):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo Electrónico")
    boton_agregar = st.form_submit_button("Añadir a la lista")

    if boton_agregar:
        if nombre and correo:
            # Guardamos como diccionario en nuestra lista en memoria
            st.session_state.participantes.append({"nombre": nombre, "correo": correo})
            st.success(f"¡{nombre} añadido con éxito!")
        else:
            st.error("Por favor, llena ambos campos.")

# 3. Mostrar la lista actual de participantes

st.subheader("Lista de Participantes")
if st.session_state.participantes:
    # Mostramos una tabla limpia con los datos acumulados
    st.table(st.session_state.participantes)

    # Botón para reiniciar la lista si es necesario
    if st.button("Limpiar lista"):
        st.session_state.participantes = []
        st.rerun()
else:
    st.info("Aún no hay participantes en la lista.")

# 4. Botón de acción masiva
st.subheader("¡Detonar Secret Santa!")
if len(st.session_state.participantes) >= 3:
    if st.button("Asignar y Enviar Correos", type="primary"):
        with st.spinner("Realizando el sorteo..."):

            # 1. Transformamos la lista de Streamlit: [{"nombre": "Ana", "correo": "ana@..."}, ...]
            #    en el diccionario que tu función espera: {"Ana": "ana@...", ...}
            personas_dict = {
                p["nombre"]: p["correo"] for p in st.session_state.participantes
            }

            # 2. Llamamos a tu función original pasándole este nuevo diccionario
            parejas_asignadas = asignment(personas_dict)

            # 3. Ahora 'parejas_asignadas' tendrá la estructura: {"Ana": "Carlos", "Carlos": "Luis", ...}
            #    Ya puedes pasárselo a tu lógica de correos para que envíe los mensajes.
            send_email(parejas_asignadas, personas_dict)
            st.success("🎉 ¡Correos enviados con éxito!")
else:
    st.warning("Necesitas al menos 3 participantes para realizar el sorteo.")
