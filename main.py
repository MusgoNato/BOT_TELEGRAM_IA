import os
from groq import Groq
from telebot import TeleBot

# Atribuição das chaves apis
BOT_TOKEN = os.environ.get('API_KEY_BOT')
API_IA = os.environ.get('API_IA')

# Conexao com a api do telegram para o bot
bot = TeleBot(BOT_TOKEN)

# Historico da IA e sua configuração.
historico = [
    {
        "role": "system",
        "content": "Todas as respostas devem ser respondidas em português para o usuário",
    },
]

# Controlador de mensagens
@bot.message_handler(func=lambda message: message.chat.id)
def handler_message(message):

    # Conexao com a api para uso de uma IA
    User = Groq(api_key=API_IA)
    
    # Armazenando hostorico de mensagens
    userResponse = message.text.strip()
    historico.append({"role": "user", "content": userResponse})
    
    # Criação do chat
    chat = User.chat.completions.create(
        messages=historico,
        model="deepseek-r1-distill-qwen-32b",
        temperature=0,
        stream=False,
    )

    # Conteudo da resposta da IA formatada
    text_from_ia = chat.choices[0].message.content
    text_from_ia = text_from_ia.split("</think>")[-1].strip()
    historico.append({"role": "assistant", "content": text_from_ia})
    
    # Bot respondendo
    bot.send_message(message.chat.id, text_from_ia)

# Roda o bot
bot.infinity_polling()