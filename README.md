# 🏅 Olimpíadas 2024 Notificações 🏅

## Descrição

Este projeto tem como objetivo enviar notificações das últimas manchetes das Olimpíadas 2024 diretamente para o seu Telegram. Utilizando técnicas de web scraping, o projeto coleta as manchetes do site Globo Esporte e as envia via bot do Telegram.

## Funcionalidades

- 🕸️ **Web Scraping**: Extração automatizada de manchetes do site Globo Esporte.
- 🤖 **Bot do Telegram**: Envio de notificações diretamente para o seu Telegram.
- 🔔 **Notificações Automáticas**: O sistema pode ser configurado para rodar automaticamente em horários definidos.
- 🥇 **Atualização de Medalhas**: Em breve, funcionalidade para atualização automática do quadro de medalhas.

## Tecnologias Utilizadas

- Python
- Requests
- BeautifulSoup (BS4)
- API do Telegram

## Como Usar

### Pré-requisitos

- Python 3.x instalado
- Conta no Telegram e um bot configurado (você pode criar um bot através do BotFather no Telegram)

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/olimpiadas-2024-notificacoes.git
    cd olimpiadas-2024-notificacoes
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

### Configuração

1. Substitua `TOKEN` pelo seu token do bot do Telegram e `CHATTOKEN` pelo ID do chat no arquivo `main.py`.

    ```python
    # Configurações do Telegram
    telegram_token = 'TOKEN'  # Substitua pelo seu token do bot
    telegram_chat_id = 'CHATTOKEN'  # Substitua pelo seu chat ID
    ```

### Execução

Execute o script principal:

```bash
python main.py
