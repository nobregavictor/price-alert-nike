import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email_utils import send_email

load_dotenv()

PRODUCT_URL = os.getenv("PRODUCT_URL")
TARGET_PRICE = float(os.getenv("TARGET_PRICE", "0"))

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}


def get_price_from_nike(url: str) -> float:
    """Baixa a página e extrai o primeiro preço em R$ encontrado no texto.

    OBS: isso é um MVP simples. Em produção, o ideal é inspecionar o HTML
    e usar um seletor CSS específico para o preço.
    """
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    text = soup.get_text(" ", strip=True)

    match = re.search(r"R\$ ?(\d{1,3}(?:\.\d{3})*,\d{2})", text)
    if not match:
        raise ValueError("Não consegui encontrar um preço em R$ na página.")

    price_str = match.group(1)            # ex: "379,99" ou "1.234,56"
    normalized = price_str.replace(".", "").replace(",", ".")
    return float(normalized)


def main():
    if not PRODUCT_URL:
        raise RuntimeError("PRODUCT_URL não configurada no .env")

    print(f"Verificando preço em: {PRODUCT_URL}")
    current_price = get_price_from_nike(PRODUCT_URL)
    print(f"Preço atual: R$ {current_price:.2f}")
    print(f"Preço alvo: R$ {TARGET_PRICE:.2f}")

    if TARGET_PRICE and current_price <= TARGET_PRICE:
        subject = "Alerta de preço – Camisa Seleção Nike"
        body = (
            f"Preço atual: R$ {current_price:.2f}\n"
            f"Preço alvo: R$ {TARGET_PRICE:.2f}\n\n"
            f"Link: {PRODUCT_URL}"
        )
        send_email(subject, body)
        print("E-mail de alerta enviado!")
    else:
        print("Ainda não atingiu o preço alvo.")


if __name__ == "__main__":
    main()
