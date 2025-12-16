"""
Script interactif pour configurer le token Telegram.
"""

import os

def setup_token():
    print("=" * 60)
    print("Configuration du Token Telegram")
    print("=" * 60)
    print()
    print("Pour obtenir un token Telegram:")
    print("1. Ouvrez Telegram et cherchez @BotFather")
    print("2. Envoyez la commande /newbot")
    print("3. Suivez les instructions pour créer votre bot")
    print("4. Copiez le token fourni (format: 123456789:ABCdef...)")
    print()
    print("-" * 60)
    
    token = input("Entrez votre token Telegram: ").strip()
    
    if not token or token == "":
        print("❌ Token vide, configuration annulée.")
        return
    
    # Mettre à jour config.py
    try:
        with open("config.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remplacer le token
        if "TELEGRAM_BOT_TOKEN = " in content:
            lines = content.split("\n")
            new_lines = []
            for line in lines:
                if line.strip().startswith("TELEGRAM_BOT_TOKEN = "):
                    new_lines.append(f'TELEGRAM_BOT_TOKEN = "{token}"')
                else:
                    new_lines.append(line)
            
            with open("config.py", "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            
            print()
            print("✅ Token configuré avec succès dans config.py!")
            print()
            print("Vous pouvez maintenant lancer le bot avec:")
            print("   python rank_estimation_bot.py")
        else:
            print("❌ Erreur: format de config.py non reconnu")
    except Exception as e:
        print(f"❌ Erreur lors de la configuration: {e}")
        print()
        print("Vous pouvez configurer manuellement en éditant config.py")

if __name__ == "__main__":
    setup_token()


