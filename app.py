from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Configurações do Azure Translator
AZURE_TRANSLATOR_ENDPOINT = "https://api.cognitive.microsofttranslator.com/translate"
#obtem as variáveis de ambiente
AZURE_SUBSCRIPTION_KEY = os.getenv("AZURE_SUBSCRIPTION_KEY")  
AZURE_REGION = os.getenv("AZURE_REGION")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    post_url = request.form['url']
    
    post_content = extract_text_from_url(post_url)
    
    # Configura a chamada de tradução
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_SUBSCRIPTION_KEY,
        'Ocp-Apim-Subscription-Region': AZURE_REGION,
        'Content-Type': 'application/json'
    }
    
    body = [{
        'text': post_content
    }]
    
    params = {
        'api-version': '3.0',
        'to': 'pt-br' #fixo para pt-br
    }

    response = requests.post(AZURE_TRANSLATOR_ENDPOINT, headers=headers, json=body, params=params)
    translation = response.json()[0]['translations'][0]['text']

    return render_template('index.html', translation=translation)

def extract_text_from_url(url):
    response = requests.get(url)
 
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch URL: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    article = soup.find('article')
    if article:
        text = article.get_text(separator=' ')
    else:
        text = soup.get_text(separator=' ')

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

if __name__ == '__main__':
    app.run(debug=True)
