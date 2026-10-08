import streamlit as st
from datetime import datetime
from database import insert_fatiga
from styles import apply_custom_css

# Configuración de página
st.set_page_config(page_title="Formulario Fatiga", page_icon="😴", layout="centered")

# Aplicar Diseño
apply_custom_css()

st.title("😴 Encuesta de Fatiga y Somnolencia")
st.markdown("Gestión de Alerta Temprana")

with st.form("fatiga_form"):
    st.subheader("Datos Generales")
    conductor = st.text_input("Nombre del Conductor")
    area_cargo = st.text_input("Área y Cargo")
    supervisor = st.text_input("Nombre del Supervisor")
    
    st.subheader("Cuestionario de Evaluación")
    st.markdown("*(Durante las últimas semanas)*")
    
    q1 = st.radio("1. ¿Ha tenido dificultades para lograr un descanso reparador?", ["No", "Sí"], horizontal=True)
    q2 = st.radio("2. ¿Presenta algún evento(s) que dificulte(n) su buen dormir?", ["No", "Sí"], horizontal=True)
    q3 = st.radio("3. ¿Ha sufrido insomnio?", ["No", "Sí"], horizontal=True)
    q4 = st.radio("4. ¿Duerme menos tiempo del necesario (Menos de 5.5 horas)?", ["No", "Sí"], horizontal=True)
    
    st.markdown("---")
    st.markdown("**Preguntas Críticas**")
    q5 = st.radio("5. ¿Está consumiendo algún medicamento que provoque somnolencia?", ["No", "Sí"], horizontal=True)
    q6 = st.radio("6. ¿Padece alguna enfermedad no tratada que pudiese causar somnolencia?", ["No", "Sí"], horizontal=True)
    st.markdown("---")

    q7 = st.radio("7. ¿Existen factores externos que afecten la calidad de su sueño?", ["No", "Sí"], horizontal=True)
    q8 = st.radio("8. ¿Ha presentado eventos importantes de somnolencia?", ["No", "Sí"], horizontal=True)
    q9 = st.radio("9. ¿Ha tenido algún problema de que disminuya su estado de alerta?", ["No", "Sí"], horizontal=True)
    q10 = st.radio("10. ¿Ha consumido alcohol antes de iniciar el servicio?", ["No", "Sí"], horizontal=True)
    q11 = st.radio("11. ¿Ha consumido drogas antes de iniciar el servicio?", ["No", "Sí"], horizontal=True)
    
    submitted = st.form_submit_button("Enviar Evaluación")

    if submitted:
        if not conductor or not supervisor:
            st.warning("Por favor, ingrese el nombre del conductor y del supervisor.")
        else:
            # Lógica de Alerta Inmediata (MVP)
            estado_alerta = "APTO"
            alerta_inmediata = False
            
            if q5 == "Sí" or q6 == "Sí" or q10 == "Sí" or q11 == "Sí":
                estado_alerta = "PELIGRO - NO APTO"
                alerta_inmediata = True
            
            # Guardar en Base de Datos
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = (
                conductor, fecha_hora, area_cargo,
                q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
                estado_alerta, supervisor
            )
            insert_fatiga(data)
            
            # Mostrar resultado visual
            if alerta_inmediata:
                st.error("🚨 **ALERTA CRÍTICA: CONDUCTOR NO APTO PARA OPERAR.** Se requiere derivación a chequeo médico inmediato según protocolo.")
            else:
                st.success(f"✅ Encuesta registrada correctamente. Conductor APTO.")
                
            st.info("El registro ha sido enviado al centro de alertas de PEGASUS.")
