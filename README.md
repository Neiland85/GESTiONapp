# GESTiONapp

GESTiONapp es una aplicación diseñada para la gestión y procesamiento de documentos de manera eficiente. Utilizando tecnologías modernas y diversas herramientas de automatización, GESTiONapp permite la carga, procesamiento y análisis de archivos como PDFs, JPGs y PNGs. Además, integra funcionalidades avanzadas de OCR (Reconocimiento Óptico de Caracteres) y clasificación de documentos, facilitando la interacción con APIs gubernamentales para la gestión de datos.

## Características Principales

- **Carga de Archivos**: Permite la carga de múltiples archivos simultáneamente a través de una API fácil de usar.
- **Procesamiento de Documentos**: Procesa archivos de diferentes formatos (PDF, JPG, PNG) y extrae información relevante.
- **OCR Avanzado**: Utiliza OCR para extraer texto de imágenes y documentos escaneados.
- **Clasificación de Documentos**: Clasifica y organiza documentos automáticamente.
- **Integración con APIs Gubernamentales**: Facilita la comunicación con APIs del gobierno para enviar y recibir datos.
- **Interfaz Amigable**: Desarrollado con FastAPI, proporcionando una API rápida y robusta.

## Estructura del Proyecto

├── README.md
├── main.py
├── requirements.txt
├── app
│ ├── init.py
│ ├── models.py
│ ├── views.py
│ ├── controllers
│ │ ├── init.py
│ │ ├── file_processor.py
│ │ ├── ocr.py
│ │ ├── classifier.py
│ │ └── government_api.py
├── tests
│ ├── init.py
│ ├── test_file_processor.py
│ ├── test_ocr.py
│ ├── test_classifier.py
│ └── test_government_api.py
└── docs
├── api_documentation.md
├── user_guide.md
└── developer_guide.md


## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/GESTiONapp.git
   cd GESTiONapp

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

pip install -r requirements.txt

uvicorn main:app --reload

Uso
Para subir archivos y procesarlos, usa el siguiente endpoint:

POST /upload/

Parámetros:

files: Lista de archivos a subir.
Ejemplo de Uso:

curl -X POST "http://localhost:8000/upload/" -F "files=@/path/to/file.jpg"

Contribuciones
¡Contribuciones son bienvenidas! Por favor, abre un issue o un pull request si tienes alguna mejora o corrección.

Licencia
Este proyecto está licenciado bajo la MIT License.


