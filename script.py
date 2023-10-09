from flask import Flask, request, jsonify
import tensorflow as tf
import joblib


app = Flask(__name__)
model = tf.keras.models.load_model('seu_modelo.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Faça previsões com o modelo TensorFlow aqui usando os dados recebidos
    predictions = model.predict(data)
    return jsonify({'predictions': predictions.tolist()})


# Carregar o modelo treinado
model = joblib.load("seu_modelo.pkl")  # Para modelos scikit-learn
# OU
model = tf.keras.models.load_model("seu_modelo.h5")  # Para modelos TensorFlow/Keras

# Função para fazer previsões
def fazer_previsao(dados):
    # Realizar pré-processamento dos dados, se necessário
    # Fazer previsões com o modelo
    resultado = model.predict(dados)
    return resultado
    
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/prever_evasao', methods=['POST'])
def prever_evasao():
    dados = request.json  # Recebe os dados do formulário como JSON
    resultado = fazer_previsao(dados)
    return jsonify({"previsao": resultado.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
