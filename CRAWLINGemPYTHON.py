#lib
import requests

#code
def obter_cotacao(url, elemento_id):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        content = resposta.text
        # Posição inicial do elemento pelo ID
        pos_inicio = content.find(f'id="{elemento_id}"')
        if pos_inicio != -1:
            # Ponto onde o id é encontrado
            snippet = content[pos_inicio:]
            # Encontra o início e o fim do valor
            pos_inicio_valor = snippet.find('value="') + 7
            pos_fim_valor = snippet.find('"', pos_inicio_valor)
            valor = snippet[pos_inicio_valor:pos_fim_valor]
            valor = valor.strip().replace(',', '.')
            return round(float(valor), 2)
    return None

def main():
    url_bitcoin = 'https://dolarhoje.com/bitcoin-hoje/'
    url_dolar = 'https://dolarhoje.com/'
    
    valor_btc = obter_cotacao(url_bitcoin, 'nacional')
    valor_dol = obter_cotacao(url_dolar, 'nacional')
    
    if valor_btc and valor_dol:
        btc_dol = valor_btc / valor_dol
        print(f'1 bitcoin (R${valor_btc}) vale US${btc_dol:.2f} (US$1 = R${valor_dol})')
    else:
        print("Não foi possível obter as cotações necessárias.")

if __name__ == "__main__":
    main()
