"# User Guide\n\n

## Instalación\n\n1. 
Clona el repositorio:\n   \`\`\`bash\n   git clone https://github.com/TU_USUARIO/GESTiONapp.git\n   cd GESTiONapp\n   \`\`\`\n\
n2. Crea y activa un entorno virtual:\n   \`\`\`bash\n   python -m venv venv\n   source venv/bin/activate  # En Windows usa \`venv\\Scripts\\activate\`\n   \`\`\`\n\
n3. Instala las dependencias:\n   \`\`\`bash\n   pip install -r requirements.txt\n   \`\`\`\n\n## Uso de la Aplicación\n\n### Subir y Procesar Archivos\n\nPara subir archivos y procesarlos, usa el siguiente endpoint:\n\n- **POST /upload/**\n\n  **Parámetros:**\n  - \`files\`: Lista de archivos a subir.\n\n  **Ejemplo de Uso:**\n  \`\`\`bash\n  curl -X POST \"http://localhost:8000/upload/\" -F \"files=@/path/to/file.jpg\"\n  \`\`\`\n\n### Obtener Documento por ID\n\n- **GET /documents/{document_id}**\n\n  **Parámetros:**\n  - \`document_id\`: ID del documento.\n\n 

 **Ejemplo de Uso:**\n  \`\`\`bash\n  curl -X GET \"http://localhost:8000/documents/1\"\n  \`\`\`\n\n### Crear Nuevo Documento\n\n- **POST /documents/**\n\n  **Parámetros:**\n  - \`Document\`: Objeto JSON con los siguientes atributos:\n    - \`id\`: ID del documento.\n    - \`name\`: Nombre del documento.\n    - \`content\`: Contenido del documento.\n    - \`processed\`: Estado de procesamiento.\n\n  **Ejemplo de Uso:**\n  \`\`\`bash\n  curl -X POST \"http://localhost:8000/documents/\" -H \"Content-Type: application/json\" -d '{\"id\": 1, \"name\": \"Documento de Ejemplo\", \"content\": \"Este es un documento de ejemplo.\", \"processed\": false}'\n  \`\`\`\n\n---\n\n
¡Gracias por usar GESTiONapp!"
