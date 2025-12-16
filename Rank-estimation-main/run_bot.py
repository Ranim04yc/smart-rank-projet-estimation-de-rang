"""
Script de lancement interactif du bot Telegram.
Demande le token si nécessaire et lance le bot.
"""

import os
import sys

def get_token():
    """Récupère le token depuis différentes sources."""
    # 1. Variable d'environnement
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if token and token.strip() and token != "#YOUR_TOKEN":
        return token
    
    # 2. Fichier config.py
    try:
        from config import TELEGRAM_BOT_TOKEN
        if TELEGRAM_BOT_TOKEN and TELEGRAM_BOT_TOKEN.strip() and TELEGRAM_BOT_TOKEN != "#YOUR_TOKEN":
            return TELEGRAM_BOT_TOKEN
    except:
        pass
    
    # 3. Fichier token.txt
    try:
        if os.path.exists("token.txt"):
            with open("token.txt", "r", encoding="utf-8") as f:
                token = f.read().strip()
                token = token.split("#")[0].strip()
                if token and token != "#YOUR_TOKEN":
                    return token
    except:
        pass
    
    return None

def main():
    print("=" * 60)
    print("🤖 Lancement du Bot d'Estimation de Rang")
    print("=" * 60)
    print()
    
    token = get_token()
    
    if not token:
        print("⚠️  Token Telegram non configuré!")
        print()
        print("Pour obtenir un token:")
        print("1. Ouvrez Telegram et cherchez @BotFather")
        print("2. Envoyez /newbot et suivez les instructions")
        print("3. Copiez le token fourni")
        print()
        print("-" * 60)
        
        user_token = input("Entrez votre token Telegram (ou appuyez sur Entrée pour annuler): ").strip()
        
        if not user_token:
            print("❌ Annulation. Configurez le token et réessayez.")
            print()
            print("Vous pouvez:")
            print("  - Éditer token.txt et y mettre votre token")
            print("  - Éditer config.py et y mettre votre token")
            print("  - Définir: $env:TELEGRAM_BOT_TOKEN='votre_token'")
            sys.exit(1)
        
        # Sauvegarder dans token.txt
        try:
            with open("token.txt", "w", encoding="utf-8") as f:
                f.write(user_token)
            print("✅ Token sauvegardé dans token.txt")
            token = user_token
        except Exception as e:
            print(f"⚠️  Impossible de sauvegarder dans token.txt: {e}")
            print("   Utilisation du token pour cette session uniquement")
    else:
        print("✅ Token trouvé dans la configuration")
    
    print()
    print("🚀 Démarrage du bot...")
    print("   Appuyez sur Ctrl+C pour arrêter le bot")
    print("=" * 60)
    print()
    
    # Définir la variable d'environnement pour cette session
    os.environ["TELEGRAM_BOT_TOKEN"] = token
    
    # Importer et lancer le bot
    try:
        from rank_estimation_bot import main as bot_main
        bot_main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Bot arrêté par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur lors du lancement du bot: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()


