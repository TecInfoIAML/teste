from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para lidar com a solicitação do formulário
@app.route('/prever_evasao', methods=['POST'])
def prever_evasao():
    # Obtenha os dados do formulário
    dados_formulario = request.form.to_dict()

    # Envie os dados para a sua API
    api_url = ''http://21339de0-85d7-4708-a0f6-404d0b59524b.southcentralus.azurecontainer.io/prever_evasao';'
    resposta_api = requests.post(api_url, json=dados_formulario)

    # Processar a resposta da API conforme necessário
    resultado_previsao = resposta_api.json()

    # Exibir o resultado em uma página HTML
    return render_template('resultado.html', resultado=resultado_previsao)

if __name__ == '__main__':
    app.run(debug=True)
