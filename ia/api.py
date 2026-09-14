from dotenv import load_dotenv
import os
from openai import OpenAI , AuthenticationError

load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La clé OPENAI_API_KEY n'a pas été trouvée dans le fichier .env")

client = OpenAI(api_key=api_key)


def appeler_openai(prompt: str, system_prompt: str = "Tu es un assistant utile.") -> str:
    try:
        client=OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title":"COMORIA"
            }
        )
        """
            Envoie un message à OpenAI et retourne la réponse.
            """
        response = client.chat.completions.create(
            model="gpt-4o-mini",          
            messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
            ],
             temperature=0.7
        )
    
        return response.choices[0].message.content
    except AuthenticationError:
        return "Nous garidjawoo"
    except Exception as e:
        return f"Erreur: {str(e)}"
    
