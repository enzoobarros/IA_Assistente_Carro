# 🤖 JARVIS Voice Assistant (Python)

Um assistente de voz inspirado no **JARVIS**, desenvolvido em **Python**, capaz de escutar comandos, interpretar perguntas e responder com voz natural, tudo de forma modular e expansível.

---

## ✨ Principais Recursos

O JARVIS pode:

- 🎙️ Ativar por palavra-chave (**“Hey Jarvis”**)
- 🎧 Ouvir comandos por voz
- 📝 Converter fala em texto
- 🧠 Processar perguntas com IA
- 🔊 Responder utilizando **Text-to-Speech**
- ⏰ Executar comandos locais simples, como informar a hora

---

## 🚀 Funcionalidades

- 🎧 **Wake Word** com `openWakeWord`
- 🗣️ **Reconhecimento de fala** usando `faster-whisper`
- 🧠 **IA conversacional** integrada (`jarvis_brain`)
- 🔊 **Síntese de voz (TTS)** com `edge-tts`
- ⏰ **Comandos locais**, como:
  - “Que horas são?”
  - “Quem é você?”
- 🛑 **Controle de fala** (interromper respostas)
- ⚙️ Arquitetura modular, fácil de manter e expandir

---

## 🧠 Funcionamento do JARVIS

Fluxo básico de execução:

1. O microfone fica escutando passivamente  
2. Ao detectar **“Hey Jarvis”**, o assistente é ativado  
3. O áudio é gravado por alguns segundos  
4. O áudio é convertido em texto (Whisper)  
5. O texto é processado:
   - Comandos locais (ex: hora)
   - Perguntas enviadas para a IA  
6. A resposta é gerada em texto  
7. O texto é convertido em voz (Edge TTS)  
8. O áudio é reproduzido para o usuário  

---

## 📁 Estrutura do Projeto

```text
jarvis_car/
├── jarvis_listen.py   # Arquivo principal (escuta, wake word e controle)
├── jarvis_brain.py    # Lógica de IA / respostas inteligentes
├── venv/              # Ambiente virtual
├── fala.mp3           # Arquivo de áudio temporário
└── README.md          # Documentação
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- PyAudio
- NumPy
- Pygame
- edge-tts
- faster-whisper
- openWakeWord
- Asyncio
- ChatGPT OpenIA

---

## 📦 Instalação

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2️⃣ Crie o ambiente virtual
```bash
python -m venv venv
```

### 3️⃣ Ative o ambiente virtual

**Linux / Zorin OS / macOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4️⃣ Instale as dependências
```bash
pip install pyaudio numpy pygame edge-tts faster-whisper openwakeword
```

⚠️ **Obs:** o PyAudio pode exigir dependências adicionais do sistema no Linux.

---

## ▶️ Como Executar

```bash
python jarvis_listen.py
```

No terminal, você verá:

```text
🎧 Aguardando 'HEY JARVIS'...
```

Diga:

**“Hey Jarvis”**

Depois faça sua pergunta 🎤

---

## ⏰ Exemplo de Comando Local

**Pergunta:**
> “Que horas são?”

**Resposta:**
> “Agora são 15 horas e 32 minutos.”

---

## 🧩 Comandos Suportados (Exemplos)

- “Que horas são?”
- “Quem é você?”
- “Pare”
- “Silêncio”

---

## 🔧 Personalização

### 🎙️ Trocar a voz

No arquivo `jarvis_listen.py`:

```python
VOICE = "pt-BR-AntonioNeural"
```

Você pode substituir por outras vozes disponíveis no **Edge TTS**.

---

## 🧠 IA (`jarvis_brain.py`)

O arquivo `jarvis_brain.py` é responsável por:

- Processar perguntas abertas  
- Conectar com APIs  
- Gerar respostas inteligentes  

Ele pode ser expandido para incluir:

- 🌐 Internet  
- 🌦️ Clima  
- 📰 Notícias  
- 🖥️ Controle de sistemas  
- 🏠 Automação residencial  

---

## ⚠️ Observações Importantes

- Utilize um microfone de boa qualidade  
- Execute em ambiente silencioso  
- O projeto ainda está em desenvolvimento  
- Algumas funcionalidades podem ser experimentais  

---

## 📌 Próximas Melhorias (Roadmap)

- 🌐 Conexão com internet (notícias, clima, presidente do país)
- 🧠 Memória de contexto
- 🎵 Controle de mídia
- 🏠 Automação residencial
- 🖥️ Interface gráfica

---

## 👨‍💻 Autor

Autor: Enzo Barros João
Projeto Desenvolvido para fins educativos com o uso de IA   
Inspirado no **JARVIS** do Homem de Ferro 🦾

---

## ⭐ Contribuição

Sinta-se à vontade para:

- Abrir *issues*
- Enviar *pull requests*
- Sugerir melhorias

Se gostou do projeto, deixe uma ⭐ no repositório!
