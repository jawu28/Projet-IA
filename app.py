from flask import Flask, request, jsonify
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from pyngrok import ngrok
import threading

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return "Bienvenue sur l'API UR3_Cobot ! Utilisez l'endpoint /predict avec une requête POST pour faire des prédictions."

# Charger le modèle et le scaler
model = load_model('lstm_optimized_model.h5')
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
scaler = joblib.load('scaler.pkl')
print("Modèle et scaler chargés avec succès")

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request Content-Type is application/json
    if request.content_type != 'application/json':
        return jsonify({'error': "Le Content-Type de la requête doit être 'application/json'."}), 415

    try:
        data = request.get_json()

        # Ensure the required 'input_data' field is in the request
        if 'input_data' not in data:
            return jsonify({'error': "Le champ 'input_data' est requis"}), 400

        input_data = np.array(data['input_data'])  # Shape: (10, 22)

        # Validate the shape of input data
        if input_data.shape != (10, 22):
            return jsonify({'error': "L'entrée doit être de forme (10, 22)"}), 400

        # Normalize the input data
        input_flat = input_data.reshape(-1, 22)  # Shape: (10, 22)
        normalized_data = scaler.transform(input_flat)
        reshaped_data = normalized_data.reshape(1, 10, 22)  # Shape: (1, 10, 22)

        # Predict using the model
        prediction = model.predict(reshaped_data)
        predicted_class = np.argmax(prediction, axis=1)[0]
        probability = prediction[0].tolist()

        # Return the prediction result as JSON
        response = {
            'prediction': int(predicted_class),
            'probability': probability
        }
        return jsonify(response), 200

    except Exception as e:
        # Handle errors and return a message
        return jsonify({'error': str(e)}), 400

# Run Flask in a separate thread
def run_flask():
    app.run(debug=True, host='0.0.0.0', port=5002, use_reloader=False)

# Terminer tout tunnel ngrok existant
ngrok.kill()
print("Tous les tunnels ngrok existants ont été terminés")

# Configurer ngrok avec ton authtoken
!ngrok config add-authtoken 2vN6XZtwK8zuDIVhqNcFv6WfYX7_76MhhCU15eBMoAxS8XTH2

# Créer un nouveau tunnel ngrok
public_url = ngrok.connect(5002)
print("URL publique pour accéder à l'API :", public_url)

# Start Flask in a separate thread
threading.Thread(target=run_flask).start()
