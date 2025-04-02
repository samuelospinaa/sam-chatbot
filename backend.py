import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Configurar la API con la clave
genai.configure(api_key=api_key)

# Configuración para la generación de contenido
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 500,
  "response_mime_type": "text/plain",
}

functions = [
  {
    "name": "get_product_price",
    "description": "Obtener mejores precios y mejores proveedores de producto en especifico",
    "parameters": {
      "type": "object",
      "properties": {
        "product_name": {
          "type": "string"
        }
      },
      "required": [
        "product_name"
      ]
    }
  }
]

# Crear un modelo generativo
model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="""
""""Eres un asistente para una pagina que se llama Dropi, la cual funciona para que personas que quieran hacer dropshipping puedan escoger y ver precios en general productos ganadores. Dentro de tus funciones esta el dar los mejores precios y cual es proveedor del producto que el usuario te de, a su vez dar cualquier tipo de asesoria sobre dropshipping que el usuario te pida."""
)


def run_chat(user_input):
    response = model.generate_content(user_input)
    return response.text
