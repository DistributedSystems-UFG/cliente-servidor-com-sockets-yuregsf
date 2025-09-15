[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZURhuU0i)
# ClientServerBasics (2.0)

Este projeto implementa uma consulta simples aos horários de um ponto de ônibus do sistema RMTC da cidade de Goiânia.

## Como usar

### Dependências

- Necessário acesso a Internet.

Instalar dependências:

```bash
pip install -r requirements
```

### Configuração

Editar o arquivo constCS.py com suas configurações de rede:

```python
# Exemplo:
HOST = 'localhost'
PORT = 5678
```

### Executar

1. Iniciar o servidor:

```bash
python server.py
```

2. Iniciar o client:

```bash
python client.py
```

### Exemplo

```bash
$ python client.py

 ____  __  __ _____ ____       ____ _     ___
|  _ \|  \/  |_   _/ ___|     / ___| |   |_ _|
| |_) | |\/| | | || |   _____| |   | |    | |
|  _ <| |  | | | || |__|_____| |___| |___ | |
|_| \_\_|  |_| |_| \____|     \____|_____|___|

Digite o numero do ponto:
71001
Linha | Destino               | Proximo | Seguinte |
-----------------------------------------------
   20 | T GARAVELO            |      44 | ---      |
```
