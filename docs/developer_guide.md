# Developer Guide

## Configuración del Entorno de Desarrollo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/GESTiONapp.git
   cd GESTiONapp

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

pip install -r requirements.txt

├── README.md
├── main.py
├── requirements.txt
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── file_processor.py
│   │   ├── ocr.py
│   │   ├── classifier.py
│   │   └── government_api.py
├── tests
│   ├── __init__.py
│   ├── test_file_processor.py
│   ├── test_ocr.py
│   ├── test_classifier.py
│   └── test_government_api.py
└── docs
    ├── api_documentation.md
    ├── user_guide.md
    └── developer_guide.md

uvicorn main:app --reload


### Paso 3: Escribir el contenido de `user_guide.md`

1. Abre `docs/user_guide.md` y añade el siguiente contenido básico para la guía del usuario:

```markdown
# User Guide

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/GESTiONapp.git
   cd GESTiONapp

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

pip install -r requirements.txt

Uso de la Aplicación
Subir y Procesar Archivos
Para subir archivos y procesarlos, usa el siguiente endpoint:

POST /upload/

Parámetros:

files: Lista de archivos a subir.
Ejemplo de Uso:

curl -X POST "http://localhost:8000/upload/" -F "files=@/path/to/file.jpg"

Obtener Documento por ID
GET /documents/{document_id}

Parámetros:

document_id: ID del documento.

curl -X GET "http://localhost:8000/documents/1"

Crear Nuevo Documento
POST /documents/

Parámetros:

Document: Objeto JSON con los siguientes atributos:
id: ID del documento.
name: Nombre del documento.
content: Contenido del documento.
processed: Estado de procesamiento.
Ejemplo de Uso:
curl -X POST "http://localhost:8000/documents/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Documento de Ejemplo", "content": "Este es un documento de ejemplo.", "processed": false}'

¡Gracias por usar GESTiONapp!

### Paso 4: Añadir y comitear los archivos modificados

1. Abre tu terminal y navega al directorio del proyecto.
2. Añade los archivos modificados al staging area:

```bash
git add docs/api_documentation.md docs/developer_guide.md docs/user_guide.md

