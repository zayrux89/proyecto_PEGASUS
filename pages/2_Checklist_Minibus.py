import streamlit as st
from datetime import datetime
from database import insert_checklist
from styles import apply_custom_css

st.set_page_config(page_title="Checklist Minibus", page_icon="🚐", layout="centered")
apply_custom_css()

st.title("🚐 Checklist Diario de Minibus")
st.markdown("Inspección Pre-Uso")

# Opciones estándar
opciones = ["Bueno (B)", "Malo (M)", "No Aplica (NA)"]

with st.form("checklist_form"):
    st.subheader("Datos del Vehículo")
    col1, col2 = st.columns(2)
    with col1:
        patente = st.text_input("Patente")
        conductor = st.text_input("Nombre del Conductor")
    with col2:
        km_inicio = st.number_input("Kilometraje Inicio", min_value=0, step=1)
        km_termino = st.number_input("Kilometraje Término (Opcional)", min_value=0, step=1)
    
    st.markdown("---")
    st.subheader("Inspección de Elementos")
    
    # Acordeones para no saturar la pantalla móvil
    fallas_detectadas = []

    with st.expander("🛑 Vehículo Detenido", expanded=True):
        st.write("Verifique los siguientes elementos:")
        t_escape = st.radio("Tubo de Escape", opciones, horizontal=True)
        asiento = st.radio("Asiento", opciones, horizontal=True)
        bateria = st.radio("Batería", opciones, horizontal=True)
        bocina = st.radio("Bocina", opciones, horizontal=True)
        cinturon = st.radio("Cinturón de Seguridad", opciones, horizontal=True)
        puertas = st.radio("Puertas", opciones, horizontal=True)
        neumaticos = st.radio("Estado de los Neumáticos", opciones, horizontal=True)
        
        elementos_detenidos = {
            "Tubo de Escape": t_escape, "Asiento": asiento, "Batería": bateria,
            "Bocina": bocina, "Cinturón de Seguridad": cinturon, "Puertas": puertas,
            "Neumáticos": neumaticos
        }
        for k, v in elementos_detenidos.items():
            if v == "Malo (M)": fallas_detectadas.append(k)

    with st.expander("🚀 Vehículo Funcionando"):
        aire = st.radio("Aire Acondicionado", opciones, horizontal=True)
        alarma = st.radio("Alarma Retroceso", opciones, horizontal=True)
        direccion = st.radio("Dirección", opciones, horizontal=True)
        embrague = st.radio("Embrague", opciones, horizontal=True)
        f_mano = st.radio("Freno de Mano", opciones, horizontal=True)
        f_pie = st.radio("Freno de Pie", opciones, horizontal=True)
        tablero = st.radio("Instrumentos del Tablero", opciones, horizontal=True)
        
        elementos_func = {
            "Aire Acondicionado": aire, "Alarma Retroceso": alarma, "Dirección": direccion,
            "Embrague": embrague, "Freno de Mano": f_mano, "Freno de Pie": f_pie,
            "Tablero": tablero
        }
        for k, v in elementos_func.items():
            if v == "Malo (M)": fallas_detectadas.append(k)

    with st.expander("📄 Documentos"):
        permiso = st.radio("Permiso de Circulación", opciones, horizontal=True)
        seguro = st.radio("Seguro Obligatorio", opciones, horizontal=True)
        revision = st.radio("Revisión Técnica", opciones, horizontal=True)
        
        documentos = {"Permiso": permiso, "Seguro": seguro, "Revisión Técnica": revision}
        for k, v in documentos.items():
            if v == "Malo (M)": fallas_detectadas.append(k + " (Doc)")

    submitted = st.form_submit_button("Enviar Inspección")

    if submitted:
        if not patente or not conductor:
            st.warning("Debe ingresar la patente y el conductor.")
        else:
            estado_general = "OPERATIVO"
            detalle_fallas = ""
            
            if len(fallas_detectadas) > 0:
                estado_general = "NO OPERATIVO (FALLAS)"
                detalle_fallas = ", ".join(fallas_detectadas)
            
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = (patente, fecha_hora, km_inicio, km_termino, conductor, estado_general, detalle_fallas)
            
            insert_checklist(data)
            
            if estado_general == "NO OPERATIVO (FALLAS)":
                st.error(f"🚨 **VEHÍCULO RECHAZADO.** Se detectaron fallas críticas en: {detalle_fallas}")
            else:
                st.success("✅ Inspección aprobada. Vehículo operativo.")
                
            st.info("Reporte enviado al dashboard PEGASUS.")
