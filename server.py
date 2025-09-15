from socket  import *
from constCS import * 
from urllib import parse
import requests
from bs4 import BeautifulSoup, Tag

REFERRER = "https://www.rmtcgoiania.com.br"

def menu():
    return b"""
 ____  __  __ _____ ____       ____ _     ___
|  _ \\|  \\/  |_   _/ ___|     / ___| |   |_ _|
| |_) | |\\/| | | || |   _____| |   | |    | |
|  _ <| |  | | | || |__|_____| |___| |___ | |
|_| \\_\\_|  |_| |_| \\____|     \\____|_____|___|

Digite o numero do ponto: """

def build_url(ponto: str) -> str:
    url = "https://www.rmtcgoiania.com.br"
    url += "/index.php?"
    params = {
            "option": "com_rmtclinhas",
            "view": "pedhorarios",
            "format": "raw",
            "ponto": ponto
            }
    return url + parse.urlencode(params)

def parse_html(html: str) -> list[dict]:
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', class_='horariosRmtc')
    if not table or not isinstance(table, Tag):
        return []

    rows = table.find_all('tr', bgcolor=lambda x: x in ['#f7f7f7', '#ffffff'])

    horarios = []
    for row in rows:
        if not isinstance(row, Tag):
            continue

        cols = row.find_all('td')
        cols = [ele.get_text(strip=True).replace('<strong>', '').replace('</strong>', '') for ele in cols]
        try:
            horario = {
                'linha': int(cols[0]),
                'destino': cols[1],
                'proximo': int(cols[2]),
                'seguinte': None if cols[3] == '---' else int(cols[3])
            }
        except (ValueError):
            continue
        horarios.append(horario)
    horarios.sort(key=lambda x: x['proximo'])
    return horarios

def print_table(horarios: list[dict]) -> str:
    if not horarios:
        return "Nenhum horario encontrado.\n"

    output = "Linha | Destino               | Proximo | Seguinte |\n"
    output += "-----------------------------------------------\n"
    for h in horarios:
        output += f"{h['linha']:5} | {h['destino'][:21]:21} | {h['proximo']:7} | {h['seguinte'] if h['seguinte'] is not None else '---':8} |\n"
    return output

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
conn.send(menu())
while True:
  msg = conn.recv(1024)
  if not msg: break
  ponto = msg.decode()

  url = build_url(ponto)
  r = requests.get(url, headers={"referer": REFERRER})
  html = r.text
  a = parse_html(html)
  table_str = print_table(a)
  conn.send(table_str.encode())
  
conn.close()
