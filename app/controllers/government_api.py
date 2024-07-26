import requests

def enviar_datos_gobierno(data):
    url = "https://datos.gob.es/api/declaracion_renta"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

