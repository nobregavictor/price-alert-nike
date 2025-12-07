# Nike Price Alert

Script em Python que monitora o preço da camisa da seleção brasileira no site da Nike
e envia um e-mail quando o valor fica abaixo de um preço alvo definido no `.env`.

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

PRODUCT_URL=...
TARGET_PRICE=350.00
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_de_app
TO_EMAIL=seu_email@gmail.com

Executar:
python price_checker.py
