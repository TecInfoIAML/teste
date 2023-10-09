from flask import Flask, request, render_template
import urllib.request
import json
import os
import ssl

app = Flask(__name__)

def allowSelfSignedHttps(allowed):
    # Bypass the server certificate verification on the client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

# URL da sua API de pontuação
api_url = 'http://21339de0-85d7-4708-a0f6-404d0b59524b.southcentralus.azurecontainer.io/score'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prever_evasao', methods=['POST'])
def prever_evasao():
    # Receber os dados do formulário HTML
    dados_formulario = request.form.to_dict()

    # Formatar os dados em um formato adequado para a solicitação à API
    data = {
        "Inputs": {
            "input1": [dados_formulario]
        },
        "GlobalParameters": {}
    }

    # Enviar a solicitação à API de pontuação
    body = str.encode(json.dumps(data))
    api_key = '65DEgn8acd3mWVh3cKSEMaHVfKr2g004'  # Substitua pela sua chave de API, se necessário
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib.request.Request(api_url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        resultado = json.loads(result.decode("utf-8"))
        # Extrair o resultado da API
        score_labels = resultado["Results"]["output1"][0]["Scored Labels"]
        resultado_final = "Não Evadido" if score_labels == '0' else "Evadido"

        # Renderizar o template HTML com o resultado
        return render_template('resultado.html', resultado=resultado_final)

    except urllib.error.HTTPError as error:
        print("A solicitação falhou com o código de status: " + str(error.code))
        print(error.info())
        print(error.read().decode("utf-8", 'ignore'))

if __name__ == '__main__':
    app.run()

