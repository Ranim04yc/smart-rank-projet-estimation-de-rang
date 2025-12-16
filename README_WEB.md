# 🌐 Interface Web - Estimation de Rang

## ✅ Interface Web Créée !

Une interface web moderne et intuitive a été créée pour utiliser le système d'estimation de rang.

## 🚀 Lancer l'interface web

### Méthode 1: Commande Python
```powershell
python app.py
```

### Méthode 2: Fichier batch (Windows)
Double-cliquez sur `LANCER_WEB.bat`

## 📱 Accéder à l'interface

Une fois le serveur lancé, ouvrez votre navigateur sur:

**http://localhost:5000**

## 🎨 Fonctionnalités

- ✅ Interface moderne et responsive
- ✅ Formulaire intuitif pour entrer les notes
- ✅ Calcul automatique des rangs
- ✅ Affichage de 3 scénarios:
  - 🌟 Vision Optimiste
  - 📊 Vision Réaliste  
  - ⚠️ Vision Pessimiste
- ✅ Support bilingue (Français/Persan)

## 📝 Utilisation

1. Entrez vos notes pour chaque matière (en pourcentage)
2. Entrez votre moyenne universitaire (sur 20)
3. Cliquez sur "محاسبه رتبه" (Calculer le Rang)
4. Consultez les résultats pour chaque spécialité

## 🔧 Structure

- `app.py` - Serveur Flask
- `templates/index.html` - Interface web
- `models/` - Modèles ML (utilisés par l'API)

## 🌐 API Endpoint

L'interface utilise l'API REST:
- **POST** `/api/estimate`
- Body JSON: `{english, math, signal, ai, logic, os, uni_avg}`
- Retourne les rangs estimés pour chaque spécialité

## ⚙️ Configuration

Le serveur écoute sur:
- **Host:** 0.0.0.0 (toutes les interfaces)
- **Port:** 5000
- **Mode:** Debug (pour le développement)

Pour changer le port, modifiez `app.py` ligne finale:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 🛑 Arrêter le serveur

Appuyez sur **Ctrl+C** dans le terminal où le serveur tourne.


