# Guide d'installation et d'exécution

## Prérequis
- Python 3.8 ou supérieur
- Un token de bot Telegram (obtenu via @BotFather)

## Installation

### 1. Installer les dépendances Python
```powershell
pip install -r requirements.txt
```

### 2. Générer les modèles de machine learning
```powershell
python generate_models.py
```

Cette étape va créer le dossier `models/` avec les fichiers pickle nécessaires.

### 3. Configurer le token Telegram

**Option A: Variable d'environnement (recommandé)**
```powershell
$env:TELEGRAM_BOT_TOKEN="votre_token_ici"
```

**Option B: Fichier .env**
Créez un fichier `.env` à la racine du projet avec:
```
TELEGRAM_BOT_TOKEN=votre_token_ici
```

Pour obtenir un token:
1. Ouvrez Telegram et cherchez @BotFather
2. Envoyez `/newbot` et suivez les instructions
3. Copiez le token fourni

### 4. Exécuter le bot
```powershell
python rank_estimation_bot.py
```

## Structure des fichiers

- `rank_estimation_bot.py` - Code principal du bot Telegram
- `generate_models.py` - Script pour générer les modèles ML
- `rankdata.xlsm` - Données d'entraînement
- `models/` - Dossier contenant les modèles pickle (généré automatiquement)
- `requirements.txt` - Dépendances Python

## Notes

- Le bot nécessite que tous les fichiers de modèles soient présents dans `./models/`
- Les logs sont sauvegardés dans `logs.txt`
- Le bot répond en persan/farsi


