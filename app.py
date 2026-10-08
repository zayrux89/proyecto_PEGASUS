import streamlit as st
import pandas as pd
import plotly.express as px
from database import init_db, get_fatiga_data, get_checklist_data
from styles import apply_custom_css

# Configuración de página principal
st.set_page_config(
    page_title="PEGASUS - Centro de Alertas",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar Base de Datos (SQLite)
init_db()

# Aplicar Diseño Premium
apply_custom_css()

# --- Header ---
st.title("🦅 PEGASUS: Centro de Control Operativo")
st.markdown("Monitor de Alertas Tempranas en Tiempo Real.")

# --- Obtener Datos ---
df_fatiga = get_fatiga_data()
df_checklist = get_checklist_data()

# --- KPIs y Métricas ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Encuestas de Fatiga (Hoy)", value=len(df_fatiga) if not df_fatiga.empty else 0)

with col2:
    st.metric(label="Checklist Vehículos (Hoy)", value=len(df_checklist) if not df_checklist.empty else 0)

with col3:
    # Contar cuántas alertas hay (Estado de Alerta == 'PELIGRO - NO APTO')
    if not df_fatiga.empty:
        alertas_activas = len(df_fatiga[df_fatiga["estado_alerta"] == "PELIGRO - NO APTO"])
    else:
        alertas_activas = 0
    st.metric(label="🔴 Alertas Activas", value=alertas_activas)

st.markdown("---")

# --- Dashboards Visuales ---
col_dash1, col_dash2 = st.columns(2)

with col_dash1:
    st.subheader("Estado de Conductores")
    if not df_fatiga.empty:
        fig_fatiga = px.pie(df_fatiga, names="estado_alerta", color="estado_alerta", 
                            color_discrete_map={"APTO": "#10B981", "PELIGRO - NO APTO": "#EF4444"},
                            hole=0.4)
        fig_fatiga.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#E2E8F0")
        st.plotly_chart(fig_fatiga, use_container_width=True)
    else:
        st.info("No hay datos de fatiga registrados aún.")

with col_dash2:
    st.subheader("Estado de Flota (Vehículos)")
    if not df_checklist.empty:
        fig_check = px.bar(df_checklist, x="patente", color="estado_general", 
                           color_discrete_map={"OPERATIVO": "#10B981", "NO OPERATIVO (FALLAS)": "#EF4444"})
        fig_check.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#E2E8F0")
        st.plotly_chart(fig_check, use_container_width=True)
    else:
        st.info("No hay checklists registrados aún.")

st.markdown("---")

# --- Tablas de Últimos Registros ---
st.subheader("Últimas Alertas Recibidas")

tab1, tab2 = st.tabs(["🚦 Alertas de Fatiga", "🚐 Reportes de Vehículos"])

with tab1:
    if not df_fatiga.empty:
        st.dataframe(df_fatiga[["fecha_hora", "conductor", "estado_alerta", "supervisor"]].head(10), use_container_width=True)
    else:
        st.write("Sin registros.")

with tab2:
    if not df_checklist.empty:
        st.dataframe(df_checklist[["fecha_hora", "patente", "estado_general", "conductor", "detalle_fallas"]].head(10), use_container_width=True)
    else:
        st.write("Sin registros.")

st.sidebar.markdown("### Navegación")
st.sidebar.info("Usa el menú superior para ir a los formularios de ingreso de datos.")
