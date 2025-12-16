# 🚀 Guide de Démarrage Rapide

## 📋 Étapes pour démarrer le projet après avoir éteint le PC

### Étape 1 : Ouvrir le terminal
- Appuyez sur `Windows + R`
- Tapez `powershell` et appuyez sur Entrée
- OU cherchez "PowerShell" dans le menu Démarrer

### Étape 2 : Aller dans le dossier du projet
```powershell
cd D:\Rank-estimation-main
```

### Étape 3 : Lancer le serveur web
```powershell
python app.py
```

### Étape 4 : Ouvrir le navigateur
- Le serveur affichera : `http://localhost:5000`
- Ouvrez votre navigateur (Chrome, Firefox, Edge)
- Allez sur : **http://localhost:5000**

---

## ✅ C'est tout !

Le projet est maintenant en cours d'exécution. Vous pouvez utiliser l'interface web.

---

## 🛑 Pour arrêter le serveur

Dans le terminal PowerShell, appuyez sur **Ctrl+C**

---

## ⚠️ Si vous avez des erreurs

### Erreur "python n'est pas reconnu"
- Vérifiez que Python est installé
- Réinstallez Python depuis python.org si nécessaire

### Erreur "Module not found"
```powershell
pip install -r requirements.txt
```

### Erreur "Models not found"
```powershell
python generate_models.py
```

---

## 📝 Commandes rapides

| Action | Commande |
|--------|----------|
| Démarrer le serveur | `python app.py` |
| Installer les dépendances | `pip install -r requirements.txt` |
| Générer les modèles | `python generate_models.py` |
| Tester la configuration | `python test_setup.py` |

---

## 💡 Astuce

Créez un raccourci sur le bureau qui lance directement le serveur :
1. Clic droit sur le bureau → Nouveau → Raccourci
2. Emplacement : `powershell.exe -NoExit -Command "cd D:\Rank-estimation-main; python app.py"`
3. Nom : "Lancer Estimation Rang"
