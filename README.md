
# 🚀 Gestión de Consultas Bot

![Python](https://img.shields.io/badge/Python-3.12-blue.svg?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.1-green.svg?logo=django&logoColor=white)
![Airtable](https://img.shields.io/badge/Airtable-API-orange.svg?logo=airtable&logoColor=white)
![Voiceflow](https://img.shields.io/badge/Voiceflow-Bot-yellow.svg?logo=voiceflow&logoColor=white)
![Make](https://img.shields.io/badge/Make-Integration-red.svg?logo=make&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

<p align="center">
  <img src="https://your-image-url.com/illustration.png" alt="Gestión de Consultas Bot" width="600"/>
</p>

## 📝 Descripción

**Gestión de Consultas Bot** es un sistema integral diseñado para gestionar las consultas de servicios de plomería. Desarrollado con **Django**, este sistema se conecta con **Airtable** para manejar los datos de las consultas, integrando a la vez un bot de **Voiceflow** que automatiza la interacción con los clientes. Además, **Make** se encarga de la automatización de tareas clave, garantizando un flujo de trabajo eficiente y sin complicaciones.

## 🔍 Características Principales

- **📊 Gestión Eficiente de Consultas**: Registra, rastrea y actualiza el estado de todas las consultas recibidas de manera centralizada.
- **🔗 Integración con Airtable**: Utiliza Airtable como base de datos para almacenar y gestionar la información de las consultas.
- **🤖 Bot de Voiceflow**: Automatiza la interacción con los clientes a través de comandos de voz o texto, permitiendo registrar nuevas solicitudes de servicio.
- **🔄 Automatización con Make**: Automatiza flujos de trabajo como la actualización del estado de las consultas y las notificaciones a los clientes.
- **🌐 Interfaz Web Moderna**: Una interfaz limpia y accesible donde los administradores pueden ver y actualizar las consultas fácilmente.

## 🛠️ Instalación y Configuración

Sigue estos pasos para configurar el proyecto localmente:

1. **Clona el Repositorio:**

   ```bash
   git clone https://github.com/ferc33/gestion-bot.git
   ```

2. **Navega al Directorio del Proyecto:**

   ```bash
   cd gestion-bot
   ```

3. **Crea y Activa un Entorno Virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

4. **Instala las Dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configura las Variables de Entorno:**

   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```bash
   AIRTABLE_API_KEY="tu_api_key"
   AIRTABLE_BASE_ID="tu_base_id"
   ```

6. **Aplica las Migraciones de la Base de Datos:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Inicia el Servidor de Desarrollo:**

   ```bash
   python manage.py runserver
   ```

8. **Accede al Sistema:**

   Abre tu navegador y dirígete a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver el sistema en acción.

## 🤖 Integración con Voiceflow

El bot de Voiceflow integrado permite una interacción fluida con los clientes mediante mensajes de texto. Los usuarios pueden registrar solicitudes de servicio, hacer consultas y recibir actualizaciones automáticas sobre el estado de sus pedidos.

<p align="center">
  <img src="" alt="Voiceflow Integration" width="600"/>
</p>

## 🔧 Automatización con Make

**Make** se encarga de la automatización de tareas backend cruciales, como la actualización de estados de las consultas y el envío de notificaciones automáticas a los clientes, optimizando así el flujo de trabajo sin necesidad de intervención manual.

<p align="center">
  <img src="" alt="Make Automation" width="600"/>
</p>

## 📊 Características Adicionales

- **🔒 Autenticación de Usuarios**: Sistema de autenticación para proteger el acceso a la interfaz de administración.
- **📈 Reportes Detallados**: Genera reportes de todas las consultas gestionadas en el sistema.
- **📲 Notificaciones Automatizadas**: Envía notificaciones automáticas a los clientes cuando cambia el estado de su consulta.

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT). 

---

<p align="center">
  <b>Desarrollado con 💻 y ☕ por Fer y Lucy</b>
</p>

<p align="center">
  <a href="https://github.com/tu-usuario/gestion-bot/issues">Reportar un problema</a> |
  <a href="https://github.com/tu-usuario/gestion-bot/pulls">Enviar una mejora</a>
</p>
