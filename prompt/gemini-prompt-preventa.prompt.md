# 📋 PROMPT MAESTRO DEFINITIVO PARA DEMO DE PREVENTA

**Actúa como un Arquitecto de Software Senior con IA, Desarrollador Full-Stack (Python/Web), Experto en Soluciones Cloud y Consultor Técnico de Preventa.**

Necesito diseñar y construir una **demo funcional, rápida (1 a 3 días de desarrollo) y 100% gratuita** para mostrarle a un cliente cómo podemos digitalizar y automatizar dos procesos operativos que actualmente maneja de forma manual. 

El objetivo principal es **atraer al cliente, validar la idea y demostrar valor en cualquier dispositivo (PC, tablet o móvil)**, no construir el sistema empresarial definitivo todavía.

#### 1. Documentos de referencia y Procesos
Analiza y utiliza como base los siguientes documentos para la automatización:
*   **"somnolencia (2)-convertido.docx"**: Encuesta de "Gestión de Alerta Temprana" (11 preguntas de Sí/No) que aplica el supervisor al conductor, con criterios automáticos para derivación a chequeo médico.
*   **"CHECK LIST MINI BUS V.01 PEGASUS (5).xlsx"**: Lista de inspección diaria del vehículo (elementos detenidos/funcionando, documentos, kilometraje, firmas).

*Nota: Identifica qué datos, validaciones y alertas se pueden automatizar de estos documentos sin inventar requisitos extra.*

#### 2. Restricciones y Entorno
*   **Costo Cero Absoluto:** Solo herramientas, librerías y *free tiers* (capas gratuitas) sin necesidad de ingresar tarjeta de crédito ni riesgo de cobros sorpresa. No uses servicios de pago de AWS.
*   **Accesibilidad (Local + Nube):** La solución debe poder ejecutarse en mi entorno local, pero **obligatoriamente** debe tener una opción de despliegue gratuito en la nube (ej. Streamlit Community Cloud, Render, Vercel, Railway, etc.) para que el cliente pueda acceder a la demo desde su celular o computador a través de una URL.
*   **Entorno de Desarrollo Local:** Windows con WSL2, Docker, VS Code, GitHub.

#### 3. Formato de Respuesta esperado (Metodología SPEC / SDD)
Quiero que estructures tu respuesta utilizando un enfoque de **Software Design Document (SDD)** ligero, orientado a preventa. Tu respuesta debe contener exactamente las siguientes secciones:

**I. Análisis de Requisitos y Lógica de Negocio**
*   Resumen de qué datos y reglas de negocio exactas se digitalizarán por cada documento (ej. criterios de derivación médica y validación del checklist).

**II. Comparativa de Alternativas y Recomendación Arquitectónica**
*   Presenta 2-3 alternativas viables de *stack* tecnológico que cumplan el costo cero y el acceso web público (ej. *Streamlit + SQLite integrado*, *FastAPI + HTML/JS + Render*, etc.).
*   Indica pros/contras, dificultad y tiempo de implementación.
*   **Elige tu recomendación principal** detallando por qué es la más rápida y segura.

**III. Diseño de la Solución (Arquitectura)**
*   Esquema de arquitectura simple de la opción ganadora (Frontend, Backend, Persistencia de datos local/cloud, Hosting).
*   Estructura de directorios y archivos recomendada para el proyecto.

**IV. Alcance del MVP (Funcionalidades de la Demo)**
*   Módulo 1: Formulario digital de Fatiga y Somnolencia con alerta visual automática.
*   Módulo 2: Formulario digital del Checklist Mini Bus.
*   Panel/Dashboard simple para ver registros consolidados.

**V. Plan de Implementación Paso a Paso (Para el Desarrollador)**
*   Pasos exactos a seguir asumiendo que tengo WSL2, Docker y VS Code.
*   Creación de entorno, dependencias a instalar, y codificación clave.
*   Paso a paso exacto para desplegarlo en la nube gratis y obtener la URL para el cliente.

**VI. Estrategia de Preventa**
*   Qué problema operativo concreto le vamos a demostrar al cliente que estamos resolviendo.
*   Qué beneficios (reducción de papel, alertas en tiempo real) enfatizar al mostrar la demo.

**VII. Roadmap de Evolución (Fase 2 - Post Venta)**
*   Qué cambiaría en la arquitectura si el cliente compra la solución (ej. paso a PostgreSQL, AWS Cognito para usuarios, backend robusto con FastAPI/Django, roles, firmas digitales). 
*   Cómo estructurar el código *hoy* para que no sea un dolor de cabeza escalarlo *mañana*.

***

### 💡 Consejo extra como Arquitecto de Software:
Para este caso en particular, la tecnología que mejor encaja con tus requerimientos (Rápido, 100% Gratuito, Local + Nube instantánea, Python) es **Streamlit**. 
Te permitirá tomar las lógicas del Excel y el Word, crear formularios web bonitos con Python en horas, y lo puedes desplegar gratis en **Streamlit Community Cloud** (directamente conectado a tu GitHub) para enviarle un link al cliente que podrá abrir desde su móvil sin gastar $1 dólar ni configurar servidores complejos.