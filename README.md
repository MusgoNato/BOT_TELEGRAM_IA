# BOT_TELEGRAM_IA

# Pacotes necessários
- Tenha instalado os pacotes necesssários, no terminal execute os seguintes comandos:
```
pip install os
pip install groq
pip install telebot
```
# Passos
- Crie um bot no telegram e gere a chave do BOT
- Gere uma chave API da <a href="https://groq.com/">GroqCloud</a> para uso de IAs
- Crie um arquivo .env e adicione as seguintes informações
```
export API_KEY_BOT=CHAVE_DA_API_BOT_TELEGRAM
export API_KEY=CHAVE_API_GROQCLOUD
```
- Sobrescreva com as suas chaves API geradas

# Execução 
No terminal execute o seguinte comando para rodar o programa
```
py main.py
```

# Observações
As IAs utilizadas são inferiores as atuais em termos de assertividade e coesão. Seu histórico é limitado, sendo uma lista simples para armazenamento, então é possível que seja lento de acordo com a geração de respostas armazenadas no histórico da IA.