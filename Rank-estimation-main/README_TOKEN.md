# 🔑 Configuration du Token Telegram

## Méthode la plus simple (RECOMMANDÉE)

1. **Ouvrez le fichier `token.txt`**
2. **Remplacez `#YOUR_TOKEN` par votre token Telegram**
3. **Sauvegardez le fichier**

C'est tout ! Le bot lira automatiquement le token depuis ce fichier.

## Obtenir un token Telegram

1. Ouvrez Telegram (sur mobile ou desktop)
2. Cherchez **@BotFather** dans la recherche
3. Envoyez la commande `/newbot`
4. Suivez les instructions :
   - Donnez un nom à votre bot
   - Donnez un username à votre bot (doit finir par "bot")
5. **Copiez le token** fourni (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Autres méthodes (optionnelles)

### Méthode 2: Fichier config.py
Éditez `config.py` et modifiez la ligne:
```python
TELEGRAM_BOT_TOKEN = "votre_token_ici"
```

### Méthode 3: Variable d'environnement
```powershell
$env:TELEGRAM_BOT_TOKEN="votre_token_ici"
```

## Ordre de priorité

Le bot cherche le token dans cet ordre:
1. Variable d'environnement `TELEGRAM_BOT_TOKEN`
2. Fichier `config.py`
3. Fichier `token.txt` ⭐ (le plus simple)
4. Sinon, affiche une erreur

## Après configuration

Une fois le token configuré, lancez simplement:
```powershell
python rank_estimation_bot.py
```


