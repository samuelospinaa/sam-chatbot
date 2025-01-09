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

# Crear un modelo generativo
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
  system_instruction="""
"Respond in a clear and concise manner, as if you were explaining a concept to a curious child. Avoid using technical terms like 'algorithm', 'neuron', or 'token'. Focus on the meaning and practical application of the information, using simple examples and analogies. If you are unsure how to respond without revealing technical details, rephrase the answer to be more general and accessible. Either dont explain or show what the user are saying or what is your process to chose the answer."""
)


def run_chat(user_input):
    response = model.generate_content(user_input)
    return response.text
