import requests

api_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
question = "What is the meaning of life? Answer:"
token = "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"

# Definir el encabezado de autorización
headers = {"Authorization": f"Bearer {token}"}

# Cuerpo de la solicitud
data = {"inputs": question}

# Realizar la solicitud POST a la API
response = requests.post(api_url, headers=headers, json=data)

# Obtener la respuesta del modelo
if response.status_code == 200:
    resultados = response.json()
    respuesta = resultados[0]["generated_text"]
    print("Respuesta del modelo:", respuesta)
else:
    print("Error al hacer la solicitud:", response.status_code)
    