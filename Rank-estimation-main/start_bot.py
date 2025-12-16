"""
Script de lancement automatique du bot.
Fait tout le nécessaire pour démarrer le bot.
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path

def check_token():
    """Vérifie si un token est configuré."""
    # 1. Variable d'environnement
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token and token.strip() and token != "#YOUR_TOKEN":
        return token, "environment variable"
    
    # 2. Fichier config.py
    try:
        from config import TELEGRAM_BOT_TOKEN
        if TELEGRAM_BOT_TOKEN and TELEGRAM_BOT_TOKEN.strip() and TELEGRAM_BOT_TOKEN != "#YOUR_TOKEN":
            return TELEGRAM_BOT_TOKEN, "config.py"
    except:
        pass
    
    # 3. Fichier token.txt
    try:
        if os.path.exists("token.txt"):
            with open("token.txt", "r", encoding="utf-8") as f:
                token = f.read().strip()
                token = token.split("#")[0].strip()
                if token and token != "#YOUR_TOKEN" and len(token) > 10:
                    return token, "token.txt"
    except:
        pass
    
    return None, None

def print_header():
    """Affiche l'en-tête."""
    print("\n" + "=" * 70)
    print(" " * 20 + "🤖 BOT TELEGRAM - ESTIMATION DE RANG")
    print("=" * 70 + "\n")

def print_instructions():
    """Affiche les instructions pour obtenir un token."""
    print("📱 POUR OBTENIR UN TOKEN TELEGRAM:")
    print("-" * 70)
    print()
    print("1. Ouvrez Telegram (sur votre téléphone ou ordinateur)")
    print("2. Cherchez: @BotFather")
    print("3. Envoyez la commande: /newbot")
    print("4. Suivez les instructions:")
    print("   - Donnez un nom à votre bot (ex: Mon Bot de Rang)")
    print("   - Donnez un username (doit finir par 'bot', ex: monbotderang_bot)")
    print("5. BotFather vous donnera un TOKEN")
    print("6. Copiez ce token (format: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz)")
    print()
    print("-" * 70)
    print()
    print("💾 POUR CONFIGURER LE TOKEN:")
    print()
    print("   Option 1 (RECOMMANDÉ):")
    print("   - Ouvrez le fichier 'token.txt' dans ce dossier")
    print("   - Remplacez #YOUR_TOKEN par votre token")
    print("   - Sauvegardez")
    print()
    print("   Option 2:")
    print("   - Dans PowerShell: $env:TELEGRAM_BOT_TOKEN='votre_token'")
    print()
    print("=" * 70)
    print()

def open_telegram_link():
    """Ouvre le lien Telegram dans le navigateur."""
    try:
        print("🌐 Ouverture de Telegram Web...")
        webbrowser.open("https://web.telegram.org")
        print("   (Si Telegram Web ne s'ouvre pas, ouvrez Telegram manuellement)")
    except:
        print("   (Impossible d'ouvrir automatiquement, ouvrez Telegram manuellement)")

def main():
    """Fonction principale."""
    print_header()
    
    # Vérifier les prérequis
    print("🔍 Vérification de la configuration...")
    print()
    
    # Vérifier Python
    try:
        import telegram
        import pandas
        import sklearn
        print("  ✅ Dépendances Python installées")
    except ImportError as e:
        print(f"  ❌ Dépendances manquantes: {e}")
        print("     Exécutez: pip install -r requirements.txt")
        return False
    
    # Vérifier les modèles
    models_exist = all(os.path.exists(f"models/{m}") for m in [
        "ai_model.pickle", "logic_model.pickle", 
        "network_model.pickle", "software_model.pickle"
    ])
    if models_exist:
        print("  ✅ Modèles ML présents")
    else:
        print("  ❌ Modèles ML manquants")
        print("     Exécutez: python generate_models.py")
        return False
    
    # Vérifier le token
    token, source = check_token()
    print()
    
    if token:
        print(f"  ✅ Token trouvé dans: {source}")
        print()
        print("🚀 Lancement du bot...")
        print("   Appuyez sur Ctrl+C pour arrêter")
        print("=" * 70)
        print()
        
        # Définir la variable d'environnement
        os.environ["TELEGRAM_BOT_TOKEN"] = token
        
        # Lancer le bot
        try:
            from rank_estimation_bot import main as bot_main
            bot_main()
        except KeyboardInterrupt:
            print("\n\n⏹️  Bot arrêté par l'utilisateur")
            return True
        except Exception as e:
            print(f"\n❌ Erreur lors du lancement: {e}")
            import traceback
            traceback.print_exc()
            return False
    else:
        print("  ⚠️  Token Telegram non configuré")
        print()
        print_instructions()
        
        # Demander si l'utilisateur veut ouvrir Telegram
        print("Voulez-vous ouvrir Telegram maintenant? (o/n): ", end="")
        try:
            response = input().strip().lower()
            if response in ['o', 'oui', 'y', 'yes']:
                open_telegram_link()
        except:
            pass
        
        print()
        print("💡 ASTUCE: Une fois que vous avez le token,")
        print("   éditez 'token.txt' et relancez ce script!")
        print()
        print("   Ou entrez le token maintenant (appuyez sur Entrée pour annuler): ", end="")
        
        try:
            user_token = input().strip()
            if user_token and len(user_token) > 10:
                # Sauvegarder dans token.txt
                try:
                    with open("token.txt", "w", encoding="utf-8") as f:
                        f.write(user_token)
                    print("✅ Token sauvegardé dans token.txt")
                    print()
                    print("🚀 Relancement avec le nouveau token...")
                    print("=" * 70)
                    print()
                    
                    os.environ["TELEGRAM_BOT_TOKEN"] = user_token
                    from rank_estimation_bot import main as bot_main
                    bot_main()
                except Exception as e:
                    print(f"❌ Erreur: {e}")
                    return False
            else:
                print("❌ Token invalide ou annulé")
                return False
        except KeyboardInterrupt:
            print("\n❌ Annulé par l'utilisateur")
            return False
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
            return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n👋 Au revoir!")
        sys.exit(0)


