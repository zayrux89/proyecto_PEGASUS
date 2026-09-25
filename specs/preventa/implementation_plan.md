# Documento de Diseño de Software (SDD) - Demo Preventa PEGASUS

Este documento define la arquitectura, alcance y plan de implementación para la demo funcional requerida, diseñada para mostrar al cliente cómo digitalizar y automatizar los procesos de "Gestión de Alerta Temprana (Fatiga y Somnolencia)" y el "Checklist de Minibus".

## I. Análisis de Requisitos y Lógica de Negocio

### 1. Encuesta de Fatiga y Somnolencia (Gestión de Alerta Temprana)
*   **Datos a capturar:** Nombre del conductor, fecha, área/cargo y 11 preguntas de Sí/No sobre calidad de sueño, insomnio, factores externos, etc.
*   **Reglas de Negocio (Alertas Automáticas):**
    *   Derivación a chequeo médico inmediata si la respuesta es "Sí" en la Pregunta 5 (consumo de medicamentos que provoquen somnolencia) o la Pregunta 6 (enfermedades no tratadas que causan somnolencia).
    *   *Nota MVP:* Para la demo, se implementará la alerta inmediata basada en las preguntas 5 y 6. El tracking histórico (3 eventos en un turno, 2 días consecutivos) se simulará o registrará para mostrarse en el dashboard.

### 2. Checklist Diario Mini Bus
*   **Datos a capturar:** Patente, Fecha, Kilometraje (Inicio/Término), Nombre de Conductor.
*   **Categorías de Inspección:** Vehículo Detenido, Vehículo Funcionando, Accesorios, Documentos, Mantenciones.
*   **Reglas de Negocio:**
    *   Cada elemento se evalúa como B (Bueno), M (Malo) o NA (No Aplica).
    *   Cualquier elemento crítico marcado como "Malo" (ej. Frenos, Dirección, Luces) debe generar una alerta visual (rojo) indicando que el vehículo no está apto para operar.

## II. Comparativa de Alternativas y Recomendación Arquitectónica

Para cumplir con la restricción de **Costo Cero Absoluto** y accesibilidad desde cualquier dispositivo (Local + Nube), se evaluaron las siguientes opciones:

1.  **FastAPI + HTML/JS/CSS (Vanilla) + Render (Cloud):** 
    *   *Pros:* Separación limpia de Backend y Frontend.
    *   *Contras:* Mayor tiempo de desarrollo (2 proyectos distintos), Render free tier entra en "sleep mode" y tarda 50s en despertar.
2.  **Next.js + Vercel + Supabase (Free tier):**
    *   *Pros:* Altamente escalable, diseño muy premium.
    *   *Contras:* Curva de desarrollo un poco más larga para un MVP de 1-3 días, requiere configurar la DB en la nube.
3.  **Streamlit + SQLite integrado + Streamlit Community Cloud (RECOMENDADO):**
    *   *Pros:* Desarrollo ultra rápido (Python 100%), UI interactiva y adaptativa para móviles construida automáticamente, despliegue gratuito con 1 click desde GitHub sin sleep mode agresivo.
    *   *Contras:* Menor personalización extrema de diseño (CSS limitado), pero suficiente para una demo "Wow".

**Recomendación:** Opción 3 (**Streamlit**). Nos permite enfocarnos en la lógica de negocio y tener los formularios listos y operando en la web en horas, cumpliendo al 100% el costo cero y la demostración de valor inmediata.

## III. Diseño de la Solución (Arquitectura)

*   **Frontend & Backend:** Streamlit (Framework Python).
*   **Persistencia de Datos:** SQLite (Base de datos local en archivo `.db`, perfecta para el MVP).
*   **Hosting:** Streamlit Community Cloud conectado al repositorio de GitHub.
*   **Estructura del Proyecto:**
    ```text
    /proyecto_PEGASUS
    ├── app.py                  # Dashboard Principal consolidado
    ├── pages/
    │   ├── 1_Formulario_Fatiga.py
    │   └── 2_Checklist_Minibus.py
    ├── database.py             # Lógica de conexión SQLite y CRUD
    ├── requirements.txt        # Dependencias (streamlit, pandas, etc.)
    └── .gitignore
    ```

