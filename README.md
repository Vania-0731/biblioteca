
# API de Gestión de Biblioteca

Esta API permite realizar operaciones CRUD sobre libros, autores, categorías y préstamos de libros. A continuación se describe cada endpoint de la API.

## 1. **Registrar Libro**

**URL**: `/api/libros/`  
**Método**: `POST`  
**Descripción**: Permite registrar un nuevo libro, incluyendo autor y categoría si no existen.

### Parámetros requeridos:
- **autor_nombre** (string): Nombre del autor del libro.
- **autor_fecha_nacimiento** (date): Fecha de nacimiento del autor.
- **categoria_nombre** (string): Nombre de la categoría del libro.
- **titulo** (string): Título del libro.
- **disponible** (boolean): Indica si el libro está disponible para préstamo.

### Ejemplo de solicitud:

```json
{
  "autor_nombre": "Vania",
  "autor_fecha_nacimiento": "2025-05-13",
  "categoria_nombre": "Fantasía",
  "titulo": "La Oveja Voldadora",
  "disponible": true
}
```

### Respuesta exitosa (201 Created):

```json
{
  "id": 1,
  "titulo": "La Oveja Voldadora",
  "autor": {
    "id": 1,
    "nombre": "Vania",
    "fecha_nacimiento": "2025-05-13"
  },
  "categoria": {
    "id": 1,
    "nombre": "Fantasía"
  },
  "disponible": true
}
```

### Códigos de estado posibles:
- `201 Created`: El libro fue registrado exitosamente.
- `400 Bad Request`: Si faltan parámetros requeridos o los datos no son válidos.

---

## 2. **Buscar Libros**

**URL**: `/api/buscar_libros/`  
**Método**: `GET`  
**Descripción**: Permite buscar libros por título, autor o categoría.

### Parámetros:
- **titulo** (opcional): El título del libro que deseas buscar.
- **autor** (opcional): El nombre del autor del libro.
- **categoria** (opcional): El nombre de la categoría del libro.

### Ejemplo de solicitud:

```bash
GET /api/buscar_libros/?titulo=La%20Oveja%20Voldadora&autor=Vania
```

### Respuesta exitosa (200 OK):

```json
[
  {
    "id": 1,
    "titulo": "La Oveja Voldadora",
    "autor": {
      "id": 1,
      "nombre": "Vania",
      "fecha_nacimiento": "2025-05-13"
    },
    "categoria": {
      "id": 1,
      "nombre": "Fantasía"
    },
    "disponible": true
  }
]
```

### Códigos de estado posibles:
- `200 OK`: Solicitud exitosa.
- `400 Bad Request`: Si los parámetros de búsqueda no son válidos.

---

## 3. **Listar Libros Disponibles**

**URL**: `/api/libros_disponibles/`  
**Método**: `GET`  
**Descripción**: Permite obtener todos los libros disponibles para préstamo.

### Respuesta exitosa (200 OK):

```json
[
  {
    "id": 1,
    "titulo": "La Oveja Voldadora",
    "autor": {
      "id": 1,
      "nombre": "Vania",
      "fecha_nacimiento": "2025-05-13"
    },
    "categoria": {
      "id": 1,
      "nombre": "Fantasía"
    },
    "disponible": true
  }
]
```

### Códigos de estado posibles:
- `200 OK`: Solicitud exitosa.
- `404 Not Found`: No hay libros disponibles.

---

## 4. **Registrar Préstamo**

**URL**: `/api/prestamos/`  
**Método**: `POST`  
**Descripción**: Permite registrar un préstamo de libro.

### Parámetros requeridos:
- **libro** (integer): El **ID** del libro que se desea prestar.
- **usuario** (string): El nombre del usuario que realiza el préstamo.
- **fecha_prestamo** (date): Fecha en que se realiza el préstamo.
- **fecha_devolucion** (date): Fecha en que se debe devolver el libro.

### Ejemplo de solicitud:

```json
{
  "libro": 1,
  "usuario": "Juan Pérez",
  "fecha_prestamo": "2025-05-07",
  "fecha_devolucion": "2025-06-07"
}
```

### Respuesta exitosa (201 Created):

```json
{
  "id": 1,
  "libro": 1,
  "usuario": "Juan Pérez",
  "fecha_prestamo": "2025-05-07",
  "fecha_devolucion": "2025-06-07"
}
```

### Códigos de estado posibles:
- `201 Created`: El préstamo fue registrado exitosamente.
- `400 Bad Request`: Si el libro no está disponible o si faltan parámetros.

---

## 5. **Devolver Libro**

**URL**: `/api/devolver_libro/`  
**Método**: `POST`  
**Descripción**: Permite registrar la devolución de un libro.

### Parámetros requeridos:
- **prestamo_id** (integer): El **ID** del préstamo que se está devolviendo.

### Ejemplo de solicitud:

```json
{
  "prestamo_id": 1
}
```

### Respuesta exitosa (200 OK):

```json
{
  "mensaje": "Devolución registrada"
}
```

### Códigos de estado posibles:
- `200 OK`: Devolución registrada exitosamente.
- `400 Bad Request`: Si el préstamo no existe o ya ha sido devuelto.

---

## Instrucciones para clonar y correr el proyecto

### Pasos para clonar el proyecto desde GitHub

1. Clona el repositorio de GitHub:

```bash
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
```

2. Navega a la carpeta del proyecto:

```bash
cd nombre_del_repositorio
```

3. Crea un entorno virtual (si aún no tienes uno):

```bash
python -m venv venv
```

4. Activa el entorno virtual:

- En Windows:
  ```bash
  venv\Scripts ctivate
  ```

- En Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

5. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

6. Realiza las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

7. Crea un superusuario para acceder al panel de administración (opcional):

```bash
python manage.py createsuperuser
```

8. Corre el servidor de desarrollo:

```bash
python manage.py runserver
```

9. Accede a la API a través de `http://127.0.0.1:8000/` o el panel de administración en `http://127.0.0.1:8000/admin/`.

---

# Códigos de estado generales:

- **`200 OK`**: Solicitud exitosa.
- **`201 Created`**: Recurso creado exitosamente.
- **`400 Bad Request`**: Solicitud con datos no válidos o incompletos.
- **`404 Not Found`**: Recurso no encontrado.
- **`500 Internal Server Error`**: Error en el servidor.
