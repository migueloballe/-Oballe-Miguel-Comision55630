Comisión: 55630
Alumno: Miguel Oballe

Descripción
Este proyecto Django se encarga de manejar servicios, contrataciones, y contiene páginas para inicio, contacto y contratación de servicios para una empresa de Enfermería/Cuidadores

Modelos
Persona: Representa a una persona con campos como nombre, dirección, teléfono y correo.
Servicio: Describe los servicios disponibles, incluyendo el nombre, descripción, costo, duración y otros detalles.
Contrato: Define un contrato entre una persona y un servicio, con detalles como la fecha y condiciones.

Vistas
home: Renderiza la página de inicio.
contacto: Renderiza la página de contacto.
servicios: Muestra todos los servicios disponibles y permite buscar servicios por nombre.
contratacion: Maneja la contratación de un servicio, incluyendo el proceso de validación del formulario.

Formularios
Cliente_Nuevo: Formulario utilizado en la vista de contratación para capturar detalles de la persona y el servicio que desea contratar.

Instalación
Clona el repositorio.
Instala las dependencias utilizando pip:
pip install -r requirements.txt

Realiza las migraciones:
python manage.py migrate

Ejecuta el servidor:
python manage.py runserver

Uso
Navega a http://localhost:8000 para acceder al sitio.
/: Página de inicio.
/servicios/: Ver y buscar servicios.
/contratacion/: Contratar un servicio.
/contacto/: Página de contacto.