## IV. Alcance del MVP (Funcionalidades de la Demo)

1.  **Módulo 1: Formulario de Fatiga y Somnolencia**
    *   Interfaz web responsive con las 11 preguntas.
    *   Validación en tiempo real que muestre un *Banner Rojo* (Alerta) si marca Sí en las preguntas críticas (5 o 6), bloqueando la aprobación.
2.  **Módulo 2: Checklist Minibus**
    *   Formulario organizado en acordeones (Expanders) por categoría para no saturar la pantalla móvil.
    *   Selectores visuales (Radio buttons: Bueno, Malo, N/A).
3.  **Panel de Control (Dashboard)**
    *   Vista gerencial/supervisor mostrando total de encuestas del día, vehículos observados y alertas activas.

## V. Plan de Implementación Paso a Paso (Para el Desarrollador)

1.  **Configuración del Entorno:**
    *   En WSL2/VS Code, usar el entorno virtual `.venv` y asegurar la instalación de `streamlit`, `pandas`, `plotly` y `sqlalchemy`.
2.  **Desarrollo de la Base de Datos:**
    *   Crear `database.py` para auto-inicializar las tablas `fatiga_logs` y `checklist_logs` en un archivo `pegasus_demo.db`.
3.  **Desarrollo de Vistas:**
    *   Codificar `app.py` como punto de entrada y dashboard.
    *   Codificar los formularios en la carpeta `pages/`.
4.  **Pruebas Locales:**
    *   Ejecutar `streamlit run app.py` y probar la carga de datos.
5.  **Despliegue a la Nube (Gratis):**
    *   Subir el código a un repositorio público de GitHub.
    *   Crear cuenta gratuita en Streamlit Community Cloud (share.streamlit.io).
    *   Conectar el repo y desplegar `app.py`. Obtener la URL pública para el cliente.

## VI. Estrategia de Preventa

*   **Problema a resolver:** El cliente usa papel (Excel/Word impresos), lo que genera demora en tabular datos, pérdida de historial y, lo más crítico, *reacción tardía* ante un conductor con fatiga o un bus con fallas.
*   **Beneficios a enfatizar en la demo:** 
    *   **Inmediatez:** El supervisor ve la alerta roja en su pantalla al instante.
    *   **Trazabilidad:** Los datos no se pierden en una carpeta, están en un dashboard en vivo.
    *   **Cero fricción:** El conductor/supervisor solo necesita el link en su celular (código QR), sin instalar apps.

## VII. Roadmap de Evolución (Fase 2 - Post Venta)

Si el cliente aprueba la demo y compra la solución definitiva, la arquitectura debe evolucionar para soportar concurrencia y seguridad empresarial:

1.  **Base de Datos:** Migrar de SQLite a **PostgreSQL** (AWS RDS o Supabase) para soportar múltiples usuarios concurrentes.
2.  **Backend:** Separar la lógica a una API REST con **FastAPI** o **Django REST Framework**.
3.  **Frontend:** Re-escribir en **Next.js** o **React** para crear una PWA (Progressive Web App) con capacidades offline (por si hay mala señal en terreno).
4.  **Seguridad:** Implementar Autenticación (JWT, Auth0 o AWS Cognito) para roles (Conductor, Supervisor, Gerente) y firmas digitales (Touch en pantalla).

> [!IMPORTANT]
> **Revisión del Usuario Requerida**
> Por favor, revisa el plan presentado en este documento. Si estás de acuerdo con usar **Streamlit y SQLite** para este MVP de 1 a 3 días, procederemos inmediatamente con la creación de la estructura del proyecto y la codificación de los formularios. ¿Apruebas este enfoque?
