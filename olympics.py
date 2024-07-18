import requests
from bs4 import BeautifulSoup

def globo_news_crawler(url):
    print("Iniciando o crawler...")
    headlines = []
    try:
        # Faz uma requisição GET para a URL
        response = requests.get(url)
        print(f"Status da requisição: {response.status_code}")
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            print("Requisição bem-sucedida. Analisando o conteúdo da página...")
            # Cria um objeto BeautifulSoup para analisar o conteúdo da página
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontra todas as manchetes na página
            headline_tags = soup.find_all('a', class_='feed-post-link')
            print(f"Encontradas {len(headline_tags)} manchetes.")
            
            # Extrai o texto das manchetes encontradas
            for tag in headline_tags:
                headlines.append(tag.get_text(strip=True))
            print("Manchetes extraídas com sucesso.")
        else:
            print(f"Erro ao acessar a página. Status code: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    return headlines

def send_telegram_notification(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Notificação enviada com sucesso.")
    else:
        print(f"Erro ao enviar notificação: {response.status_code} - {response.text}")

# URL para realizar o crawling
url = 'https://ge.globo.com/olimpiadas/'
headlines = globo_news_crawler(url)

# Configurações do Telegram
telegram_token = 'TOKEN'  # Substitua pelo seu token do bot
telegram_chat_id = 'CHATTOKEN'  # Substitua pelo seu chat ID

# Criar a mensagem da notificação com emojis
message_lines = [f"🏅 {headline}" for headline in headlines[:5]]
message = "Aqui estão as manchetes mais recentes das Olimpíadas 2024:\n\n" + "\n".join(message_lines)

# Enviar notificação para o Telegram
send_telegram_notification(telegram_token, telegram_chat_id, message)
