# API Documentation

## Endpoints

### GET /documents/{document_id}
- **Descripción**: Obtiene un documento por ID.
- **Parámetros**:
  - `document_id`: ID del documento.
- **Respuesta**:
  - `document_id`: ID del documento.
  - `name`: Nombre del documento.
  - `content`: Contenido del documento.
  - `processed`: Estado de procesamiento.

### POST /documents/
- **Descripción**: Crea un nuevo documento.
- **Parámetros**:
  - `Document`: Objeto JSON con los siguientes atributos:
    - `id`: ID del documento.
    - `name`: Nombre del documento.
    - `content`: Contenido del documento.
    - `processed`: Estado de procesamiento.
- **Respuesta**:
  - `message`: Mensaje de éxito.
  - `document`: Objeto JSON del documento creado.

