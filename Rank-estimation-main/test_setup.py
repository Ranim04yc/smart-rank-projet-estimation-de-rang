"""
Script de test pour vérifier que tout est configuré correctement.
"""

import os
import sys
import pickle

def test_imports():
    """Test que toutes les dépendances sont installées."""
    print("Testing imports...")
    try:
        import telegram
        import pandas
        import numpy
        import sklearn
        print("✓ All required packages are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing package: {e}")
        return False

def test_models():
    """Test que tous les modèles existent et peuvent être chargés."""
    print("\nTesting models...")
    models = ['ai_model.pickle', 'logic_model.pickle', 'network_model.pickle', 'software_model.pickle']
    all_exist = True
    
    for model_name in models:
        model_path = os.path.join('models', model_name)
        if not os.path.exists(model_path):
            print(f"✗ {model_name} not found")
            all_exist = False
        else:
            try:
                with open(model_path, 'rb') as f:
                    model = pickle.load(f)
                print(f"✓ {model_name} loaded successfully")
            except Exception as e:
                print(f"✗ Error loading {model_name}: {e}")
                all_exist = False
    
    return all_exist

def test_data_file():
    """Test que le fichier de données existe."""
    print("\nTesting data file...")
    if os.path.exists('rankdata.xlsm'):
        print("✓ rankdata.xlsm exists")
        return True
    else:
        print("✗ rankdata.xlsm not found")
        return False

def test_token_config():
    """Test la configuration du token."""
    print("\nTesting token configuration...")
    token = os.getenv("TELEGRAM_BOT_TOKEN", None)
    if token and token != "#YOUR_TOKEN":
        print("✓ TELEGRAM_BOT_TOKEN is set")
        return True
    else:
        print("⚠ TELEGRAM_BOT_TOKEN not set (you'll need to set it before running the bot)")
        print("  Set it with: $env:TELEGRAM_BOT_TOKEN='your_token'")
        return False

def main():
    print("=" * 50)
    print("Rank Estimation Bot - Setup Test")
    print("=" * 50)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Models", test_models()))
    results.append(("Data file", test_data_file()))
    token_set = test_token_config()
    
    print("\n" + "=" * 50)
    print("Summary:")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        if token_set:
            print("\n🎉 Everything is ready! You can run the bot with:")
            print("   python rank_estimation_bot.py")
        else:
            print("\n⚠️  Almost ready! Just set your Telegram bot token:")
            print("   $env:TELEGRAM_BOT_TOKEN='your_token_here'")
            print("   python rank_estimation_bot.py")
    else:
        print("\n❌ Some issues need to be fixed before running the bot.")
        sys.exit(1)

if __name__ == "__main__":
    main()


