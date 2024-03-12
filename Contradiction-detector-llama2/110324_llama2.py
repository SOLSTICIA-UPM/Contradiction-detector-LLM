import requests

# Definir contexto y pregunta
context = """
Requierement 1: System should allow warden to assign student a seat in his hostel.
Requirement 2: System should allow warden to assign student a seat in his hostel if he has approval from provost.
"""

question = "Do the requirements contradict each other?"

# Plantilla
template = f"""
I will present various software requirements in the context delimited by angle brackets. These proposed requirements may contradict each other.

A contradiction in software requirements refers to a scenario where two or more specified requirements are mutually exclusive or incompatible,
preventing their simultaneous fulfillment or coexistence within the system.

Provide a unique response with the following structure:

Identify contradiction: Respond with a simple 'yes' or 'no'.
Argument: Present a concise explanation, limited to 50 words, to justify your response.

If you don't have the information then give response \"I don't know\".

Context:
<{context}>

Question: {question}

Response:
"""

# API URL y token
api_url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
token = "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"

# Encabezado de autorización
headers = {"Authorization": f"Bearer {token}"}

# Cuerpo de la solicitud
data = {"inputs": template}

# Realizar la solicitud POST a la API
response = requests.post(api_url, headers=headers, json=data)

# Obtener la respuesta del modelo
if response.status_code == 200:
    resultados = response.json()
    respuesta = resultados[0]["generated_text"]
    print("Respuesta del modelo:", respuesta)
else:
    print("Error al hacer la solicitud:", response.status_code)
