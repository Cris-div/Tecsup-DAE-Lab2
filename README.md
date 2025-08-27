# 🧪 Laboratorio 02 – Flujo de Trabajo en Django

## 🎯 Objetivos  
- Comprender el flujo de trabajo en un proyecto Django siguiendo el patrón **MVT (Model–View–Template)**.  
- Configurar el entorno virtual y trabajar con dependencias usando `pip` y `requirements.txt`.  
- Crear un proyecto Django con al menos **3 aplicaciones conectadas de forma coherente**.  
- Implementar **CRUD completo** en la app `tasks` (crear, listar, actualizar, eliminar).  
- Desarrollar estilos con **CSS puro** y consumir **endpoints JSON** con **JS vanilla**.  
- Documentar el trabajo realizado y manejar el proyecto con **Git y GitHub**.  

---

## ⚙️ Desarrollo  

1. **Configuración del entorno**  
   - Creación del proyecto y activación de entorno virtual en Windows.  
   - Instalación de dependencias y registro en `requirements.txt`.  

2. **Creación del proyecto y apps**  
   - `config` → configuración principal.  
   - `tasks` → gestión de tareas.  
   - `users` → gestión de usuarios.  
   - `categories` → clasificación de tareas.  

3. **Modelos y relaciones**  
   - Definición del modelo `Task` con título, descripción, estado, prioridad y relación con `User` y `Category`.  
   - Aplicación de migraciones para generar las tablas en la base de datos.  

4. **Vistas y Templates**  
   - Implementación de vistas para CRUD de tareas.  
   - Creación de plantillas HTML (`task_list.html`, `task_form.html`, `task_confirm_delete.html`) con CSS puro.  

5. **Endpoints y consumo desde frontend**  
   - Creación de endpoint `/api/tasks/` para devolver tareas en JSON.  
   - Consumo desde el frontend con `fetch` en JavaScript.  

6. **Control de versiones con Git**  
   - Creación de ramas (`feature/tasks-app`, `feature/users-app`, etc.).  
   - Subida del proyecto a GitHub en un repositorio centralizado.  

---

## 📸 Evidencias  

- Captura del **Frontend** mostrando lista de tareas.  
- Captura de la **CLI** ejecutando el servidor.  
- Captura de la **estructura del proyecto** en VS Code.  
- Captura del **endpoint JSON** funcionando en el navegador.  

*(Aquí irían las imágenes en la carpeta `evidencias/` como en el Lab01)*  

---

## ✅ Conclusiones  

1. La práctica permitió reforzar el **flujo completo de un proyecto Django**, desde la configuración inicial hasta el despliegue en el navegador.  
2. La creación de varias apps (`tasks`, `users`, `categories`) permitió entender cómo **separar responsabilidades** y mantener el proyecto organizado.  
3. Implementar el CRUD de tareas fue clave para comprender cómo se conectan los modelos, vistas y plantillas en el patrón MVT.  
4. Usar **CSS puro** mostró la importancia de personalizar el frontend sin depender de frameworks externos.  
5. La integración de **endpoints y consumo con JS** permitió ver cómo Django puede servir datos dinámicos que luego el frontend utiliza.  
6. Se afianzaron buenas prácticas de **Git y GitHub**, trabajando con ramas y documentando el proyecto en un repositorio.  
7. Este laboratorio consolidó los conocimientos de Django y sentó las bases para proyectos más grandes con mayor integración de frontend y backend.  

---

## 👨‍💻 Autor  
**Christian David Unocc Ramirez**  
Laboratorio 02 – Desarrollo de Aplicaciones Empresariales  
