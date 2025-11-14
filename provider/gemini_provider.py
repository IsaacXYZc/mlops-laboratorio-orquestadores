from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini = OpenAI(
    api_key=gemini_api_key
    ,base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model_name = "gemini-2.0-flash"

def get_traduction(text, target_language):
    response =  gemini.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates text to the target language specified by the user."},
            {"role": "user", "content": f"translate to " + target_language +": " + text },
        ],
        temperature=0.7,
    )
    answer = response.choices[0].message.content
    return answer


if __name__ == "__main__":
    test_text = "Hola, ¿cómo estás?"
    target_language = "Inglés"
    print(get_traduction(test_text, target_language))