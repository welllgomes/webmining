#lib
#!pip install requests
#!pip install beautifulsoup4

#code
import requests
from bs4 import BeautifulSoup

def obter_cotacao(url, elemento, atributo):
    x = requests.get(url)
    if x.status_code == 200:
        soup = BeautifulSoup(x.content, 'html.parser')
        cotacao = soup.find(elemento, atributo)
        if cotacao:
            valor = cotacao.get('value').strip().replace(',', '.')
            return round(float(valor), 2)
    return None

def main():
    url_bitcoin = 'https://dolarhoje.com/bitcoin-hoje/'
    url_dolar = 'https://dolarhoje.com/'
    
    valor_btc = obter_cotacao(url_bitcoin, 'input', {'id': 'nacional'})
    valor_dol = obter_cotacao(url_dolar, 'input', {'id': 'nacional'})
    
    if valor_btc and valor_dol:
        btc_dol = valor_btc / valor_dol
        print(f'wellington_gomes >> 1 bitcoin (R${valor_btc}) vale US${btc_dol:.2f} (US$1 = R${valor_dol})')
    else:
        print("Não foi possível obter as cotações necessárias.")

if __name__ == "__main__":
    main()
