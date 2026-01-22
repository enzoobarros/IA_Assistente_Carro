import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é o J.A.R.V.I.S., um assistente de voz embarcado em um carro.

REGRAS OBRIGATÓRIAS:
- Responda SEMPRE em português do Brasil
- Seja direto, claro e educado
- Use frases curtas
- NÃO invente histórias, empresas ou personagens
- NÃO cite Tony Stark, filmes ou ficção
- NÃO use listas longas
- NÃO faça perguntas desnecessárias
- NUNCA diga algo que voce não sabe em hipotese alguma
- Se não souber algo, diga claramente que não sabe'
- Se a pergunta for vaga, peça esclarecimento em UMA frase curta

ESTILO:
- Tom calmo, confiante e profissional
- Como um assistente real de veículo
"""

# =========================
# RESPOSTA NORMAL (STRING)
# =========================
def perguntar_jarvis(texto: str) -> str:
    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": texto}
        ],
        temperature=0.3,   # 🔥 MUITO IMPORTANTE
        max_tokens=150
    )

    return resposta.choices[0].message.content.strip()


# =========================
# RESPOSTA EM STREAM (FUTURO)
# =========================
def perguntar_jarvis_stream(texto: str):
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": texto}
        ],
        temperature=0.6,
        stream=True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            yield delta.content
