# Nike Price Alert

Script em Python que monitora o preço da camisa da seleção brasileira no site da Nike
e envia um e-mail quando o valor fica abaixo de um preço alvo definido no `.env`.
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/7f019982-1383-440e-9526-c5dbf891c493" />


## Tecnologias

- Python
- Requests
- BeautifulSoup4
- python-dotenv
- SMTP (envio de e-mail)

## Como usar

1. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
Instale as dependências:


pip install -r requirements.txt
Crie um arquivo .env na raiz com:

env

PRODUCT_URL=https://www.nike.com.br/camisa-nike-brasil-i-2024-25-torcedor-pro-masculina-028564.html?cor=0L

TARGET_PRICE=350.00

EMAIL_HOST=smtp.gmail.com

EMAIL_PORT=465

EMAIL_USER=seu_email@gmail.com

EMAIL_PASS=sua_senha_de_app

TO_EMAIL=seu_email@gmail.com

Executar:
python price_checker.py
