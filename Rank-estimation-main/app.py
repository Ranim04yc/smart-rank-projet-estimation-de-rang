"""
Application web Flask pour l'estimation de rang.
Interface web pour utiliser les modèles ML.
"""

from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)

# Charger les modèles une fois au démarrage
MODELS = {}

def load_models():
    """Charge tous les modèles ML."""
    global MODELS
    try:
        MODELS['ai'] = pickle.load(open("./models/ai_model.pickle", "rb"))
        MODELS['logic'] = pickle.load(open("./models/logic_model.pickle", "rb"))
        MODELS['network'] = pickle.load(open("./models/network_model.pickle", "rb"))
        MODELS['software'] = pickle.load(open("./models/software_model.pickle", "rb"))
        print("✅ Tous les modèles chargés avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur lors du chargement des modèles: {e}")
        return False

def calculate_avg(en, math, signal, ai, logic, os):
    """Calcule les moyennes pondérées pour chaque spécialité."""
    ai_avg = ((en) + (math * 2) + (signal * 3) + (ai * 4) + (logic * 2) + (os * 3)) / 15
    network_avg = ((en) + (math * 2) + (signal * 2) + (ai * 3) + (logic * 3) + (os * 4)) / 15
    logic_avg = ((en) + (math * 2) + (signal * 2) + (ai * 3) + (logic * 4) + (os * 3)) / 15
    software_avg = ((en) + (math * 2) + (signal * 2) + (ai * 4) + (logic * 3) + (os * 3)) / 15
    return (ai_avg, network_avg, logic_avg, software_avg)

@app.route('/')
def index():
    """Page d'accueil."""
    return render_template('index.html')

@app.route('/api/estimate', methods=['POST'])
def estimate_rank():
    """API endpoint pour estimer les rangs."""
    try:
        data = request.get_json()
        
        # Récupérer les données
        en = float(data.get('english', 0))
        math = float(data.get('math', 0))
        signal = float(data.get('signal', 0))
        ai = float(data.get('ai', 0))
        logic = float(data.get('logic', 0))
        os_score = float(data.get('os', 0))
        uni_avg = float(data.get('uni_avg', 17))
        
        # Calculer les moyennes
        all_avg = calculate_avg(en, math, signal, ai, logic, os_score)
        
        # Calculer les moyennes optimistes, réalistes et pessimistes
        optimistic_avg = all_avg
        realistic_avg = tuple(a - 1 for a in all_avg)
        pessimistic_avg = tuple(a - 2 for a in all_avg)
        
        # Prédire les rangs
        results = {
            'optimistic': {},
            'realistic': {},
            'pessimistic': {}
        }
        
        # Optimiste
        results['optimistic']['ai'] = int(MODELS['ai'].predict([[uni_avg, optimistic_avg[0]]])[0][0])
        results['optimistic']['network'] = int(MODELS['network'].predict([[uni_avg, optimistic_avg[1]]])[0][0])
        results['optimistic']['logic'] = int(MODELS['logic'].predict([[uni_avg, optimistic_avg[2]]])[0][0])
        results['optimistic']['software'] = int(MODELS['software'].predict([[uni_avg, optimistic_avg[3]]])[0][0])
        
        # Réaliste
        results['realistic']['ai'] = int(MODELS['ai'].predict([[uni_avg, realistic_avg[0]]])[0][0])
        results['realistic']['network'] = int(MODELS['network'].predict([[uni_avg, realistic_avg[1]]])[0][0])
        results['realistic']['logic'] = int(MODELS['logic'].predict([[uni_avg, realistic_avg[2]]])[0][0])
        results['realistic']['software'] = int(MODELS['software'].predict([[uni_avg, realistic_avg[3]]])[0][0])
        
        # Pessimiste
        results['pessimistic']['ai'] = int(MODELS['ai'].predict([[uni_avg, pessimistic_avg[0]]])[0][0])
        results['pessimistic']['network'] = int(MODELS['network'].predict([[uni_avg, pessimistic_avg[1]]])[0][0])
        results['pessimistic']['logic'] = int(MODELS['logic'].predict([[uni_avg, pessimistic_avg[2]]])[0][0])
        results['pessimistic']['software'] = int(MODELS['software'].predict([[uni_avg, pessimistic_avg[3]]])[0][0])
        
        return jsonify({
            'success': True,
            'results': results,
            'averages': {
                'ai': round(optimistic_avg[0], 2),
                'network': round(optimistic_avg[1], 2),
                'logic': round(optimistic_avg[2], 2),
                'software': round(optimistic_avg[3], 2)
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Démarrage de l'application web...")
    print("=" * 60)
    
    if load_models():
        print("\n✅ Serveur prêt!")
        print("📱 Ouvrez votre navigateur sur: http://localhost:5000")
        print("   Appuyez sur Ctrl+C pour arrêter")
        print("=" * 60)
        print()
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("\n❌ Impossible de charger les modèles. Vérifiez que les fichiers existent dans ./models/")


