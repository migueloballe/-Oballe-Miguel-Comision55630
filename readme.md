# **Proyecto de Gestión de Contratos y Servicios de Salud**

Descripción
Este es un proyecto Django que ayuda en la gestión de contratos y servicios de salud. Incluye funcionalidades para manejar pacientes, enfermeros, y distintos servicios ofrecidos. 

Modelos
Persona: Representa a cualquier cliente en el sistema. 
Servicio: Detalla un servicio médico o tratamiento que se ofrece.
Enfermero: Subclase de Persona que agrega detalles específicos sobre enfermeros.
Contrato: Asocia un paciente con un servicio y un enfermero.
Avatar: Almacena imágenes de perfil para los usuarios.

Vistas
home: Página de inicio.
contacto: Página acerca de mi. 
servicios: Lista todos los servicios disponibles.
contratacion: Formulario para contratar un servicio.
Nuevo_enfermero: Formulario para registrarse como enfermero y se considero en la bolsa de trabajado de busquedas.
registro: Formulario de registro para nuevos coordinadores. Los coordinadores tendran un abm de los modelos persona,servicio, enfermero y contrato y podrán
asociar enfermeros , clientes con un contrato en especifico. 
login_request: Maneja la autenticación de usuario.
editarPerfilYAvatar: Permite al usuario editar su perfil y avatar.

URL Patterns
* /: Home.
* /servicios/: Lista de servicios.
* /contratacion/: Formulario de contratación.
* /contacto/: Página de contacto.
* /registro/: Página de registro.
* /enfermero/: Página para agregar un nuevo enfermero.
* /login/: Página de login.
* /logout/: Página de logout.
* /editar_perfil/: Página para editar perfil y avatar.
* (entre otros relacionados con operaciones CRUD para contratos, personas, enfermeros y servicios)

Cómo Instalar : 
Clona el repositorio.

Instala las dependencias: 
```
pip install -r requirements.txt
```

Realiza las migraciones:
```
python manage.py migrate
```

Ejecuta el servidor:
```
python manage.py runserver
```

Cómo Usar:
Regístrate como usuario. Para testear se da brinda el usuario: miguelangel / contraseña: hola123*
Acceso al portal de administración provisto por django: 127.0.0.1/admin : usuario: admin , contraseña:admin

Inicia sesión.
Navega por las distintas opciones disponibles en el menú.

Contribuir
Si deseas contribuir, por favor realiza un fork del repositorio y realiza un Pull Request.

Licencia
Este proyecto está bajo la Licencia MIT. Ve el archivo LICENSE.md para más detalles.
