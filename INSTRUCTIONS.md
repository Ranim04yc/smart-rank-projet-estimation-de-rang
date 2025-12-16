# Instructions d'exécution - Bot d'estimation de rang

## ✅ État actuel

Tout est configuré et prêt à être exécuté ! Les éléments suivants ont été mis en place :

- ✅ Toutes les dépendances Python sont installées
- ✅ Les modèles de machine learning ont été générés dans `./models/`
- ✅ Le code a été vérifié et est sans erreur
- ⚠️ Il ne reste plus qu'à configurer le token Telegram

## 🚀 Pour démarrer le bot

### Étape 1 : Obtenir un token Telegram

1. Ouvrez Telegram et cherchez **@BotFather**
2. Envoyez la commande `/newbot`
3. Suivez les instructions pour créer votre bot
4. Copiez le token fourni (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Étape 2 : Configurer le token

**Option A - Variable d'environnement (recommandé pour Windows PowerShell):**
```powershell
$env:TELEGRAM_BOT_TOKEN="votre_token_ici"
```

**Option B - Variable d'environnement (pour CMD):**
```cmd
set TELEGRAM_BOT_TOKEN=votre_token_ici
```

### Étape 3 : Lancer le bot

```powershell
python rank_estimation_bot.py
```

Le bot devrait démarrer et afficher des messages de log. Vous pouvez maintenant l'utiliser sur Telegram !

## 📁 Structure du projet

```
Rank-estimation-main/
├── rank_estimation_bot.py    # Code principal du bot
├── generate_models.py        # Script pour générer les modèles
├── test_setup.py            # Script de test de configuration
├── requirements.txt         # Dépendances Python
├── rankdata.xlsm           # Données d'entraînement
├── models/                 # Modèles ML (générés automatiquement)
│   ├── ai_model.pickle
│   ├── logic_model.pickle
│   ├── network_model.pickle
│   └── software_model.pickle
└── logs.txt                # Fichier de logs (créé automatiquement)
```

## 🧪 Tester la configuration

Pour vérifier que tout est correctement configuré :

```powershell
python test_setup.py
```

## 📝 Utilisation du bot

Une fois le bot lancé :

1. Cherchez votre bot sur Telegram
2. Envoyez `/start` pour commencer
3. Utilisez `/rank_estimation` pour estimer votre rang
4. Suivez les instructions du bot (en persan/farsi)

## ⚠️ Notes importantes

- Le bot doit rester en cours d'exécution pour fonctionner
- Les logs sont sauvegardés dans `logs.txt`
- Si vous modifiez les données d'entraînement (`rankdata.xlsm`), vous devrez régénérer les modèles avec `python generate_models.py`

## 🔧 Dépannage

**Erreur "TELEGRAM_BOT_TOKEN not set":**
- Vérifiez que vous avez bien défini la variable d'environnement
- Redémarrez le terminal après avoir défini la variable

**Erreur "Model file not found":**
- Exécutez `python generate_models.py` pour générer les modèles

**Erreur d'import:**
- Réinstallez les dépendances : `pip install -r requirements.txt`


