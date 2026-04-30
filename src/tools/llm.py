import os 
from dotenv import load_dotenv

load_dotenv()

def deepseek(prompt: str) -> str:
    import httpx
    api = os.getenv("DEEPSEEK_API_KEY")

    response = httpx.post(
        "https://api.deepseek.com/chat/completions",
        headers= {"Authorization": f"Bearer {api}",
                 "Content-Type": "application/json"},
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
            }
    )    

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

_PROVIDERS = {
    "deepseek": deepseek,
}

def call_llm(prompt: str, provider: str = "deepseek") -> str:

    if provider not in _PROVIDERS:
        raise ValueError(f"Unsupported provider: {provider}")
    
    return _PROVIDERS[provider](prompt)


 