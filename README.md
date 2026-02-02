# 🎮 Sims 4 Python AI - Créateur de Mods avec IA

Un programme Python puissant pour créer des mods pour Les Sims 4 en utilisant l'intelligence artificielle de Google (AI Studio et Vertex AI).

## 📚 Documentation Rapide

- **[🚀 Démarrage Rapide (5 min)](QUICKSTART.md)** - Commencez immédiatement
- **[📖 Guide d'Utilisation Complet](USAGE_GUIDE.md)** - Documentation détaillée avec exemples
- **[🎬 Démo sans API](demo.py)** - Testez sans clé API

## ✨ Fonctionnalités

- 🤖 **Deux moteurs d'IA** : Google AI Studio (Gemini) et Google Vertex AI
- 🎮 **Génération automatique de mods** pour Les Sims 4
- 📦 **Packaging automatique** des mods créés
- 💻 **Mode interactif** facile à utiliser
- ⌨️ **Mode ligne de commande** pour l'automatisation
- 🚀 **Création d'exécutable** avec PyInstaller

## 📋 Prérequis

- Python 3.8 ou supérieur
- Un compte Google Cloud ou accès à Google AI Studio
- Une des clés API suivantes :
  - Clé API Google AI Studio (Gemini) - **Recommandé pour débuter**
  - Projet Google Cloud avec Vertex AI activé

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/toinou181/sims4pythonai.git
cd sims4pythonai
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configuration des clés API

Copiez le fichier `.env.example` vers `.env` :

```bash
cp .env.example .env
```

Éditez le fichier `.env` et ajoutez vos clés :

#### Pour Google AI Studio (Gemini) - Recommandé

```env
GOOGLE_API_KEY=votre_cle_api_gemini
```

Pour obtenir une clé API :
1. Allez sur https://makersuite.google.com/app/apikey
2. Créez une nouvelle clé API
3. Copiez-la dans votre fichier `.env`

#### Pour Google Vertex AI (optionnel)

```env
GOOGLE_CLOUD_PROJECT=votre_project_id
GOOGLE_CLOUD_LOCATION=us-central1
```

Configuration requise :
1. Créez un projet sur Google Cloud Console
2. Activez l'API Vertex AI
3. Configurez l'authentification (gcloud auth application-default login)

## 💻 Utilisation

### Mode Interactif (Recommandé)

Lancez simplement le programme :

```bash
python sims4_mod_creator.py
```

Le programme vous guidera à travers :
1. Le choix du moteur d'IA
2. La description de votre mod
3. Le nom de votre mod

### Mode Ligne de Commande

```bash
# Avec Google AI Studio (Gemini)
python sims4_mod_creator.py --description "Un mod qui ajoute des interactions sociales amusantes" --name "FunSocial"

# Avec Vertex AI
python sims4_mod_creator.py --description "Un mod pour gagner plus d'argent au travail" --name "MoneyBoost" --provider vertex
```

### Options de ligne de commande

```
Options:
  --description, -d   Description du mod à créer (requis)
  --name, -n          Nom du mod (défaut: custom_mod)
  --provider, -p      Fournisseur d'IA: gemini ou vertex (défaut: gemini)
  --help, -h          Affiche l'aide
```

## 🎯 Exemples de mods

Voici quelques exemples de descriptions que vous pouvez utiliser :

1. **Mod de carrière** : "Un mod qui permet aux Sims de gagner 2x plus d'argent dans leurs carrières"
2. **Mod social** : "Ajoute une nouvelle interaction sociale 'Raconter une blague épique' qui rend tous les Sims heureux"
3. **Mod de compétences** : "Un mod qui fait apprendre les compétences 3 fois plus vite"
4. **Mod d'objets** : "Ajoute un nouveau lit qui donne un bonus d'énergie au réveil"

## 📦 Création d'un exécutable avec PyInstaller

Pour créer un exécutable autonome qui ne nécessite pas Python :

```bash
# Installation de PyInstaller (déjà dans requirements.txt)
pip install pyinstaller

# Création de l'exécutable
pyinstaller sims4_mod_creator.spec
```

L'exécutable sera créé dans le dossier `dist/`.

### Pour Windows :
```bash
dist/Sims4ModCreator.exe
```

### Pour Linux/Mac :
```bash
./dist/Sims4ModCreator
```

## 📁 Structure des fichiers

```
sims4pythonai/
├── sims4_mod_creator.py      # Application principale
├── sims4_mod_creator.spec    # Configuration PyInstaller
├── requirements.txt           # Dépendances Python
├── .env.example              # Exemple de configuration
├── .env                      # Votre configuration (à créer)
├── .gitignore               # Fichiers à ignorer
├── README.md                # Ce fichier
└── generated_mods/          # Dossier des mods générés (créé automatiquement)
    └── [vos_mods]/
```

## 🔧 Installation des mods dans Les Sims 4

1. Localisez votre dossier Mods :
   - Windows : `Documents\Electronic Arts\The Sims 4\Mods\`
   - Mac : `Documents/Electronic Arts/The Sims 4/Mods/`

2. Copiez le fichier `.py` du mod généré dans ce dossier

3. Dans le jeu :
   - Allez dans Options → Autres → Activer les mods personnalisés
   - Activez "Autoriser les mods de script"
   - Redémarrez le jeu

⚠️ **Important** : Testez toujours les mods sur une sauvegarde séparée !

## 🛠️ Développement

### Architecture

Le programme utilise une architecture modulaire :

- `AIProvider` : Classe de base pour les fournisseurs d'IA
- `GoogleAIStudioProvider` : Implémentation pour Google AI Studio (Gemini)
- `VertexAIProvider` : Implémentation pour Google Vertex AI
- `Sims4ModCreator` : Classe principale de création de mods

### Ajouter un nouveau fournisseur d'IA

Pour ajouter un nouveau fournisseur d'IA, créez une classe héritant de `AIProvider` :

```python
class MonNouveauProvider(AIProvider):
    def __init__(self, api_key: str):
        # Initialisation
        pass
    
    def generate_code(self, prompt: str) -> str:
        # Implémentation de la génération
        pass
```

## 🐛 Dépannage

### Erreur : "GOOGLE_API_KEY non définie"

- Vérifiez que vous avez créé le fichier `.env`
- Assurez-vous d'avoir copié votre clé API correctement

### Erreur lors de l'import de google.generativeai

```bash
pip install --upgrade google-generativeai
```

### Problèmes avec Vertex AI

- Vérifiez que vous êtes authentifié : `gcloud auth application-default login`
- Vérifiez que l'API Vertex AI est activée dans votre projet Google Cloud

### L'exécutable ne fonctionne pas

- Assurez-vous d'avoir un fichier `.env` dans le même dossier que l'exécutable
- Vérifiez les logs dans la console

## 📝 Licence

Ce projet est open source. Utilisez-le librement pour créer vos mods !

## ⚠️ Avertissement

- Les mods générés par IA doivent toujours être testés avant utilisation
- Electronic Arts n'est pas responsable des mods tiers
- Faites des sauvegardes de vos parties avant d'installer des mods
- Certains mods peuvent ne pas fonctionner avec toutes les versions du jeu

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Améliorer la documentation

## 📧 Support

Pour toute question ou problème, ouvrez une issue sur GitHub.

---

**Créé avec ❤️ pour la communauté Les Sims 4**