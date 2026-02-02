# 🚀 Démarrage Rapide

Guide de démarrage en **5 minutes** pour créer votre premier mod Sims 4 avec l'IA !

## Étape 1 : Installation (2 min)

```bash
# Cloner le projet
git clone https://github.com/toinou181/sims4pythonai.git
cd sims4pythonai

# Installer les dépendances
pip install -r requirements.txt
```

## Étape 2 : Obtenir une clé API (2 min)

1. Allez sur https://makersuite.google.com/app/apikey
2. Cliquez sur "Create API Key"
3. Copiez la clé générée

## Étape 3 : Configuration (30 sec)

```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer le fichier .env et ajouter votre clé
# GOOGLE_API_KEY=votre_cle_ici
```

Sur Windows, utilisez `notepad .env` pour éditer.
Sur Linux/Mac, utilisez `nano .env` ou votre éditeur préféré.

## Étape 4 : Créer votre premier mod ! (30 sec)

### Option A : Mode interactif (Recommandé)

```bash
python sims4_mod_creator.py
```

Suivez les instructions à l'écran :
1. Choisissez "1" pour Google AI Studio
2. Décrivez votre mod (ex: "Un mod qui donne 10000§ quand le Sim lit")
3. Donnez un nom (ex: "MoneyFromReading")

### Option B : Ligne de commande

```bash
python sims4_mod_creator.py \
  --description "Un mod qui donne 10000§ quand le Sim lit" \
  --name "MoneyFromReading"
```

## Étape 5 : Installer le mod dans le jeu

1. Trouvez votre dossier Mods :
   - **Windows** : `Documents\Electronic Arts\The Sims 4\Mods\`
   - **Mac** : `Documents/Electronic Arts/The Sims 4/Mods/`

2. Copiez le fichier `.py` du mod depuis `generated_mods/[nom_du_mod]/`

3. Dans le jeu :
   - Options → Autres
   - ✅ Activer les mods personnalisés
   - ✅ Autoriser les mods de script
   - Redémarrer le jeu

## 🎉 C'est tout !

Vous pouvez maintenant créer autant de mods que vous voulez !

---

## 📦 Bonus : Créer un exécutable

Pour utiliser l'application sans Python :

**Windows :**
```cmd
build.bat
```

**Linux/Mac :**
```bash
./build.sh
```

L'exécutable sera dans `dist/`

---

## 💡 Exemples d'idées de mods

- "Les Sims gagnent 2x plus d'argent au travail"
- "Les compétences s'apprennent 5 fois plus vite"
- "Ajoute une interaction sociale 'Blague épique'"
- "Les Sims ont besoin de moins de sommeil"
- "Augmente la vitesse de déplacement des Sims"

---

## ❓ Besoin d'aide ?

- Consultez le [README.md](README.md) pour la documentation complète
- Consultez le [USAGE_GUIDE.md](USAGE_GUIDE.md) pour des exemples détaillés
- Ouvrez une issue sur GitHub

**Amusez-vous bien ! 🎮**
