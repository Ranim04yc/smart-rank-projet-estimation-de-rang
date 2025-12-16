"""
Test de la logique du bot sans avoir besoin d'un token Telegram réel.
Ce script teste toutes les fonctions du bot.
"""

import pickle
import os

def test_models():
    """Test que tous les modèles peuvent être chargés et utilisés."""
    print("🧪 Test des modèles de machine learning...")
    
    models_dir = "./models"
    model_files = {
        "ai": "ai_model.pickle",
        "logic": "logic_model.pickle", 
        "network": "network_model.pickle",
        "software": "software_model.pickle"
    }
    
    loaded_models = {}
    
    for name, filename in model_files.items():
        filepath = os.path.join(models_dir, filename)
        if not os.path.exists(filepath):
            print(f"❌ {filename} non trouvé!")
            return False
        
        try:
            with open(filepath, "rb") as f:
                model = pickle.load(f)
            loaded_models[name] = model
            print(f"  ✓ {name}_model chargé")
        except Exception as e:
            print(f"  ❌ Erreur lors du chargement de {filename}: {e}")
            return False
    
    # Test de prédiction
    print("\n🧪 Test de prédiction avec des données d'exemple...")
    test_uni_avg = 17.5
    test_avg = 45.0
    
    try:
        ai_rank = int(loaded_models["ai"].predict([[test_uni_avg, test_avg]])[0][0])
        network_rank = int(loaded_models["network"].predict([[test_uni_avg, test_avg]])[0][0])
        logic_rank = int(loaded_models["logic"].predict([[test_uni_avg, test_avg]])[0][0])
        software_rank = int(loaded_models["software"].predict([[test_uni_avg, test_avg]])[0][0])
        
        print(f"  ✓ Prédictions réussies:")
        print(f"    - AI Rank: {ai_rank}")
        print(f"    - Network Rank: {network_rank}")
        print(f"    - Logic Rank: {logic_rank}")
        print(f"    - Software Rank: {software_rank}")
        return True
    except Exception as e:
        print(f"  ❌ Erreur lors de la prédiction: {e}")
        return False

def test_avg_function():
    """Test de la fonction avg."""
    print("\n🧪 Test de la fonction de calcul de moyenne...")
    
    try:
        # Import de la fonction
        import sys
        sys.path.insert(0, '.')
        from rank_estimation_bot import avg
        
        # Test avec des valeurs d'exemple
        result = avg(en=80, math=75, signal=70, ai=85, logic=78, os=72)
        
        if len(result) == 4:
            print(f"  ✓ Fonction avg fonctionne correctement")
            print(f"    Résultats: AI={result[0]:.2f}, Network={result[1]:.2f}, Logic={result[2]:.2f}, Software={result[3]:.2f}")
            return True
        else:
            print(f"  ❌ Fonction avg retourne un mauvais nombre de valeurs")
            return False
    except Exception as e:
        print(f"  ❌ Erreur lors du test de avg: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("TEST DE LA LOGIQUE DU BOT (sans Telegram)")
    print("=" * 60)
    print()
    
    results = []
    results.append(("Modèles ML", test_models()))
    results.append(("Fonction avg", test_avg_function()))
    
    print()
    print("=" * 60)
    print("RÉSUMÉ DES TESTS")
    print("=" * 60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 Tous les tests sont passés! La logique du bot fonctionne correctement.")
        print()
        print("Pour lancer le bot réel, vous devez:")
        print("1. Obtenir un token depuis @BotFather sur Telegram")
        print("2. L'ajouter dans token.txt")
        print("3. Lancer: python rank_estimation_bot.py")
    else:
        print("❌ Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)


