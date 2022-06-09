import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

def moeda(coin):
    data = requests.get(f"https://economia.awesomeapi.com.br/json/last/{coin.upper()}")
    data_json = data.json()
    return data_json[coin.replace("-","").upper()]

class obj:
    def __init__(self, eur, brl, usd):
        self.eur = eur
        self.brl = brl
        self.usd = usd
    def get_moedas(self):
        return self.eur, self.brl, self.usd

dados_obj = obj(moeda("BTC-EUR"),moeda("BTC-BRL"),moeda("BTC-USD")).get_moedas()
# print(dados_obj)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = dados_obj
        self.wfile.write(bytes(json.dumps(message), "utf8"))
with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()
